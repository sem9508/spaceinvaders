
class GameManager:
    def __init__(self, screen):
        self.collision_objects = []
        self.objects = []
        self.screen = screen
        self.bullets = []
        self.enemyBullets = []
        self.enemies = []



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
    def player_collisions(self):
        for bullet in self.enemyBullets:
            if self.player.rect.collidepoint((bullet.x, bullet.y)):
                self.player.pop()
                self.bullets.pop(self.bullets.index(bullet))