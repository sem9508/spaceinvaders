import math
import time
import pygame
from constants import *

class Bunker:
    def __init__(self, game_manager, x, y, width, height):
        self.game_manager = game_manager
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect_width = 10
        self.rect_height = 10

        self.grid = []

        for i in range(width//self.rect_width):
            for j in range(height//self.rect_height):
                self.grid.append(pygame.Rect(self.x + self.rect_width*i, self.y + self.rect_height*j, self.rect_width, self.rect_height))


    def draw(self):
        for pixel in self.grid:
            pygame.draw.rect(self.game_manager.screen, GREEN, pixel)

    def update(self):
        self.check_bullet_collision()







    def check_bullet_collision(self):
        for bullet in self.game_manager.enemyBullets:
            for pixel in self.grid:
                if pixel.collidepoint(bullet.x, bullet.y):
                    self.grid.pop(self.grid.index(pixel))
                    self.game_manager.enemyBullets.pop(self.game_manager.enemyBullets.index(bullet))

        for bullet in self.game_manager.bullets:
            for pixel in self.grid:
                if pixel.collidepoint(bullet.x, bullet.y):
                    self.grid.pop(self.grid.index(pixel))
                    self.game_manager.bullets.pop(self.game_manager.bullets.index(bullet))
