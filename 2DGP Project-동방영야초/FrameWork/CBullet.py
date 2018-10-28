from pico2d import *
from FrameWork.CObject import cObject
ZACO1, ZACO2, PLAYER1  = range(3)
# left, bottom, width, height

bullet_image_table = { ZACO1 : (33, 174, 25, 25),
                        ZACO2  :(33, 174, 25, 25),
                       PLAYER1 : (35,167,40,12)
                     }


name = "class_Bullet"

class cBullet:
    enemyBullet_image = None
    PlayerBullet_image1 = None
    PlayerBullet_image2 = None
    def __init__(self,x,y, _Bullet_type,Bullet_image):

        self.ObjectInfo = cObject()

        if cBullet.enemyBullet_image == None:
            cBullet.enemyBullet_image = load_image("Enemies & Special Projectiles.png")
        if cBullet.PlayerBullet_image1 == None:
            cBullet.PlayerBullet_image1 = load_image("Projectiles and Items.png")
        if(cBullet.PlayerBullet_image2 == None):
            cBullet.PlayerBullet_image2 = load_image("Players.png")

        if(_Bullet_type == "P"):
            self.ObjectInfo.image = cBullet.PlayerBullet_image1
        elif _Bullet_type == "P2":
            self.ObjectInfo.image = cBullet.PlayerBullet_image2
        else:
            self.ObjectInfo.image = cBullet.enemyBullet_image1

        self.ObjectInfo.x = x
        self.ObjectInfo.y = y

        self.ObjectInfo.image_width = bullet_image_table[Bullet_image][2]
        self.ObjectInfo.image_height = bullet_image_table[Bullet_image][3]

        self.ObjectInfo.width = bullet_image_table[Bullet_image][2]
        self.ObjectInfo.height = bullet_image_table[Bullet_image][3]

        self.ObjectInfo.image_left = bullet_image_table[Bullet_image][0]
        self.ObjectInfo.image_bottom = self.ObjectInfo.image.h - bullet_image_table[Bullet_image][1]
        self.ObjectInfo.frame_offset = 0

        self.ObjectInfo.velocity[1] = 1.0
    def update(self):
        self.ObjectInfo.y += self.ObjectInfo.velocity[1]
        pass

    def draw(self):
        self.ObjectInfo.draw()