# https://gymnasium.farama.org/environments/classic_control/cart_pole/
import time
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import gymnasium as gym # gym으로 pip 설치
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
import wandb
from datetime import datetime
from shutil import copyfile

from c_qnet import QNet, ReplayBuffer, Transition, MODEL_DIR


class DQN:
    def __init__(self, env, test_env, config, use_wandb):
        self.env = env
        self.test_env = test_env
        self.use_wandb = use_wandb

        self.env_name = config["env_name"]

        self.current_time = datetime.now().astimezone().strftime('%Y-%m-%d_%H-%M-%S')

        if self.use_wandb:
            self.wandb = wandb.init(
                project="DQN_{0}".format(self.env_name),
                name=self.current_time,
                config=config
            )

        self.max_num_episodes = config["max_num_episodes"]
        self.batch_size = config["batch_size"]
        self.learning_rate = config["learning_rate"]
        self.gamma = config["gamma"]
        self.steps_between_train = config["steps_between_train"]
        self.target_sync_step_interval = config["target_sync_step_interval"]
        self.replay_buffer_size = config["replay_buffer_size"]
        self.epsilon_start = config["epsilon_start"]
        self.epsilon_end = config["epsilon_end"]
        self.epsilon_final_scheduled_percent = config["epsilon_final_scheduled_percent"]
        self.print_episode_interval = config["print_episode_interval"]
        self.train_num_episodes_before_next_test = config["train_num_episodes_before_next_test"]
        self.validation_num_episodes = config["validation_num_episodes"]
        self.episode_reward_avg_solved = config["episode_reward_avg_solved"]

        self.epsilon_scheduled_last_episode = self.max_num_episodes * self.epsilon_final_scheduled_percent

        # network
        # self.q = QNet(n_features=4, n_actions=2)
        self.q = QNet(n_features=8, n_actions=4)
        self.target_q = QNet(n_features=8, n_actions=4)
        self.target_q.load_state_dict(self.q.state_dict())

        self.optimizer = optim.Adam(self.q.parameters(), lr=self.learning_rate)

        # agent
        self.replay_buffer = ReplayBuffer(self.replay_buffer_size)

        self.time_steps = 0
        self.total_time_steps = 0
        self.training_time_steps = 0

    def epsilon_scheduled(self, current_episode):
        fraction = min(current_episode / self.epsilon_scheduled_last_episode, 1.0)

        epsilon = min(
            self.epsilon_start + fraction * (self.epsilon_end - self.epsilon_start),
            self.epsilon_start
        )
        return epsilon

    def train_loop(self):
        loss = 0.0

        total_train_start_time = time.time()

        validation_episode_reward_avg = 0.0

        is_terminated = False

        for n_episode in range(1, self.max_num_episodes + 1):
            epsilon = self.epsilon_scheduled(n_episode)

            episode_reward = 0

            observation, _ = self.env.reset()

            done = False

            while not done:
                self.time_steps += 1
                self.total_time_steps += 1

                action = self.q.get_action(observation, epsilon)

                next_observation, reward, terminated, truncated, _ = self.env.step(action)

                transition = Transition(observation, action, next_observation, reward, terminated)

                self.replay_buffer.append(transition)

                episode_reward += reward
                observation = next_observation
                done = terminated or truncated

                if self.total_time_steps % self.steps_between_train == 0 and self.time_steps > self.batch_size:
                    loss = self.train()

            total_training_time = time.time() - total_train_start_time
            total_training_time = time.strftime('%H:%M:%S', time.gmtime(total_training_time))

            if n_episode % self.print_episode_interval == 0:
                print(
                    "[Episode {:3,}, Time Steps {:6,}]".format(n_episode, self.time_steps),
                    "Episode Reward: {:>5},".format(episode_reward),
                    "Replay buffer: {:>6,},".format(self.replay_buffer.size()),
                    "Loss: {:6.3f},".format(loss),
                    "Epsilon: {:4.2f},".format(epsilon),
                    "Training Steps: {:5,},".format(self.training_time_steps),
                    "Elapsed Time: {}".format(total_training_time)
                )

            if n_episode % self.train_num_episodes_before_next_test == 0:
                validation_episode_reward_lst, validation_episode_reward_avg = self.validate()

                print("[Validation Episode Reward: {0}] Average: {1:.3f}".format(
                    validation_episode_reward_lst, validation_episode_reward_avg
                ))

                if validation_episode_reward_avg > self.episode_reward_avg_solved:
                    print("Solved in {0:,} steps ({1:,} training steps)!".format(
                        self.time_steps, self.training_time_steps
                    ))
                    self.model_save(validation_episode_reward_avg)
                    is_terminated = True

            if self.use_wandb:
                self.wandb.log({
                    "[VALIDATION] Mean Episode Reward ({0} Episodes)".format(self.validation_num_episodes): validation_episode_reward_avg,
                    "[TRAIN] Episode Reward": episode_reward,
                    "[TRAIN] Loss": loss if loss != 0.0 else 0.0,
                    "[TRAIN] Epsilon": epsilon,
                    "[TRAIN] Replay buffer": self.replay_buffer.size(),
                    "Training Episode": n_episode,
                    "Training Steps": self.training_time_steps
                })

            if is_terminated:
                break

        total_training_time = time.time() - total_train_start_time
        total_training_time = time.strftime('%H:%M:%S', time.gmtime(total_training_time))
        print("Total Training End : {}".format(total_training_time))
        self.wandb.finish()

    def train(self):
        self.training_time_steps += 1

        batch = self.replay_buffer.sample(self.batch_size)

        # observations.shape: torch.Size([32, 4]),
        # actions.shape: torch.Size([32, 1]),
        # next_observations.shape: torch.Size([32, 4]),
        # rewards.shape: torch.Size([32, 1]),
        # dones.shape: torch.Size([32])
        observations, actions, next_observations, rewards, dones = batch

        # state_action_values.shape: torch.Size([32, 1])
        q_out = self.q(observations)
        q_values = q_out.gather(dim=-1, index=actions)

        with torch.no_grad():
            q_prime_out = self.target_q(next_observations)
            # next_state_values.shape: torch.Size([32, 1])
            max_q_prime = q_prime_out.max(dim=1, keepdim=True).values
            max_q_prime[dones] = 0.0

            # target_state_action_values.shape: torch.Size([32, 1])
            targets = rewards + self.gamma * max_q_prime

        # loss is just scalar torch value
        loss = F.mse_loss(targets.detach(), q_values)

        # print("observations.shape: {0}, actions.shape: {1}, "
        #       "next_observations.shape: {2}, rewards.shape: {3}, dones.shape: {4}".format(
        #     observations.shape, actions.shape,
        #     next_observations.shape, rewards.shape, dones.shape
        # ))
        # print("state_action_values.shape: {0}".format(state_action_values.shape))
        # print("next_state_values.shape: {0}".format(next_state_values.shape))
        # print("target_state_action_values.shape: {0}".format(
        #     target_state_action_values.shape
        # ))
        # print("loss.shape: {0}".format(loss.shape))

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # sync
        if self.time_steps % self.target_sync_step_interval == 0:
            self.target_q.load_state_dict(self.q.state_dict())

        return loss.item()

    def model_save(self, validation_episode_reward_avg):
        filename = "dqn_{0}_{1:4.1f}_{2}.pth".format(
            self.env_name, validation_episode_reward_avg, self.current_time
        )
        torch.save(self.q.state_dict(), os.path.join(MODEL_DIR, filename))

        copyfile(
            src=os.path.join(MODEL_DIR, filename),
            dst=os.path.join(MODEL_DIR, "dqn_{0}_latest.pth".format(self.env_name))
        )

    def validate(self):
        episode_reward_lst = np.zeros(shape=(self.validation_num_episodes,), dtype=float)

        for i in range(self.validation_num_episodes):
            episode_reward = 0

            observation, _ = self.test_env.reset()

            done = False

            while not done:
                action = self.q.get_action(observation, epsilon=0.0)

                next_observation, reward, terminated, truncated, _ = self.test_env.step(action)

                episode_reward += reward
                observation = next_observation
                done = terminated or truncated

            episode_reward_lst[i] = episode_reward

        return episode_reward_lst, np.average(episode_reward_lst)


