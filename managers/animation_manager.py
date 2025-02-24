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
        self.fps = FPS
        self.frequency = FREQUENCY

    def add_player_ship_frames(self, frame):
        self.player_ship_frames.append(frame)

    def add_enemy_1_frames(self, frame):
        self.enemy_1_frames.append(frame)

    def add_enemy_2_frames(self, frame):
        self.enemy_2_frames.append(frame)

    def add_enemy_3_frames(self, frame):
        self.enemy_3_frames.append(frame)

    def add_enemy_4_frames(self, frame):
        self.enemy_4_frames.append(frame)

    def add_boss_enemy_frames(self, frame):
        self.boss_enemy_frames.append(frame)

    def add_reloading_frames(self, frame):
        self.reloading_frames.append(frame)
    
    def animation_with_frames(self, frames):
        if self.animation_timer <= self.fps / 8:
            self.img = pygame.image.load(frames[0]).convert_alpha()
            self.animation_timer += 1

        elif self.animation_timer > self.fps / 8 and self.animation_timer <= self.fps / 4:
            self.img = pygame.image.load(frames[1]).convert_alpha()
            self.animation_timer += 1

        elif self.animation_timer > self.fps / 4 and self.animation_timer <= self.fps * (3 / 8):
            self.img = pygame.image.load(frames[2]).convert_alpha()
            self.animation_timer += 1

        elif self.animation_timer > self.fps * (3 / 8) and self.animation_timer <= self.fps / 2:
            self.img = pygame.image.load(frames[3]).convert_alpha()
            self.animation_timer += 1
        
        elif self.animation_timer > self.fps / 2 and self.animation_timer <= self.fps * (5 / 8):
            self.img = pygame.image.load(frames[4]).convert_alpha()
            self.animation_timer += 1

        elif self.animation_timer > self.fps * (5 / 8) and self.animation_timer <= self.fps * (6 / 8):
            self.img = pygame.image.load(frames[5]).convert_alpha()
            self.animation_timer += 1

        elif self.animation_timer > self.fps * (6 / 8) and self.animation_timer <= self.fps * (7 / 8):
            self.img = pygame.image.load(frames[6]).convert_alpha()
            self.animation_timer += 1

        elif self.animation_timer > self.fps * (7 / 8) and self.animation_timer <= self.fps:
            self.img = pygame.image.load(frames[7]).convert_alpha()
            self.animation_timer += 1

        else:
            self.animation_timer = 0

        return self.img

    def animation_without_frames(self, obj):
        obj.rect.y += math.sin(2 * int(math.pi) * self.frequency * self.animation_timer)
    
        #  x(t) = A * sin(2 * pi * frequecy * time + phi0)
        #  phi0 is the beginning fase
