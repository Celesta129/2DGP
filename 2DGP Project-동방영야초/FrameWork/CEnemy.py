from pico2d import *
from FrameWork import MainFrameWork
from FrameWork import CObject

name = "class_CEnemy"
#FRAMES_PER_ACTION
#ACTION_PER_TIME
#game_framework.frame_time) % 8


class Zaco1:
    enemy_image = None
    left = 10
    bottom = 38
    width = 32
    height = 32
    image_width = 32
    image_height = 32
    max_frame = 4


    def __init__(self,x = None,y = None):
        if Zaco1.enemy_image == None:
            Zaco1.enemy_image = load_image("Enemies & Special Projectiles.png")

        self.ObjectInfo = CObject.cObject()

        self.ObjectInfo.image = Zaco1.enemy_image
        self.ObjectInfo.x,self.ObjectInfo.y = 0,0
        if (None != x): self.ObjectInfo.x = x
        if (None != y): self.ObjectInfo.y = y

        self.ObjectInfo.image_left, self.ObjectInfo.image_bottom = Zaco1.left, Zaco1.enemy_image.h - Zaco1.bottom
        self.ObjectInfo.width,self.ObjectInfo.height = Zaco1.width, Zaco1.height
        self.ObjectInfo.image_width, self.ObjectInfo.image_height = Zaco1.image_width, Zaco1.image_height

        self.ObjectInfo.frame = 0
        self.ObjectInfo.max_frame = Zaco1.max_frame
        self.bullet = None
        pass

    def update(self):
        MAX_FRAME =  self.ObjectInfo.max_frame
        TIME_PER_ACTION = 0.5
        ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

        self.ObjectInfo.frame = (self.ObjectInfo.frame + MAX_FRAME * ACTION_PER_TIME * MainFrameWork.frame_time) % MAX_FRAME
        pass

    def draw(self):
        self.ObjectInfo.draw()
        pass
    pass

class bullet1:
    def draw(self):
        pass

    pass