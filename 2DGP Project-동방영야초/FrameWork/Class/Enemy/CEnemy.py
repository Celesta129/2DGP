from FrameWork import MainFrameWork
from FrameWork import CObject
from FrameWork import Calculator
from FrameWork import CBullet
from pico2d import *

name = "class_CEnemy"
#FRAMES_PER_ACTION
#ACTION_PER_TIME
#game_framework.frame_time) % 8
class Zaco1:

    left = 0
    bottom = 0
    width = 26
    height = 28
    image_width = 30
    image_height = 30
    def __init__(self,x,y):
        self.ObjectInfo = CObject.cObject
        self.ObjectInfo.x,self.ObjectInfo.y = x,y
        self.ObjectInfo.width,self.ObjectInfo.height = Zaco1.width, Zaco1.height
        self.ObjectInfo.image_width, self.ObjectInfo.image_height = Zaco1.image_width, Zaco1.image_height
        self.ObjectInfo.frame_offset = Zaco1.image_width

        self.bullet = None
        pass
    def update(self):
        pass

    def draw(self):
        self.ObjectInfo.draw()
        pass
    pass