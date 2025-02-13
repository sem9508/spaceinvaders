import pygame
import sys
from constants import *
from objects.player_ship import PlayerShip
from managers.input_manager import *
from managers.game_manager import GameManager

class Game:
    def __init__(self, screen):
        self.game_manager = GameManager()

        self.screen = screen
        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        self.player = PlayerShip(SCREEN_WIDTH/2-SHIP_WIDTH/2, SCREEN_HEIGHT - 20 - SHIP_HEIGHT/2, 32, 32, RED, 'assets\images\player_ship.png', 1)
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
            use_input(keys, self.game_manager.objects)
                
            # Update
            # Draw
            self.screen.fill(BLACK)

            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)
        return self.next_screen