import pygame
from objects.ship import Ship
from constants import *

class Enemy(Ship):
    def __init__(self, game_manager, x, y, width, height, img):
        super().__init__(game_manager, x, y, width, height, img)
        self.image_index = 0
        self.timer = 0

        self.max_frames = len(img)-1

    