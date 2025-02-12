import pygame
from constants import *
from objects.button import *

class Options:
    def __init__(self, screen):
        self.screen = screen
        self.fps = FPS
        self.run = True
        self.next_screen = None
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('space invaders options')

        self.close_btn = Button(self.screen.get_width() -64/2 -40, 15, 64, 64,'assets/images/close.png')# deze is 64 bij 64



    def loop(self):
        while self.run:

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return -1
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.close_btn.update(pygame.mouse.get_pos()):
                        self.run = False
                        self.next_screen = 0
            
            #draw
            self.screen.fill(BLACK)
            self.close_btn.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)
                
        return self.next_screen
