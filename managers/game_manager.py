
class GameManager:
    def __init__(self):
        self.collision_objects = []
        self.objects = []

    def add_collision_object(self, obj):
        self.collision_objects.append(obj)

    def add_game_object(self, obj):
        self.objects.append(obj)