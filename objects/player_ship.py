import pygame
from objects.ship import Ship

# inherits from Ship
# that way all the enemies and the player share the basic ship class but can have different properties

class PlayerShip(Ship):
    def __init__(self, x, y, width, height, color, img, input_group):
        super().__init__(x, y, width, height, color, img, input_group) # the init for the basic ship class (super is the Ship)

# adding an update function here overrrides the update function of Ship so keep that in mind