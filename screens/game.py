import pygame
import sys
from constants import *
from objects.player_ship import *
from objects.enemy import *
from managers.game_manager import GameManager
from managers.animation_manager import AnimationManager
from objects.bunker import Bunker

class Game:
    def __init__(self, screen):
        self.screen = screen

        self.game_manager = GameManager(self.screen)
        self.animation_manager = AnimationManager()

        self.animation_manager.add_player_ship_frames('assets/images/player_ship_1.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_2.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_3.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_4.png')

        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1.png')



        self.bunkers = [
            Bunker(self.game_manager, 50, self.screen.get_height()-200, 100, 50),
            Bunker(self.game_manager, 200, self.screen.get_height()-200, 100, 50),
            Bunker(self.game_manager, 350, self.screen.get_height()-200, 100, 50),
            Bunker(self.game_manager, 500, self.screen.get_height()-200, 100, 50),


        ]

        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        self.player = PlayerShip(self.game_manager, SCREEN_WIDTH/2 - SHIP_WIDTH/2, SCREEN_HEIGHT - 20 - SHIP_HEIGHT/2, 32, 32, self.animation_manager.player_ship_frames)
        self.enemy = Enemy(self.game_manager, SCREEN_WIDTH/2-SHIP_WIDTH/2, SCREEN_HEIGHT - 20 - SHIP_HEIGHT/2, 32, 32, self.animation_manager.enemy_1_frames)
        pygame.display.set_caption('space invaders')

        self.game_manager.add_collision_object(self.player)
        self.game_manager.add_game_object(self.player)
        self.game_manager.add_game_object(self.enemy)
        self.game_manager.add_collision_object(self.enemy)


    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return -1
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

                    if event.key == pygame.K_r:
                        self.player.reload()
                
            keys = pygame.key.get_pressed()
                
            # Update
            self.player.update(keys)
            for bullet in self.game_manager.bullets:
                bullet.update()

            for bunker in self.bunkers:
                bunker.update()

            # Animation
            self.player.animation()

            # Draw
            self.screen.fill(BLACK)
            self.enemy.draw()
            self.player.draw()
            for bunker in self.bunkers:
                bunker.draw()
            for bullet in self.game_manager.bullets:
                bullet.draw()

            # Window/Time Update
            pygame.display.flip()
            self.clock.tick(self.fps)
            self.timer_animations =+ 1

        return self.next_screen