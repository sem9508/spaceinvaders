import pygame
from objects.ship import Ship
class Upgrade(Ship):
    def __init__(self, game_manager, x, y, width, height, img, velocity_x, velocity_y):
        super().__init__(game_manager, x, y, width, height, img)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self):
        direction = [0, 0]
        direction[0] += self.velocity_x
        direction[1] += self.velocity_y

        if self.rect.y >= self.game_manager.screen.get_height() - self.rect.height:
            self.game_manager.upgrades.pop(0)

        self.move(direction[0], direction[1])