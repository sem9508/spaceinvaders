import pygame
from constants import *
import math

class Ship:
    def __init__(self, game_manager, x, y, width, height, img):
        self.rect = pygame.Rect(x, y, width, height)
        self.game_manager = game_manager
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.speed = 2

    def draw(self):
        self.game_manager.screen.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
        pass

    def move(self, dir_x, dir_y):
        if not dir_x and not dir_y:
            return
        
        angle = math.atan2(dir_y, dir_x)

        self.rect.x += self.speed*math.cos(angle)
        self.rect.y += self.speed*math.sin(angle)

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > self.game_manager.screen.get_width() - self.rect.width:
            self.rect.x = self.game_manager.screen.get_width() - self.rect.width