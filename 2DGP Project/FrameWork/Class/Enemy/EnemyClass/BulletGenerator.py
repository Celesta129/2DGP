from pico2d import *
from FrameWork.CObject import *
from FrameWork import MainFrameWork

class BulletGenerator(Object):
    image = None
    def __init__(self, target):
        if BulletGenerator.image == None:
            BulletGenerator.image = load_image("Bullet_Generator.png")
        super().__init__(0,0)

        self.image = BulletGenerator.image
        self.image_left, self.image_bottom = 0, 0
        self.image_width, self.image_height = 30,30
        self.width = 30
        self.height = 30

        self.target = target
        self.rotPos = 0 # degree
        self.dist = 30


    def update(self):
        radian = math.radians(self.rot)
        self.x = self.target.x + math.cos(radian) * self.dist - math.sin(radian) * self.dist
        self.y = self.target.y + math.sin(radian) * self.dist + math.cos(radian) * self.dist

        self.rot -= 180 * MainFrameWork.frame_time
        #self.move()
        pass


    pass