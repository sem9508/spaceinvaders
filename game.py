import pygame
from CONSTANTS import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.run = True

    def loop(self):
        while self.run:
            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()