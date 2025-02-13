import pygame
from objects.ship import Ship
from objects.bullet import Bullet
from constants import *

# inherits from Ship
# that way all the enemies and the player share the basic ship class but can have different properties

class PlayerShip(Ship):
    def __init__(self, game_manager, x, y, width, height, img):
        super().__init__(game_manager, x, y, width, height, img) # the init for the basic ship class (super is the Ship)
        self.max_ammo = 5
        self.ammo = self.max_ammo

        self.reload_clock = 0
        self.reload_duration = 3*FPS

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

        if self.ammo <= 0:
            self.reload_clock += 1
            if self.reload_clock >= self.reload_duration:
                self.ammo = self.max_ammo
                self.reload_clock = 0


    def shoot(self):
        if self.ammo <= 0:
            return
        
        self.ammo -= 1
        new_bullet = Bullet(self.game_manager, WHITE, 2, self.rect.x + self.rect.width/2, self.rect.y, 0, -1)
        self.game_manager.bullets.append(new_bullet)

# adding an update function here overrrides the update function of Ship so keep that in mind