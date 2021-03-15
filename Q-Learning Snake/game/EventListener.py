import pygame
import env

class EventListener:
    def __init__(self):
        self.exit = False

    def listener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def setExit(self, value):
        self.exit = value