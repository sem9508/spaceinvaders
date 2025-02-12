import pygame
import sys
from constants import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('space invaders')

    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return -1
            # Draw
            self.screen.fill(BLACK)

            pygame.display.flip()
            self.clock.tick(self.fps)
        return self.next_screen