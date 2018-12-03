from pico2d import *
from FrameWork.CObject import Object
from FrameWork import MainFrameWork
from FrameWork import Game_World
from FrameWork.Calculator import *
#from FrameWork.Sound.MySound import *

BLACK, RED1, RED2, PURPLE1, PURPLE2, BLUE1, BLUE2, CYAN1, CYAN2, GREEN1, GREEN2, GREEN3, YELLOW1,YELLOW2, YELLOW3,WHITE = range(16)
bullet_color_table = [BLACK, RED1, RED2, PURPLE1, PURPLE2, BLUE1, BLUE2, CYAN1, CYAN2, GREEN1, GREEN2, GREEN3, YELLOW1, YELLOW2, YELLOW3, WHITE]

black, red, purple, blue, cyan, green, yellow, white = range(8)
bullet_color_table2 = [black, red, purple, blue, cyan, green, yellow, white]

#bullet_index_name
RICE, WEDGE, SMALL_RICE, CIRCLE, PLAYER1  = range(5)

# left, bottom, image_width, image_height, width, height
bullet_image_table = { RICE : (7, 493, 32, 28, 14,28),
                       WEDGE  :(10, 36, 16, 16, 12,14),
                       SMALL_RICE: (10, 83, 16, 16, 8, 16),
                       CIRCLE:(10, 67, 16, 16, 16, 16),
                       PLAYER1 : (35,167,40,12, 38,12)
                     }


name = "class_Bullet"

class cBullet(Object):
    def __init__(self,x,y, Bullet_image, Bullet_image_index):
        super().__init__(x, y)

        self.rot = 90
        self.image = Bullet_image
        self.image_width = bullet_image_table[Bullet_image_index][2]
        self.image_height = bullet_image_table[Bullet_image_index][3]

        self.width = bullet_image_table[Bullet_image_index][4]
        self.height = bullet_image_table[Bullet_image_index][5]

        self.image_left = bullet_image_table[Bullet_image_index][0]
        self.image_bottom = self.image.h - bullet_image_table[Bullet_image_index][1]

        self.velocity[0] = 0.0
        self.velocity[1] = 1.0

        self.objectType = "Rect"
        self.dmg = 1
    def RotateVelocity(self, degree, vx = None, vy = None):
        radian = math.radians(degree)
        cos = math.cos(radian)
        sin = math.sin(radian)

        vx0 = self.velocity[0]
        vy0 = self.velocity[1]

        self.velocity[0] = vx0 * cos - vy0 * sin
        self.velocity[1] = vx0 * sin + vy0 * cos

        if vx != None and vy != None:
            vx = vx0 * cos - vy0 * sin
            vy = vx0 * sin + vy0 * cos

class pBullet_normal(cBullet):
    image = None
    sound = None

    def __init__(self, x, y):
        if(pBullet_normal.image == None):
            pBullet_normal.image = load_image("Players.png")
        if(pBullet_normal.sound == None):
            pBullet_normal.sound =  load_wav('se_plst00.wav')
            pBullet_normal.sound.set_volume(15)

        super().__init__(x,y,self.image , PLAYER1)
        pBullet_normal.sound.play()

class Bullet_rice(cBullet):
    image = None
    sound = None

    def __init__(self, x, y, bullet_color):
        if(Bullet_rice.image == None):
            Bullet_rice.image = load_image("Projectiles and Items.png")
        if (Bullet_rice.sound == None):
            Bullet_rice.sound = load_wav('se_tan00.wav')
            Bullet_rice.sound.set_volume(10)

        self.image = Bullet_rice.image

        super().__init__(x,y,self.image , RICE)
        self.frame = bullet_color_table2[bullet_color]
        Bullet_rice.sound.play()
class Bullet_Wedge(cBullet):
    image = None
    sound = None
    def __init__(self, x, y, bullet_color):
        if (Bullet_Wedge.image == None):
            Bullet_Wedge.image = load_image("Projectiles and Items.png")
        if (Bullet_Wedge.sound == None):
            Bullet_Wedge.sound = load_wav('se_tan00.wav')
            Bullet_Wedge.sound.set_volume(10)

        self.image = Bullet_Wedge.image

        super().__init__(x, y, self.image, WEDGE)
        self.frame = bullet_color_table[bullet_color]
        Bullet_Wedge.sound.play()

class Bullet_SmallRice(cBullet):
    image = None
    sound = None
    def __init__(self, x, y, bullet_color):
        if(Bullet_SmallRice.image == None):
            Bullet_SmallRice.image = load_image("Projectiles and Items.png")
        if (Bullet_SmallRice.sound == None):
            Bullet_SmallRice.sound = load_wav('se_kira00.wav')
            Bullet_SmallRice.sound.set_volume(15)

        self.image = Bullet_SmallRice.image

        super().__init__(x, y, self.image, SMALL_RICE)
        self.frame = bullet_color_table[bullet_color]
        Bullet_SmallRice.sound.play()


class Bullet_Circle(cBullet):
    image = None
    def __init__(self, x, y, bullet_color):
        if(Bullet_Circle.image == None):
            Bullet_Circle.image = load_image("Projectiles and Items.png")
        self.image = Bullet_Circle.image

        super().__init__(x, y, self.image, CIRCLE)
        self.frame = bullet_color_table[bullet_color]
        self.radius = 8
        self.objectType = "Circle"

def InitBullet(Bullet, rot_degree = 0,velocity_x = 0, velocity_y = -1):
    # 속도 단위는 km/h, Bullet
    Bullet.rot += rot_degree + 180
    radian = math.radians(rot_degree)
    Bullet.velocity[0] = math.cos(radian) * velocity_x
    Bullet.velocity[1] = math.sin(radian) * velocity_y

def rotate_bullet(bulletlist,degree):
    for bullet in bulletlist:
        bullet.rot += degree
        radian = math.radians(degree)
        vx = bullet.velocity[0]
        vy = bullet.velocity[1]
        bullet.velocity[0] = math.cos(radian) * vx - math.sin(radian) * vy
        bullet.velocity[1] = math.sin(radian) * vx + math.cos(radian) * vy
    pass

def InitNWayBullet(bulletlist, vx0, vy0, degree):
    rad_step = math.radians(degree)
    rad = 0

    num = len(bulletlist)

    if num % 2  == 0:
        rad = -num/2 * rad_step
    else:
        rad = (-num/2 + 0.5) * rad_step

    for bullet in bulletlist:
        cos = math.cos(rad)
        sin = math.sin(rad)
        bullet.velocity[0] = vx0 * cos - vy0 * sin
        bullet.velocity[1] = vx0 * sin + vy0 * cos

        bullet.rot = math.degrees(rad)
        rad += rad_step
