import pygame
from CONSTANTS import *
from game import Game

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True
active_screen = 0

while run:
    if active_screen == 0:
        window_instance = Game(screen)
        active_screen = window_instance.loop()