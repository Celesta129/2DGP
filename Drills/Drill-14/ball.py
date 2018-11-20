import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1260-1), random.randint(0, 1109-1)
        #self.x, self.y = 1000,600

    def set_center_object(self,object):
        self.boy = object
        pass
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        x = self.boy.cx
        y = self.boy.cy
        #window_left = clamp()
        self.image.draw(x + self.delta_x, y + self.delta_y)

        #draw_rectangle(*self.get_bb())

    def update(self):
        # self.window_x = self.boy.x - self.x
        # self.window_y = self.boy.y - self.y
        self.delta_x = self.x - self.boy.x
        self.delta_y  = self.y - self.boy.y
        pass


