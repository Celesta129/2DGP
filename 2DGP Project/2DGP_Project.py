import pico2d

from FrameWork import MainFrameWork
from FrameWork.State import State_Logo
from FrameWork.State import State_Lobby
from FrameWork.State import State_Stage
from FrameWork.State import State_End

State_Current = State_Lobby


def Run():
    pico2d.open_canvas( )
    MainFrameWork.run(State_Lobby)
    pico2d.close_canvas()

if __name__ == '__main__':
    Run()