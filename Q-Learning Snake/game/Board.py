import pygame

class BoardSingleton:
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.MAP_SIZE = 400
        self.BOARD_SIZE = 20
        self.DOT_SIZE = self.MAP_SIZE/self.BOARD_SIZE
        self.BG_COLOR = (0, 0, 0)
        self.TXT_COLOR = (255, 255, 255)

        self.high_score = 0
        self.score = 0

        self.font = pygame.font.SysFont("bahnschrift", 14)
        self.render_board = pygame.display.set_mode((self.MAP_SIZE, self.MAP_SIZE))

    def refresh_board(self):
        self.render_board.fill(self.BG_COLOR)
        self.set_current_score()

    def set_current_score(self):
        value = self.font.render(f"Score: {self.score}", True, self.TXT_COLOR)
        self.render_board.blit(value, [0, 0])

        self.check_for_high_score()

    def check_for_high_score(self):
        if(self.high_score < self.score):
            self.high_score = self.score
        value = self.font.render(f"High Score: {self.score}", True, self.TXT_COLOR)
        self.render_board.blit(value, [0, 20])

    def draw_rectangle(self, position, COLOR):
        pygame.draw.rect(self.render_board, COLOR, [position[0], position[1], self.DOT_SIZE, self.DOT_SIZE])

    def draw_snake(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.render_board, (255, 0, 0), [x[0], x[1], self.DOT_SIZE, self.DOT_SIZE])

    def add_score_point(self):
        self.score = self.score + 1

    def zero_scote_point(self):
        self.score = 0

        