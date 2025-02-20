import pygame
from constants import *

class Bullet:
    def __init__(self, game_manager, color, radius, x, y, dir_x, dir_y):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y

        self.speed = 5
        self.game_manager = game_manager

        self.direction = [dir_x, dir_y]

    def draw(self):
        pygame.draw.circle(self.game_manager.screen, self.color, (self.x, self.y), self.radius)
    
    def update(self):
        self.x += self.direction[0]*self.speed
        self.y += self.direction[1]*self.speed
