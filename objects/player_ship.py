import pygame
from objects.ship import Ship

# inherits from Ship
# that way all the enemies and the player share the basic ship class but can have different properties

class PlayerShip(Ship):
    def __init__(self, game_manager, x, y, width, height, img):
        super().__init__(game_manager, x, y, width, height, img) # the init for the basic ship class (super is the Ship)

    def update(self, keys):
        direction = [0, 0]
        if keys[pygame.K_a]:
            direction[0] -= 1
        if keys[pygame.K_d]:
            direction[0] += 1
        if keys[pygame.K_w]:
            direction[1] -= 1
        if keys[pygame.K_s]:
            direction[1] += 1

        self.move(direction[0], direction[1])
# adding an update function here overrrides the update function of Ship so keep that in mind