def main():
    ENV_NAME = "LunarLander-v2"
    env = gym.make(ENV_NAME)
    test_env =  gym.make(ENV_NAME)
    config = {
        "env_name": ENV_NAME,                    #환경의 이름
        "max_num_episodes": 1_500,              #훈련을 위한 최대 에피소드 횟수, _는 1000단위
        "batch_size": 32,                                 #훈련시 배치에서 한번에 가져오는 랜덤 배치 사이즈
        # "learning_rate": 0.0001,                       #학습율
        "learning_rate": 0.0005,  # 학습율 수정 적용
        "gamma": 0.99,                                     #감가율
        "steps_between_train": 1,                     #훈련 사이의 환경 스텝 수
        "target_sync_step_interval": 500,         #기존 Q 모델을 타깃 Q 모델로 동기화시키는 step 간격
        "replay_buffer_size": 300_000,             #리플레이 버퍼 사이즈
        "epsilon_start": 0.95,                           # Epsilon 초기 값
        "epsilon_end": 0.01,                             # Epsilon 최종 값
        "epsilon_final_scheduled_percent": 0.75,      # Epsilon 최종값 스케줄 마지막 에피소드 비율
        "print_episode_interval": 10,                # Episode 통계 출력에 관한 에피소드 간격
        "train_num_episodes_before_next_test": 50,  #검증 사이마다 각 훈련 episode 간격
        "validation_num_episodes": 3,              #검증에 수행하는 에피소드 횟수
        "episode_reward_avg_solved": 200,       #훈련 종료를 위한 검증 에피소드 리워드의 Average
    }
    use_wandb = True
    dqn = DQN(env=env, test_env=test_env, config=config, use_wandb=use_wandb)
    dqn.train_loop()


if __name__ == '__main__':
    main()
