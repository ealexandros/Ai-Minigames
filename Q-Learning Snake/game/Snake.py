from game.Board import BoardSingleton
import env

class Snake:
    def __init__(self):
        self.board = BoardSingleton.getInstance()

        self.snake = []
        self.previous_tail_state = [-1, -1]
        self.snake_head = [env.MAP_SIZE//2, env.MAP_SIZE//2]

        self.snake_lenght = 1

    def map_computer_action(self, action):
        if(action == 0):
            return [-env.DOT_SIZE, 0]
        elif(action == 1):
            return [env.DOT_SIZE, 0]
        elif(action == 2):
            return [0, -env.DOT_SIZE]
        elif(action == 3):
            return [0, env.DOT_SIZE]

    def snake_invalid_move(self):
        if(self.snake_head[0] >= env.MAP_SIZE or self.snake_head[0] < 0 or self.snake_head[1] >= env.MAP_SIZE or self.snake_head[1] < 0):
            return True

        if(self.snake_lenght == 2 and self.previous_tail_state == self.snake_head):
            return True

        for x in self.snake[:-1]:
            if(x == self.snake_head):
                return True
        return False

    def action(self, action):
        x, y = self.map_computer_action(action)
        self.snake_head[0] += x
        self.snake_head[1] += y

        new_head = [self.snake_head[0], self.snake_head[1]]
        self.snake.append(new_head)
        if(len(self.snake) > self.snake_lenght):
            self.previous_tail_state = self.snake[0]
            del self.snake[0]

    def snake_draw_frame(self):
        self.board.draw_snake(self.snake)

    def get_snake_head(self):
        return self.snake_head.copy()