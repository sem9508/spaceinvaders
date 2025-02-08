import pygame
from ship import Ship

# inherits from Ship
# that way all the enemies and the player share the basic ship class but can have different properties

class PlayerShip(Ship):
    def __init__(self):
        super.__init__() # the init for the basic ship class (super is the Ship)
