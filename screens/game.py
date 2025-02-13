import pygame
import sys
from constants import *
from objects.player_ship import PlayerShip

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        self.player = PlayerShip(SCREEN_WIDTH/2-32/2, SCREEN_HEIGHT - 10 - 32, 32, 32, RED, 'assets\images\player_ship.png')
        pygame.display.set_caption('space invaders')

    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return -1
                
            # Update
            # Draw
            self.screen.fill(BLACK)

            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)
        return self.next_screen