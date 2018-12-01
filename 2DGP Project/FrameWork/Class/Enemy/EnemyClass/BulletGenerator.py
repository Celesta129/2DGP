from pico2d import *
from FrameWork.CObject import *
class BulletGenerator(Object):
    image = None
    def __init__(self, x, y, target):
        if BulletGenerator.image == None:
            BulletGenerator.image = load_image("Enemies & Special Projectiles")
        super.__init__(x,y)
        self.image_left, self.image_bottom = 14,195
        self.image_width, self.image_height = 60,60
        self.width = self.image_width
        self.height = self.image_height

        self.target = target
        self.rotPos = 0 # degree
        self.dist = 0
    def update(self):

        self.move()
        pass


    pass