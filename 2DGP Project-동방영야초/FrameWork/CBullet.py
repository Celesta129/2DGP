from pico2d import *
from FrameWork.CObject import cObject
from FrameWork import MainFrameWork
from FrameWork import Game_World
from FrameWork.Calculator import *

BLACK, RED1, RED2, PURPLE1, PURPLE2, BLUE1, BLUE2, CYAN1, CYAN2, GREEN1, GREEN2, GREEN3, YELLOW1,YELLOW2, YELLOW3,WHITE = range(16)
black, red, purple, blue, cyan, green, yellow, white = range(8)
bullet_color_table = [BLACK, RED1, RED2, PURPLE1, PURPLE2, BLUE1, BLUE2, CYAN1, CYAN2, GREEN1, GREEN2, GREEN3, YELLOW1, YELLOW2, YELLOW3, WHITE]
bullet_color_table2 = [black, red, purple, blue, cyan, green, yellow, white]
ZACO1, ZACO2, PLAYER1  = range(3)
# left, bottom, image_width, image_height, width, height

bullet_image_table = { ZACO1 : (7, 493, 32, 28, 14,28),
                        ZACO2  :(33, 174, 25, 25, 12,14),
                       PLAYER1 : (35,167,40,12, 38,12)
                     }


name = "class_Bullet"

class cBullet(cObject):
    def __init__(self,x,y, Bullet_image, Bullet_image_index):
        super().__init__(x, y)

        self.image = Bullet_image
        self.image_width = bullet_image_table[Bullet_image_index][2]
        self.image_height = bullet_image_table[Bullet_image_index][3]

        self.width = bullet_image_table[Bullet_image_index][4]
        self.height = bullet_image_table[Bullet_image_index][5]

        self.image_left = bullet_image_table[Bullet_image_index][0]
        self.image_bottom = self.image.h - bullet_image_table[Bullet_image_index][1]


        self.velocity[1] = 1.0

        self.objectType = "Rect"
        self.dmg = 1

class pBullet_1(cBullet):
    image = None
    def __init__(self, x, y):
        if(pBullet_1.image == None):
            pBullet_1.image = load_image("Players.png")

        super().__init__(x,y,self.image , PLAYER1)

class eBullet_1(cBullet):
    image = None
    def __init__(self, x, y):
        if(eBullet_1.image == None):
            eBullet_1.image = load_image("Projectiles and Items.png")
        self.image = eBullet_1.image

        super().__init__(x,y,self.image , ZACO1)
        self.frame = bullet_color_table2[blue]

def InitBullet(Bullet, rot_degree,velocity_x,velocity_y):
    # 속도 단위는 km/h, Bullet
    Bullet.rot = rot_degree + 90
    radian = math.radians(rot_degree)
    Bullet.velocity[0] = math.cos(radian) * get_PPS(velocity_x)
    Bullet.velocity[1] = math.sin(radian) * get_PPS(velocity_y)