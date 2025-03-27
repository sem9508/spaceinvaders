import pygame
import math
from constants import *

class AnimationManager():
    def __init__(self):
        self.player_ship_frames = []
        self.enemy_1_frames = []
        self.enemy_2_frames = []
        self.enemy_3_frames = []
        self.enemy_4_frames = []
        self.boss_enemy_frames = []
        self.reloading_frames = []
        self.animation_timer = 0
        self.frame_duration = 8
        self.fps = FPS
        self.frequency = FREQUENCY

    def add_player_ship_frames(self, frame):
        self.player_ship_frames.append(frame)

    def load_player_ship_frames(self):
        self.player_ship_frames = [pygame.image.load(frame).convert_alpha() for frame in self.player_ship_frames]

    def add_enemy_1_frames(self, frame):
        self.enemy_1_frames.append(frame)

    def load_enemy_1_frames(self):
        self.enemy_1_frames = [pygame.image.load(frame).convert_alpha() for frame in self.enemy_1_frames]

    def add_enemy_2_frames(self, frame):
        self.enemy_2_frames.append(frame)

    def load_enemy_2_frames(self):
        self.enemy_2_frames = [pygame.image.load(frame).convert_alpha() for frame in self.enemy_2_frames]

    def add_enemy_3_frames(self, frame):
        self.enemy_3_frames.append(frame)

    def load_enemy_3_frames(self):
        self.enemy_3_frames = [pygame.image.load(frame).convert_alpha() for frame in self.enemy_3_frames]

    def add_enemy_4_frames(self, frame):
        self.enemy_4_frames.append(frame)

    def load_enemy_4_frames(self):
        self.enemy_4_frames = [pygame.image.load(frame).convert_alpha() for frame in self.enemy_4_frames]

    def add_boss_enemy_frames(self, frame):
        self.boss_enemy_frames.append(frame)

    def load_boss_enemy_frames(self):
        self.boss_enemy_frames = [pygame.image.load(frame).convert_alpha() for frame in self.boss_enemy_frames]

    def add_reloading_frames(self, frame):
        self.reloading_frames.append(frame)

    def load_reloading_frames(self):
        self.reloading_frames = [pygame.image.load(frame).convert_alpha() for frame in self.reloading_frames]

    
    def animation_with_frames(self, image_index, image, max_frames, animation_timer):
        
        if animation_timer >= self.frame_duration:
            animation_timer = 0
            image_index+=1
            if image_index > max_frames:
                image_index = 0
            self.img = image[image_index]
            return self.img, image_index, animation_timer

        else:
            animation_timer +=1
            return image[image_index], image_index, animation_timer



    def animation_without_frames(self, obj):
        obj.rect.y += math.sin(2 * int(math.pi) * self.frequency * self.animation_timer)
    
        #  x(t) = A * sin(2 * pi * frequecy * time + phi0)
        #  phi0 is the beginning fase
