from pico2d import *
from FrameWork.CObject import cObject
from FrameWork import MainFrameWork
from FrameWork import Game_World
from FrameWork.Calculator import *

BLACK, RED1, RED2, PURPLE1, PURPLE2, BLUE1, BLUE2, CYAN1, CYAN2, GREEN1, GREEN2, GREEN3, YELLOW1,YELLOW2, YELLOW3,WHITE = range(16)
bullet_color_table = [BLACK, RED1, RED2, PURPLE1, PURPLE2, BLUE1, BLUE2, CYAN1, CYAN2, GREEN1, GREEN2, GREEN3, YELLOW1, YELLOW2, YELLOW3, WHITE]

ZACO1, ZACO2, PLAYER1  = range(3)
# left, bottom, image_width, image_height, width, height

bullet_image_table = { ZACO1 : (33, 174, 25, 25, 12,14),
                        ZACO2  :(33, 174, 25, 25, 12,14),
                       PLAYER1 : (35,167,40,12, 38,12)
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

        self.ObjectInfo.width = bullet_image_table[Bullet_image][4]
        self.ObjectInfo.height = bullet_image_table[Bullet_image][5]

        self.ObjectInfo.image_left = bullet_image_table[Bullet_image][0]
        self.ObjectInfo.image_bottom = self.ObjectInfo.image.h - bullet_image_table[Bullet_image][1]


        self.ObjectInfo.velocity[1] = 1.0

        self.ObjectInfo.objectType = "Rect"
        self.dmg = 1
    def update(self):
        self.ObjectInfo.x += self.ObjectInfo.velocity[0] * MainFrameWork.frame_time
        self.ObjectInfo.y += self.ObjectInfo.velocity[1] * MainFrameWork.frame_time





    def draw(self):
        self.ObjectInfo.draw()