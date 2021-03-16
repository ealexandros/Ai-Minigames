from game.Board import BoardSingleton
import random

import env

class Food:
    def __init__(self):
        self.food_position = [0, 0]
        self.board = BoardSingleton.getInstance()
        self.set_new_food_coordinates()

    def __eq__(self, other):
        return self.food_position == other.snake_head

    def set_new_food_coordinates(self):
        self.food_position = [random.randint(0, env.BOARD_TABLE-1)*env.DOT_SIZE for _ in range(2)]

    def food_draw_frame(self):
        self.board.draw_rectangle(self.food_position)

    def get_food_xy(self):
        return [self.food_position[0]//env.DOT_SIZE, self.food_position[1]//env.DOT_SIZE]