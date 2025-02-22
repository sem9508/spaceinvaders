import pygame
from constants import *
import math

class Ship:
    def __init__(self, game_manager, x, y, width, height, img):
        self.rect = pygame.Rect(x, y, width, height)
        self.game_manager = game_manager
        self.image = img
        self.img = pygame.image.load(self.image[0]).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
        self.fps = FPS
        self.speed = 2
        self.timer_animations = 0


    def draw(self):
        self.game_manager.screen.blit(self.img, (self.rect.x, self.rect.y))

    def animation_with_frames(self):
        if self.timer_animations <= self.fps / 8:
            self.img = pygame.image.load(self.image[0]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer_animations += 1

        elif self.timer_animations > self.fps / 8 and self.timer_animations <= self.fps / 4:
            self.img = pygame.image.load(self.image[1]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer_animations += 1

        elif self.timer_animations > self.fps / 4 and self.timer_animations <= self.fps * (3 / 8):
            self.img = pygame.image.load(self.image[2]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer_animations += 1

        elif self.timer_animations > self.fps * (3 / 8) and self.timer_animations <= self.fps / 2:
            self.img = pygame.image.load(self.image[3]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer_animations += 1

        elif self.timer_animations > self.fps / 2:
            self.timer_animations = 0

    def animation_without_frames(self):
        pass

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
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > self.game_manager.screen.get_height() - self.rect.height:
            self.rect.y = self.game_manager.screen.get_height() - self.rect.height