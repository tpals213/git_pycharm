# https://gymnasium.farama.org/environments/classic_control/cart_pole/
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import gymnasium as gym
import torch

from c_qnet import QNet, MODEL_DIR


def test(env, q, num_episodes):
    for i in range(num_episodes):
        episode_reward = 0  # cumulative_reward

        # Environment 초기화와 변수 초기화
        observation, _ = env.reset()

        episode_steps = 0

        done = False

        while not done:
            episode_steps += 1
            action = q.get_action(observation, epsilon=0.0)

            next_observation, reward, terminated, truncated, _ = env.step(action)

            episode_reward += reward
            observation = next_observation
            done = terminated or truncated

        print("[EPISODE: {0}] EPISODE_STEPS: {1:3d}, EPISODE REWARD: {2:4.1f}".format(
            i, episode_steps, episode_reward
        ))


def main_play(num_episodes, env_name):
    env_lunar = gym.make(env_name, render_mode="human")
    # env = gym.make(env_name)
    print(env_lunar.action_space)

    q = QNet(n_features=8, n_actions=4)
    model_params = torch.load(os.path.join(MODEL_DIR, "dqn_{0}_latest.pth".format(env_name)))
    q.load_state_dict(model_params)

    test(env_lunar, q, num_episodes)

    env_lunar.close()


if __name__ == "__main__":
    NUM_EPISODES = 3
    ENV_NAME = 'LunarLander-v2'

    main_play(num_episodes=NUM_EPISODES, env_name=ENV_NAME)
