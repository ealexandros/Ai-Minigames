import pygame
import time
import random

from game.Board import BoardSingleton
from game.Snake import Snake
from game.Food import Food
from game.event_listener import EventListener

pygame.init()
pygame.display.set_caption('Q-Learning Snake')

FRAME_RATE = 8
clock = pygame.time.Clock()

board = BoardSingleton()
snake = Snake()
food = Food()
event = EventListener()
 
def SnakeGame():
    while not event.exit:
        event.listen()
        board.refresh_board()

        if(snake.snake_logic(event.x, event.y)):
            quit()
        
        if(snake.get_snake_head() == food.get_food_position()):
            snake.snake_lenght += 1

        food.food_logic(snake.get_snake_head())
 
        pygame.display.update()
        clock.tick(FRAME_RATE)

SnakeGame()