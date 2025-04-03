import pygame
import random
from objects.ship import Ship
from objects.bullet import *
from constants import *
directionEnemy = [0, 0]
class Enemy(Ship):
    def __init__(self, game_manager, x, y, width, height, img):
        super().__init__(game_manager, x, y, width, height, img)
        self.image_index = 0
        self.timer = 0

        self.max_frames = len(img)-1

    
        self.enemy = True
        self.direction = 'RIGHT'
        self.speed = 5

    def draw(self):
        self.game_manager.screen.blit(self.img, (self.rect.x, self.rect.y))

    def shootEnemy(self):
        
        new_bullet = Bullet(self.game_manager,RED, 2, self.rect.x, self.rect.y+10, 0, -1)
        self.game_manager.bullets.append(new_bullet)

    
    def spawnEnemy(self):
        
        new_enemy = Enemy(self.game_manager,RED, 2, self.rect.x, self.rect.y+10, 0, 1)
        self.game_manager.enemy.append(new_enemy)


    def update(self):
        if self.direction == 'RIGHT':
            self.rect.x += self.speed
        if self.direction == 'LEFT':
            self.rect.x -= self.speed
        if self.rect.x + self.rect.width >= SCREEN_WIDTH:
            self.rect.y += SHIP_HEIGHT
            self.direction = 'LEFT'
        if self.rect.x <= 0:
            self.rect.y += SHIP_HEIGHT
            self.direction = 'RIGHT'

            
        
      
            