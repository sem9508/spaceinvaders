import pygame
from constants import *

class Ship:
    def __init__(self, x, y, width, height, color, img, input_group):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.input_group = input_group
        self.img = pygame.image.load(img).convert_alpha()

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
        pass
