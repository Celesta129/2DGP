from FrameWork import Game_World
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Blue import Zaco_Blue
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Red import Zaco_Red
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Yellow import Zaco_Yellow

from FrameWork.Class.Enemy.MovePattern.MovePattern import *
from FrameWork.Class.Enemy.ShotPattern.ShotPattern import *
import json
from FrameWork.Game_World import *
name = "Enemy_Generator"

def read_file(stage_number):

    filename = None
    if stage_number == 0:
        filename = "Test.json"
    elif stage_number == 1:
        filename = "Stage_02.json"
    else:
        return
    with open(filename, "r") as f:
        final_object_info = json.load(f)

    return final_object_info


# First "|" = Time
# second "|" = Type of enemy
# Third "|" = posX
# fourth "|" = posY

ENEMYTYPE, POSX, POSY,MP,SP = range(5)

enemy_table = {"ZACO_BLUE" : Zaco_Blue,
               "ZACO_RED" : Zaco_Red,
               "ZACO_YELLOW" : Zaco_Yellow
               }

MP_table = {"MP_GO_STRAIGHT" : MP_go_straight,
            "MP_GO_RIGHT" : MP_go_right,
            "MP_GO_LEFT" : MP_go_left }

SP_table = {"SP_AIMING_BLUEWEDGE": SP_Aiming_BlueWedge,
            "SP_360_BUM_SMALLRICE": SP_360_bum_smallrice,
            "SP_BACK_BLUECIRCLE" : SP_back_blueCircle
            }

def load_dic_by_json(file):
    array = json.load(file)
    return array

def read_array_to_float(array, output_array):
    value = float(array)
    output_array.append(value)


 # 최종 정보를 이용해 Enemy 생성
def make_Enemy(info_array, cur_stage_timeacc):
    if len(info_array) == 0 :
        return
    if info_array[0]["Time"] > cur_stage_timeacc :
        return

    Enemy_type = info_array[0]["Type"]

    x,y = info_array[0]["x"], info_array[0]["y"]
    MP,SP = info_array[0]["MP"], info_array[0]["SP"]

    MP = MP_table[MP]
    SP = SP_table[SP]

    Enemy = enemy_table[Enemy_type](x,y,MP,SP)

    Game_World.add_object(Enemy,Game_World.layer_enemy)
    info_array.pop(0)
    pass
#{"Time": ,  "Type": "", "x": ,  "y": ,  "MP": "", "SP": "" }