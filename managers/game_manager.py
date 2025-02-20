
class GameManager:
    def __init__(self, screen):
        self.collision_objects = []
        self.objects = []
        self.screen = screen
        self.bullets = []

    def add_collision_object(self, obj):
        self.collision_objects.append(obj)

    def add_game_object(self, obj):
        self.objects.append(obj)

        