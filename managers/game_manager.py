import random

class GameManager:
    def __init__(self, screen):
        self.collision_objects = []
        self.objects = []
        self.screen = screen
        self.bullets = []
        self.enemy_bullets = []
        self.enemies = []
        self.bunkers = []
        self.upgrades = []



    def add_collision_object(self, obj):
        self.collision_objects.append(obj)

    def add_game_object(self, obj):
        self.objects.append(obj)

    def enemie_collisions(self):
        for bullet in self.bullets:
            for enemie in self.enemies:
                if enemie.rect.collidepoint((bullet.x, bullet.y)): 
                    self.enemies.pop(self.enemies.index(enemie))
                    self.bullets.pop(self.bullets.index(bullet))
                    if random.randint(1, 4) == 1:
                        return enemie.rect.x, enemie.rect.y, True
        return None, None, False
    
    def player_schip_collisions(self, player_ship):
        for upgrade in self.upgrades:
            if player_ship.rect.collidepoint((upgrade.rect.x, upgrade.rect.y)):
                self.upgrades.pop(self.upgrades.index(upgrade))
                player_ship.max_ammo += 1

    def delete_bullet(self):
        for bullet in self.bullets:
            if bullet.y < 0:
                print('succes')
                self.bullets.pop(self.bullets.index(bullet))