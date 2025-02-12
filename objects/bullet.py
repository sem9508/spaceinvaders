import pygame
from constants import *

class Bullet:
    def __init__(self, color, radius, x, width, y, height):
        self.color = color
        self.radius = radius
        self.center = (x + width/2, y + height/2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radiuss)
    
    def update(self):
        pass
