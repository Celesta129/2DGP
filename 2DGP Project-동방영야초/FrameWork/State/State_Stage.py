from pico2d import *
from FrameWork import MainFrameWork
#from FrameWork.Class.CPlayer import CPlayer
class CObject:
    def __init__(self, w = None, h = None):
        self.x,self.y = 0,0
        self.image_width = 0
        self.image_height = 0
        self.width = None
        self.height = None
        self.image = None
        self.image_left = 0
        self.image_bottom = 0
        if(w == None):
            self.Width = self.image_width
        if(h == None):
            self.Height = self.image_height

    def draw(self):
        if self.image != None:
            self.image.clip_draw(self.image_left, self.image_bottom,
                                 self.image_width ,self.image_height,
                                 self.x, self.y,
                                 self.width,self.height)
        pass

    def update(self):
        pass


class CPlayer:
    Player_image = None
    def __init__(self):
        self.ObjectInfo = CObject()
        if CPlayer.Player_image == None:
            self.image = load_image("Players.png")

        self.ObjectInfo.width = 100
        self.ObjectInfo.height = 100
        self.ObjectInfo.image_width = 100
        self.ObjectInfo.image_height = 100

    def draw(self):
        self.ObjectInfo.draw()


name = "State_Stage"

image_Main_BG = None
image_Background = None
Background_Scroll_y = 0

player = None

def enter():
    global image_Main_BG
    global player
    if player == None:
        player = CPlayer()
        CPlayer.x = 400
        CPlayer.y = 300
        pass
    if image_Main_BG == None:
        image_Main_BG = load_image("MainBackGround.png")


def exit():
    global image_Main_BG
    del(image_Main_BG)



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MainFrameWork.quit()
    pass


def update():
    pass


def draw():
    global image_Main_BG
    clear_canvas()

    image_Main_BG.clip_draw(0,0,121,159,400,300,800,600)
    player.draw()
    update_canvas()
    pass