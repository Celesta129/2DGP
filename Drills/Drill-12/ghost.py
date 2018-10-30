from pico2d import *
import math

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

#각속도 Angular velocity
w = 720 / 2
#meter
Radius = 3

class cGhost:
    image_boy = None
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.velocity_x = 0.0
        self.velocity_y = 0.0

        self.acc_x = 0.0
        self.acc_y = 0.0

        if(None == cGhost.image_boy):
            cGhost.image_boy = load_image('animation_sheet.png')
        pass

    def draw(self):
        cGhost.image_boy.clip_draw(0,0,100,100,self.x,self.y)
        pass

    def cal_velocity(self):
        self.acc_x = -pow(w,2) * self.x
        self.acc_y = -pow(w,2) * self.y

        self.velocity_x += self.acc_x
        self.velocity_y += self.acc_y

    def update(self):
        self.cal_velocity()
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        pass

    pass