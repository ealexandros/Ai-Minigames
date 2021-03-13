import pygame
import env

class EventListener:
    def __init__(self):
        self.exit = False
        self.x = 0
        self.y = env.DOT_SIZE

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x = -env.DOT_SIZE
                    self.y = 0
                elif event.key == pygame.K_RIGHT:
                    self.x = env.DOT_SIZE
                    self.y = 0
                elif event.key == pygame.K_UP:
                    self.y = -env.DOT_SIZE
                    self.x = 0
                elif event.key == pygame.K_DOWN:
                    self.y = env.DOT_SIZE
                    self.x = 0

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value

    def setExit(self, value):
        self.exit = value