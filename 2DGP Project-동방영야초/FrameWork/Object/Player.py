from pico2d import *
import FrameWork.Object.Object

class Player:
    Player_image = None
    def __init__(self):
        self.ObjectInfo = Object()
        if Player_image == None:
            self.image = load_image("")
        self.x,self.y = 0
        self.attacked = 0

