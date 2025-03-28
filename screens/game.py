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

        self.background = pygame.image.load('assets/images/background space invaders.png').convert_alpha()

        self.animation_manager.add_player_ship_frames('assets/images/player_ship_1.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_2.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_3.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_4.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_1.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_2.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_3.png')
        self.animation_manager.add_player_ship_frames('assets/images/player_ship_4.png')
        self.animation_manager.load_player_ship_frames()

        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_1.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_1.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_1.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_2.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_2.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_1.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_1.png')
        self.animation_manager.add_enemy_1_frames('assets/images/enemy_1_1.png')
        self.animation_manager.load_enemy_1_frames()

        self.animation_manager.add_reloading_frames('assets/images/reloading_1.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_2.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_3.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_4.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_5.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_6.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_7.png')
        self.animation_manager.add_reloading_frames('assets/images/reloading_8.png')
        self.animation_manager.load_reloading_frames()
        self.bunkers = [
            Bunker(self.game_manager, 50, self.screen.get_height()-200, 100, 50),
            Bunker(self.game_manager, 200, self.screen.get_height()-200, 100, 50),
            Bunker(self.game_manager, 350, self.screen.get_height()-200, 100, 50),
            Bunker(self.game_manager, 500, self.screen.get_height()-200, 100, 50),

        ]

        self.fps = FPS
        self.run = True
        self.animation_without_frames = ANIMATION_WITHOUT_FRAMES
        self.next_screen = None
        self.reloading_index = 0
        self.reloading_timer = 0
        self.reloading_max_frames = len(self.animation_manager.reloading_frames) - 1
        self.clock = pygame.time.Clock()
        self.player = PlayerShip(self.game_manager, SCREEN_WIDTH/2 - SHIP_WIDTH/2, SCREEN_HEIGHT - 20 - SHIP_HEIGHT/2, 32, 32, self.animation_manager.player_ship_frames)
        pygame.display.set_caption('space invaders')

        self.game_manager.add_game_object(self.player)
        self.game_manager.add_collision_object(self.player)

        self.game_manager.enemies = [
            Enemy(self.game_manager, 25, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 50, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 75, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 100, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 125, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 150, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 175, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 200, 50, 32, 32, self.animation_manager.enemy_1_frames),
            Enemy(self.game_manager, 225, 50, 32, 32, self.animation_manager.enemy_1_frames),
          
        ]


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
                




            self.player.update(keys)
            for bullet in self.game_manager.bullets:
                bullet.update()

            for enemy in self.game_manager.enemies:
                enemy.update()

            self.game_manager.enemie_collisions()
            self.game_manager.delete_bullet()

            for bunker in self.bunkers:
                bunker.update()

            
            # Animation
            self.player.img, self.player.image_index, self.player.timer = self.animation_manager.animation_with_frames(self.player.image_index, self.animation_manager.player_ship_frames, self.player.max_frames, self.player.timer)            
            for enemy in self.game_manager.enemies:
                enemy.img, enemy.image_index, enemy.timer = self.animation_manager.animation_with_frames(enemy.image_index, self.animation_manager.enemy_1_frames, enemy.max_frames, enemy.timer)
            if self.player.reloading:
                self.reloading_img, self.reloading_index, self.reloading_timer = self.animation_manager.animation_with_frames(self.reloading_index, self.animation_manager.reloading_frames, self.reloading_max_frames, self.reloading_timer)

            if self.animation_without_frames:
                for obj in self.game_manager.objects:
                    if hasattr(obj, 'player_ship'):
                        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                            self.animation_manager.animation_without_frames(obj)
                    else:   
                        self.animation_manager.animation_without_frames(obj)
            

            # Draw
            self.screen.blit(self.background, (0, 0))
            for obj in self.game_manager.objects:
                obj.draw()
            for bunker in self.bunkers:
                bunker.draw()
            for bullet in self.game_manager.bullets:
                bullet.draw()
            for enemy in self.game_manager.enemies:
                enemy.draw()


            if self.player.reloading:
                self.game_manager.screen.blit(self.reloading_img, (self.player.rect.x, self.player.rect.y - 32 - 10))

            # Window/Time Update
            pygame.display.flip()
            self.clock.tick(self.fps)

        return self.next_screen