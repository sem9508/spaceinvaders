
class AnimationManager():
    def __init__(self):
        self.player_ship_frames = []
        self.enemy_1_frames = []

    def add_player_ship_frames(self, frame):
        self.player_ship_frames.append(frame)

    def add_enemy_1_frames(self, frame):
        self.enemy_1_frames.append(frame)