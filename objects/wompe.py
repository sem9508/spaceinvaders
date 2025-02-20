import pygame
from objects.ship import Ship
from constants import *

class NotPlayerShip(Ship):
    def __init__(self, game_manager, x, y, width, height, img):
        super().__init__(game_manager, x, y, width, height, img)
    