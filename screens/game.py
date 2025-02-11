import pygame
import sys
from CONSTANTS import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.fps = FPS
        self.run = True
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('space invaders')

    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()

            # Draw
            self.screen.fill(BLACK)

            pygame.display.flip()
            self.clock.tick(self.fps)