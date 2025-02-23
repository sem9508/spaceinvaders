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
        self.frequency = FREQUENCY
        self.timer = 0


    def draw(self):
        self.game_manager.screen.blit(self.img, (self.rect.x, self.rect.y))

    def animation_with_frames(self):
        if self.timer <= self.fps / 8:
            self.img = pygame.image.load(self.image[0]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        elif self.timer > self.fps / 8 and self.timer <= self.fps / 4:
            self.img = pygame.image.load(self.image[1]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        elif self.timer > self.fps / 4 and self.timer <= self.fps * (3 / 8):
            self.img = pygame.image.load(self.image[2]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        elif self.timer > self.fps * (3 / 8) and self.timer <= self.fps / 2:
            self.img = pygame.image.load(self.image[3]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1
        
        elif self.timer > self.fps / 2 and self.timer <= self.fps * (5 / 8):
            self.img = pygame.image.load(self.image[4]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        elif self.timer > self.fps * (5 / 8) and self.timer <= self.fps * (6 / 8):
            self.img = pygame.image.load(self.image[5]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        elif self.timer > self.fps * (6 / 8) and self.timer <= self.timer * (7 / 8):
            self.img = pygame.image.load(self.image[6]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        elif self.timer > self.fps * (7 / 8) and self.timer <= self.fps:
            self.img = pygame.image.load(self.image[7]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
            self.timer += 1

        else:
            self.timer = 0

    def animation_without_frames(self):
        self.rect.y += math.sin(2 * int(math.pi) * self.frequency * self.timer)
    
        #  x(t) = A * sin(2 * pi * frequecy * time + phi0)
        #  phi0 is the beginning fase

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