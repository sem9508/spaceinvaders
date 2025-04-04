import random

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
<<<<<<< HEAD
                if enemy.rect.collidepoint((bullet.x, bullet.y)):
                    self.enemies.pop(self.enemies.index(enemy))
                    self.bullets.pop(self.bullets.index(bullet))
    def player_collisions(self):
        for bullet in self.enemyBullets:
            if self.player.rect.collidepoint((bullet.x, bullet.y)):
                self.player.pop()
=======
                if enemy.rect.collidepoint((bullet.x, bullet.y)): 
                    self.enemies.pop(self.enemies.index(enemy))
                    self.bullets.pop(self.bullets.index(bullet))
                    if random.random() < 0.25:
                        return enemy.rect.x, enemy.rect.y, True
        return None, None, False
    
    def player_schip_collision_upgrade(self, player_ship):
        for upgrade in self.upgrades:
            if player_ship.rect.collidepoint((upgrade.rect.x, upgrade.rect.y)):
                self.upgrades.pop(self.upgrades.index(upgrade))
                player_ship.max_ammo += 1
        
        

    def player_ship_collision_enemie(self, player_ship, lifes_lost):
        for enemy in self.enemies:
            if enemy.rect.colliderect(player_ship.rect):

                lifes_lost -= 1
                self.enemies.pop(self.enemies.index(enemy))

        return lifes_lost

    def delete_bullet(self):
        for bullet in self.bullets:
            if bullet.y < 0:
                print('succes')
>>>>>>> 49af8651a2b3984dbc7fe98f32c6ddfa2feb8fa0
                self.bullets.pop(self.bullets.index(bullet))