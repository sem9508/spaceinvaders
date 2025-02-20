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

        self.rect_width = 2
        self.rect_height = 2

        self.grid = [[1 for _ in range(20)] for _ in range(20)]

    def draw(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(self.game_manager.screen, RED, pygame.Rect(row*self.rect_width+self.x, col*self.rect_height+self.y, self.rect_width, self.rect_height))

    def destroy(self, x, y):
        '''
        row, col = 
        self.grid[]'''