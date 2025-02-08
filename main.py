import pygame
from CONSTANTS import *
from screens.game import Game
from screens.menu import Menu
import os

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True
active_screen = 0

while run:
    if active_screen == 0:
        window_instance = Menu(screen)
        active_screen = window_instance.loop()

    if active_screen == 1:
        window_instance = Game(screen)
        active_screen = window_instance.loop()