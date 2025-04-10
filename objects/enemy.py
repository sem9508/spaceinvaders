from time import sleep
import pygame
import random
from objects.ship import Ship
from objects.bullet import *
from constants import *

directionEnemy = [0, 0]
x = 600
y = 0
q = 0
secure_random = random.SystemRandom
class Enemy(Ship):
    def __init__(self, game_manager, x, y, width, height, img, animation_manager):
        super().__init__(game_manager, x, y, width, height, img)
        self.image_index = 0
        self.timer = 0
        self.game_manager = game_manager
        self.animation_manager = animation_manager
        self.max_frames = len(img)-1

        self.enemy = True
        self.direction = 'RIGHT'
        self.speed = 1

    def draw(self):
        self.game_manager.screen.blit(self.img, (self.rect.x, self.rect.y))

    def shootEnemy(self):
        
        new_bullet = Bullet(self.game_manager,RED, 2, self.rect.x, self.rect.y+35, 0, 1)
        self.game_manager.enemyBullets.append(new_bullet)


  

    def spawnEnemy(self):
        
        new_enemy = Enemy(self.game_manager,RED, 2, SHIP_WIDTH, 0 + SHIP_HEIGHT, 0, 1)
        self.game_manager.enemy.append(new_enemy)


    def update(self): 
        
        global x
        global y
        global q
        if x == 800:
            y = random.randrange(600)
            x = 0
            q += 1

        if x == y:
            self.shootEnemy()
        
        x += 1



    



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


    
        



        

        


        



            
        
      
            