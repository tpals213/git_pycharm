# https://gymnasium.farama.org/environments/classic_control/cart_pole/
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import gymnasium as gym
import torch

from c_policy_and_value import MODEL_DIR, Policy


def test(env, policy, num_episodes):
    for i in range(num_episodes):
        episode_reward = 0  # cumulative_reward

        # Environment 초기화와 변수 초기화
        observation, _ = env.reset()

        episode_steps = 0

        done = False

        while not done:
            episode_steps += 1
            # action = policy.get_action(observation)
            action = policy.get_action(observation, exploration=False)

            next_observation, reward, terminated, truncated, _ = env.step(action * 2)

            episode_reward += reward
            observation = next_observation
            done = terminated or truncated

        print("[EPISODE: {0}] EPISODE_STEPS: {1:3d}, EPISODE REWARD: {2:4.1f}".format(
            i, episode_steps, episode_reward
        ))


def main_play(num_episodes, env_name):
    env = gym.make(env_name, render_mode="human")

    policy = Policy(n_features=2, n_actions=1)
    model_params = torch.load(os.path.join(MODEL_DIR, "reinforce_{0}_latest.pth".format(env_name)))
    policy.load_state_dict(model_params)

    test(env, policy, num_episodes=num_episodes)

    env.close()


if __name__ == "__main__":
    NUM_EPISODES = 3
    ENV_NAME = "MountainCarContinuous-v0"

    main_play(num_episodes=NUM_EPISODES, env_name=ENV_NAME)
