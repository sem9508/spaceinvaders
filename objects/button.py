import pygame
from constants import *

class Button:
    def __init__(self, x, y, width, height, path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, mouse):
        if self.rect.collidepoint(mouse[0], mouse[1]):
            return True
        else:
            return False