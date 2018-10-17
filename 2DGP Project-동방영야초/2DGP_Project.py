import pico2d

from FrameWork import MainFrameWork
from FrameWork.State import State_Logo

State_Current = State_Logo

def Run():
    pico2d.open_canvas( )
    MainFrameWork.run(State_Current)
    pico2d.close_canvas()

if __name__ == '__main__':
    Run()