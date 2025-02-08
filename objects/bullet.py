import pygame
from CONSTANTS import *

class bullet:
    def __init__(self, color, radius, x, width, y, height):
        self.color = color
        self.radius = radius
        self.center = (x + width/2, y + height/2)

    def draw(self, screen):
        pass
    
    def update(self):
        pass
