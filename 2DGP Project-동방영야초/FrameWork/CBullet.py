from pico2d import *
from FrameWork.CObject import cObject
ZACO1, ZACO2  = range(2)
# left, bottom, width, height

bullet_image_table = { ZACO1 : (0, 0, 50, 50),
                        ZACO2  :(0, 0, 50, 50)
                          }

name = "class_Bullet"

class cBullet:
    enemyBullet_image = None
    PlayerBullet_image = None
    def __init__(self,x,y, _Bullet_type,Bullet_image):

        self.ObjectInfo = cObject()

        if cBullet.enemyBullet_image == None:
            cBullet.enemyBullet_image = load_image("Enemies & Special Projectiles.png")

        if cBullet.PlayerBullet_image == None:
            cBullet.PlayerBullet_image = load_image("Projectiles and Items.png")

        if(_Bullet_type == "P"):
            self.ObjectInfo.image = cBullet.PlayerBullet_image
        else:
            self.ObjectInfo.image = cBullet.enemyBullet_image

        self.ObjectInfo.x = x
        self.ObjectInfo.y = y

        self.ObjectInfo.image_width = bullet_image_table[Bullet_image][2]
        self.ObjectInfo.image_height = bullet_image_table[Bullet_image][3]

        self.ObjectInfo.width = bullet_image_table[Bullet_image][2]
        self.ObjectInfo.height = bullet_image_table[Bullet_image][3]

        self.ObjectInfo.image_left = bullet_image_table[Bullet_image][0]
        self.ObjectInfo.image_bottom = self.ObjectInfo.image.h - bullet_image_table[Bullet_image][1]
        self.ObjectInfo.frame_offset = 0


    def update(self):
        pass

    def draw(self):
        self.ObjectInfo.draw()