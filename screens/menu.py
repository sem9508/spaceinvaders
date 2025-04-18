import pygame
from constants import *
from objects.button import *

class Menu:
    def __init__(self, screen, set_current_frame):
        self.set_current_frame = set_current_frame

        self.screen = screen
        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('space invaders menu')
        
        self.play_btn = Button(SCREEN_WIDTH/2-300/2, SCREEN_HEIGHT/2-100/2, 300, 100,'assets/images/start.png') # deze is 300 bij 100
        self.options_btn = Button(self.screen.get_width() -64/2 -40, 15, 64, 64,'assets/images/options.png') # deze is 64 bij 64


    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return -1 # handle window closure in main.py

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_btn.update(pygame.mouse.get_pos()):
                        self.run = False
                        self.next_screen = 1

                    elif self.options_btn.update(pygame.mouse.get_pos()):
                        self.run = False
                        self.next_screen = 2

            # update
                        
            # draw
            self.screen.fill(BLACK)
            self.play_btn.draw(self.screen)
            self.options_btn.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)
            self.set_current_frame(self.screen)
        return self.next_screen
