import pygame
import time
import random
import numpy as np

from PIL import Image

import env
from game.Board import BoardSingleton
from game.Snake import Snake
from game.Food import Food
from game.EventListener import EventListener

class SnakeGameEnv():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Q-Learning Snake')

        self.clock = pygame.time.Clock()

        self.board = BoardSingleton.getInstance()
        self.food = Food()
        self.snake = Snake()
        self.event = EventListener()

    def step(self, action):
        self.snake.action(action)
        new_observation = np.array(self.get_image_map())

        reward = -env.MOVE_PENALTY
        if(self.snake.snake_invalid_move()):
            reward = -env.INVALID_MOVE_PENALTY
        elif(self.food == self.snake):
            reward = env.FOOD_REWARD

        if(self.food == self.snake):
            self.food.set_new_food_coordinates()
            self.board.add_score_point()
            self.snake.snake_lenght += 1

        done = False
        if(self.event.exit == True or self.snake.snake_invalid_move()):
            done = True

        return new_observation, reward, done

    def render(self):
        self.event.listener()
        self.board.refresh_board()

        self.food.food_draw_frame()
        self.snake.snake_draw_frame()

        pygame.display.update()
        self.clock.tick(env.FRAME_RATE)

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.board.restart()

        observation = np.array(self.get_image_map())
        return observation, False

    def calculate_snake_head(self):
        snake_head_temp = self.snake.get_snake_head()
        if(snake_head_temp[0] < 0):
            snake_head_temp[0] = 0
        elif(snake_head_temp[0] >= env.MAP_SIZE):
            snake_head_temp[0] = env.MAP_SIZE-env.DOT_SIZE
        if(snake_head_temp[1] < 0):
            snake_head_temp[1] = 0
        elif(snake_head_temp[1] >= env.MAP_SIZE):
            snake_head_temp[1] = env.MAP_SIZE-env.DOT_SIZE

        snake_head_temp = [snake_head_temp[0]//env.DOT_SIZE, snake_head_temp[1]//env.DOT_SIZE]
        return snake_head_temp

    def get_image_map(self):
        map_env = np.zeros((env.BOARD_SIZE, env.BOARD_SIZE, 3), dtype=np.uint8)

        food_location = self.food.get_food_xy()
        map_env[food_location[0]][food_location[1]] = self.board.COLOR["FD"]

        snake_head = self.calculate_snake_head()
        map_env[snake_head[0]][snake_head[1]] = self.board.COLOR["SN_HD"]

        snake_tail = self.snake.snake
        for x, y in snake_tail[:-1]:
            map_env[x//env.DOT_SIZE][y//env.DOT_SIZE] = self.board.COLOR["SN"]

        img = Image.fromarray(map_env, 'RGB')
        return img

    def get_episode_score(self):
        return self.board.score