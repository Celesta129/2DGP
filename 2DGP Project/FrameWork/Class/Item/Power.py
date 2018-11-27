from FrameWork.CObject import Object
from pico2d import *

class Power(Object):
    image = None
    image_left,image_bottom,image_width,image_height = 282,82,12,12
    def __init__(self,x,y):
        if Power.image == None:
            Power.image = load_image("Projectiles and Items.png")
        super.__init__(x,y)
        self.image_left = Power.image_left
        self.image_bottom = Power.image_bottom

        self.width = Power.image_width
        self.height = Power.image_height

        self.image_width = Power.image_width
        self.image_height = Power.image_height


        pass


