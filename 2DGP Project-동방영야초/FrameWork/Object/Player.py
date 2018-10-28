from pico2d import *

class Player:
    Player_image = None
    def __init__(self):
        #self.ObjectInfo = Object
        if Player.Player_image == None:
            self.image = load_image("Players.png")

    def draw(self):
        pass

