from game.Board import BoardSingleton
import random

class Food:
    def __init__(self):
        self.board = BoardSingleton()

        self.set_new_food_coordinates()
        self.FD_COLOR = (0, 255, 0)

    def set_new_food_coordinates(self):
        self.food_position = [random.randint(0, self.board.DOT_SIZE-1)*self.board.DOT_SIZE for _ in range(2)]

    def get_food_position(self):
        return self.food_position

    def food_logic(self, snake_position):
        if(snake_position[0] == self.food_position[0] and snake_position[1] == self.food_position[1]):
            self.set_new_food_coordinates()
            self.board.add_score_point()
        self.board.draw_rectangle(self.food_position, self.FD_COLOR)