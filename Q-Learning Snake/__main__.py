from tqdm import tqdm
import numpy as np

from game.SnakeGameEnv import SnakeGameEnv
from computer.MachineAgent import MachineAgent

import env

game_env = SnakeGameEnv()
agent = MachineAgent()

for episode in tqdm(range(1, env.EPISODES + 1), ascii=True, unit='episodes'):

    agent.tensorboard.step = episode
    current_state, done = game_env.reset()

    while(not done):
        if(np.random.random() > env.epsilon):
            action = np.argmax(agent.get_qs(current_state))
        else:
            action = np.random.randint(0, env.ACTION_SPACE_SIZE)

        new_state, reward, done = game_env.step(action)

        if(env.SHOW_PREVIEW and not episode % env.SHOW_PREVIEW):
            game_env.render()

        agent.update_replay_memory((current_state, action, reward, new_state, done))
        agent.train(done)

        current_state = new_state

    if(env.epsilon > env.MIN_EPSILON):
        env.epsilon = env.epsilon*env.EPSILON_DECAY
        env.epsilon = max(env.MIN_EPSILON, env.epsilon)

    # Graphs
    agent.tensorboard.update_stats(score=game_env.get_episode_score())
    if(not episode%env.AGGREGATE_STATS_EVERY or episode == 1):
        agent.tensorboard.update_stats(epsilon=env.epsilon)
