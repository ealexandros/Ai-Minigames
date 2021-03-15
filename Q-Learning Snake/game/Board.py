import pygame
import env

class BoardSingleton:
    __instance = None

    @staticmethod 
    def getInstance():
        if(BoardSingleton.__instance == None):
            BoardSingleton.__instance = BoardSingleton()
        return BoardSingleton.__instance

    def __init__(self):
        self.COLOR = {
            "BG": (0, 0, 0),
            "SN": (255, 0, 0),
            "SN_HD": (0, 0, 255),
            "FD": (0, 255, 0),
            "TXT": (255, 255, 255)
        }

        self.high_score = 0
        self.score = 0

        self.font = pygame.font.SysFont("bahnschrift", 14)
        self.render_board = pygame.display.set_mode((env.MAP_SIZE, env.MAP_SIZE))

    def restart(self):
        self.render_board.fill(self.COLOR["BG"])
        self.zero_scote_point()
        self.update_score()

    def refresh_board(self):
        self.render_board.fill(self.COLOR["BG"])
        self.update_score()

    def update_score(self):
        value = self.font.render(f"Score: {self.score}", True, self.COLOR["TXT"])
        self.render_board.blit(value, [0, 0])

        value = self.font.render(f"High Score: {self.high_score}", True, self.COLOR["TXT"])
        self.render_board.blit(value, [60, 0])

    def draw_rectangle(self, position):
        pygame.draw.rect(self.render_board, self.COLOR["FD"], [position[0], position[1], env.DOT_SIZE, env.DOT_SIZE])

    def draw_snake(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.render_board, self.COLOR["SN"], [x[0], x[1], env.DOT_SIZE, env.DOT_SIZE])

    def add_score_point(self):
        self.score = self.score + 1
        if(self.high_score < self.score):
            self.high_score = self.score

    def zero_scote_point(self):
        self.score = 0

        