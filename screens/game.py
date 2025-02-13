import pygame
import sys
from constants import *
from objects.player_ship import PlayerShip
from managers.game_manager import GameManager

class Game:
    def __init__(self, screen):
        self.screen = screen

        self.game_manager = GameManager(self.screen)

        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        self.player = PlayerShip(self.game_manager, SCREEN_WIDTH/2-SHIP_WIDTH/2, SCREEN_HEIGHT - 20 - SHIP_HEIGHT/2, 32, 32, 'assets\images\player_ship.png')
        pygame.display.set_caption('space invaders')

        self.game_manager.add_collision_object(self.player)

        self.game_manager.add_game_object(self.player)


    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return -1
                
            keys = pygame.key.get_pressed()
                
            # Update
            self.player.update(keys)

            # Draw
            self.screen.fill(BLACK)

            self.player.draw()

            pygame.display.flip()
            self.clock.tick(self.fps)
        return self.next_screen