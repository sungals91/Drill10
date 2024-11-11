from pico2d import *
import random

import game_framework
from state_machine import *

class Bird:

    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(100, 200), random.randint(400, 500)
        self.frame = 0
        self.face_dir = 1

    def update(self):
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1500 or self.x < 100:
            self.face_dir = self.face_dir * -1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 200, 0, 200, 120,
                                          0 , '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 200, 0, 200, 120,
                                          0, 'h', self.x, self.y, 100, 100)

# Boy Run Speed
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4