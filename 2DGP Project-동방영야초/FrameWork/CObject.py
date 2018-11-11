name = "class_Object"
from FrameWork import MainFrameWork
from FrameWork.Calculator import *

import math
PIXEL_PER_METER = 42 / 1.5 # 42Pixel = 1.5Meter

class cObject:
    def __init__(self, x = None, y = None):
        self.x, self.y = 0, 0
        if (None != x): self.x = x
        if (None != y): self.y = y

        self.velocity = [0,0]
        self.radius = 0.0

        self.frame = 0
        self.max_frame = 0

        self.image = None
        self.image_left = 0
        self.image_bottom = 0

        self.image_width = 0
        self.image_height = 0
        self.width = 0
        self.height = 0

        self.flip = False
        self.rot = 0

        self.objectType = "Rect"
    def draw(self):
        if self.image != None:
            if self.flip == True:
                self.image.clip_composite_draw(self.image_left + self.image_width * int(self.frame), self.image_bottom,
                                 self.image_width, self.image_height,
                                 math.radians(self.rot + 180), 'v',
                                 self.x, self.y,
                                 self.image_width,self.image_height)
            else:
                self.image.clip_composite_draw(self.image_left + self.image_width * int(self.frame), self.image_bottom,
                                               self.image_width, self.image_height,
                                               math.radians(self.rot), 'n',
                                               self.x, self.y,
                                               self.image_width, self.image_height)

            #left, bottom, width, height, rad, flip, x, y
        pass
    def move(self):
        self.x += get_PPS(self.velocity[0]) * MainFrameWork.frame_time
        self.y += get_PPS(self.velocity[1]) * MainFrameWork.frame_time

    def get_bb(self):
        left = self.x - self.width / 2
        right = self.x + self.width / 2
        bottom = self.y - self.height / 2
        top = self.y + self.height / 2

        return
    def handle_event(self,event):
        pass
    def update(self):
        self.move()
        pass
