name = "class_Object"

import math
PIXEL_PER_METER = 42 / 1.5 # 42Pixel = 1.5Meter

class cObject:
    def __init__(self, x = None, y = None):
        self.x,self.y = 0,0
        if(x != None):
            self.x = x
        if(y != None):
            self.y = y

        self.velocity = [0,0]

        self.hp = 0
        self.dmg = 0
        self.radius = 0.0

        self.frame = 0
        self.frame_offset = 0

        self.image = None
        self.image_left = 0
        self.image_bottom = 0

        self.image_width = 0
        self.image_height = 0
        self.width = 0
        self.height = 0

        self.flip = False
        self.rot = 0
    def draw(self):
        if self.image != None:
            if self.flip == True:
                self.image.clip_composite_draw(self.image_left + self.frame_offset * int(self.frame), self.image_bottom,
                                 self.image_width, self.image_height,
                                 math.radians(self.rot + 180), 'v',
                                 self.x, self.y,
                                 self.width,self.height)
            else:
                self.image.clip_composite_draw(self.image_left + self.frame_offset * int(self.frame), self.image_bottom,
                                               self.image_width, self.image_height,
                                               math.radians(self.rot), 'n',
                                               self.x, self.y,
                                               self.width, self.height)

            #left, bottom, width, height, rad, flip, x, y
        pass
    def handle_event(self,event):
        pass
    def update(self):
        pass
