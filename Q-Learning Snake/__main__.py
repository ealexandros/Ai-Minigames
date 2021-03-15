from tqdm import tqdm
import numpy as np

from game.SnakeGameEnv import SnakeGameEnv
from computer.MachineAgent import MachineAgent

import env

game_env = SnakeGameEnv()
agent = MachineAgent()

for episode in tqdm(range(1, env.EPISODES + 1), ascii=True, unit='episodes'):
    
    # Update tensorboard step every episode
    # agent.tensorboard.step = episode

    current_state, done = game_env.reset()

    while(not done):
        if(np.random.random() > env.epsilon):
            action = np.argmax(agent.get_qs(current_state))
        else:
            action = np.random.randint(0, env.ACTION_SPACE_SIZE)

        new_state, reward, done = game_env.step(action)

        if(env.SHOW_PREVIEW and not episode % env.AGGREGATE_STATS_EVERY):
            game_env.render()

        agent.update_replay_memory((current_state, action, reward, new_state, done))
        agent.train(done)

        current_state = new_state

    if(env.epsilon > env.MIN_EPSILON):
        env.epsilon = env.epsilon*env.EPSILON_DECAY
        env.epsilon = max(env.MIN_EPSILON, env.epsilon)