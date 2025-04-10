import random
from constants import *

class GameManager:
    def __init__(self, screen):
        self.collision_objects = []
        self.objects = []
        self.screen = screen
        self.bullets = []
        self.enemyBullets = []
        self.enemies = []
        self.bunkers = []
        self.upgrades = []



    def add_collision_object(self, obj):
        self.collision_objects.append(obj)

    def add_game_object(self, obj):
        self.objects.append(obj)

    def enemy_collisions(self):
        for bullet in self.bullets:
            for enemy in self.enemies:

                if enemy.rect.collidepoint((bullet.x, bullet.y)):
                    self.enemies.pop(self.enemies.index(enemy))
                    self.bullets.pop(self.bullets.index(bullet))
                    random_variable = random.random()
                    if random_variable < 0.25:
                        return enemy.rect.x, enemy.rect.y, True
        return None, None, False
    
    def player_schip_collisions(self, player_ship, lifes):
        for upgrade in self.upgrades:
            if player_ship.rect.colliderect(upgrade.rect):
                self.upgrades.pop(self.upgrades.index(upgrade))
                if player_ship.double_gun:
                    
                        player_ship.max_ammo += 1
                else:
                    random_variable = random.random()
                    if random_variable < 0.01:
                        player_ship.double_gun = True
                    else:
                        player_ship.max_ammo += 1
        
        for enemy in self.enemies:
            if enemy.rect.colliderect(player_ship.rect):
                lifes -= 1
                self.enemies.pop(self.enemies.index(enemy))
        
        for enemybullet in self.enemyBullets:
            if player_ship.rect.collidepoint((enemybullet.x, enemybullet.y)):
                lifes -= 1
                self.enemyBullets.pop(self.enemyBullets.index(enemybullet))

        return lifes    

    def delete_bullet(self):
        for bullet in self.bullets:
            if bullet.y < 0:
                print('succes')
                self.bullets.pop(self.bullets.index(bullet))

        for enemybullet in self.enemyBullets:
            if enemybullet.y > SCREEN_HEIGHT:
                print('works')
                self.enemyBullets.pop(self.enemyBullets.index(enemybullet))