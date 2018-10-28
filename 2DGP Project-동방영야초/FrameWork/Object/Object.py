from pico2d import *

class Object:
    def __init__(self):
        self.x,self.y = 0,0
        self.width,self.height = 0
        self.image = None
        self.image_left = 0
        self.image_bottom = 0

    def draw(self):
        if self.image != None:
            self.image.clip_draw(self.image_left, self.image_bottom,self.width ,self.height)
        pass

    def update(self):
        pass

    pass