from game.Board import BoardSingleton

class Snake:
    def __init__(self):
        self.board = BoardSingleton()

        self.snake = []
        self.snake_head = [self.board.MAP_SIZE/2, self.board.MAP_SIZE/2]
        self.snake_lenght = 1

    def call_draw_snake(self):
        self.board.draw_snake(self.snake)

    def snake_out_of_range(self):
        if self.snake_head[0] >= self.board.MAP_SIZE or self.snake_head[0] < 0 or self.snake_head[1] >= self.board.MAP_SIZE or self.snake_head[1] < 0:
            return True
        return False

    def snake_invalid_move(self, head):
        for x in self.snake[:-1]:
            if(x == head):
                return True
        return False

    def snake_logic(self, x, y):
        if(self.snake_out_of_range()):
            return True
        
        self.snake_head[0] += x
        self.snake_head[1] += y

        new_head = [self.snake_head[0], self.snake_head[1]]
        self.snake.append(new_head)


        if len(self.snake) > self.snake_lenght:
            del self.snake[0]
        self.call_draw_snake()

        if(self.snake_invalid_move(new_head)):
            return True
        return False

    def get_snake_head(self):
        return self.snake_head

        
