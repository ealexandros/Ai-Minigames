import pygame
import time
import random

import env

from game.Board import BoardSingleton
from game.Snake import Snake
from game.Food import Food
from game.EventListener import EventListener

class SnakeGame():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Q-Learning Snake')

        self.clock = pygame.time.Clock()

        self.board = BoardSingleton()
        self.snake = Snake()
        self.food = Food()
        self.event = EventListener()

    def check_snake_food_collision(self):
        if(self.snake.get_snake_head() == self.food.get_food_position()):
            self.snake.snake_lenght += 1
        self.food.food_logic(self.snake.get_snake_head())

    def start(self):
        while(not self.event.exit):
            self.event.listener()
            self.board.refresh_board()

            if(self.snake.snake_logic(self.event.x, self.event.y)):
                quit()
            
            self.check_snake_food_collision()

            pygame.display.update()
            self.clock.tick(env.FRAME_RATE)