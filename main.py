import pygame
from constants import *
from screens.game import Game
from screens.menu import Menu
from screens.options import Options
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
run = True
active_screen = 0

while run:
    if active_screen == 0:
        window_instance = Menu(screen)
        active_screen = window_instance.loop()

    elif active_screen == 1:
        window_instance = Game(screen)
        active_screen = window_instance.loop()

    elif active_screen == 2:
        window_instance = Options(screen)
        active_screen = window_instance.loop()

    else: # window closure. when window is closed in a loop of a screen it should return -1 which triggers this else. for example look at menu.py
        pygame.quit()
        sys.exit()   