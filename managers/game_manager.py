
class GameManager:
    def __init__(self, screen):
        self.collision_objects = []
        self.objects = []
        self.screen = screen
        self.bullets = []
        self.enemy_bullets = []
        self.enemies = []



    def add_collision_object(self, obj):
        self.collision_objects.append(obj)

    def add_game_object(self, obj):
        self.objects.append(obj)

    def enemie_collisions(self):
        for bullet in self.bullets:
            for enemie in self.enemies:
                if enemie.rect.collidepoint((bullet.x, bullet.y)):
                    print('e')
                    self.enemies.pop(self.enemies.index(enemie))
                    self.bullets.pop(self.bullets.index(bullet))