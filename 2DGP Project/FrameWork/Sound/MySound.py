from pico2d import *

Sound_BGM_Stage1 = None
Sound_BGM_Stage1_Boss = None

Sound_Bullet_Pong = None # se_tan00.wav
Sound_Bullet_Ching = None # se_tan01.wav
Sound_Bullet_Kira = None    # se_kira00.wav

Sound_Select_OK = None  # se_ok00.wav
Sound_Select_Select = None # se_select00.wav
Sound_Select_Cancle = None # se_cancle00.wav
Sound_Select_Pause = None # se_pause.wav

Sound_Effect_Player_Shot = None  # se_plst00.wav
Sound_Effect_EnemyDelete = None # se_enep00.wav
Sound_Effect_PlayerDead = None # se_pldead00.wav
Sound_Effect_Timeout = None # se_timeout.wav

if Sound_BGM_Stage1 == None:

    Sound_BGM_Stage1 = load_music("voyage_1969.mp3")
if Sound_BGM_Stage1_Boss == None:
    Sound_BGM_Stage1_Boss = load_music("se_tan00.wav")

if Sound_Bullet_Pong == None:
    Sound_Bullet_Pong = load_wav("se_tan00.wav")
if Sound_Bullet_Ching == None:
    Sound_Bullet_Ching = load_wav("se_tan01.wav")
if Sound_Bullet_Kira == None:
    Sound_Bullet_Kira = load_wav("se_kira00.wav")

if Sound_Select_OK == None:
    Sound_Select_OK = load_wav("se_ok00.wav")
if Sound_Select_Select == None:
    Sound_Select_Select = load_wav("se_select00.wav")
if Sound_Select_Cancle == None:
    Sound_Select_Cancle = load_wav("se_cancle00.wav")
if Sound_Select_Pause == None:
    Sound_Select_Pause = load_wav("se_pause.wav")

if Sound_Effect_Player_Shot == None:
    Sound_Effect_Player_Shot = load_wav("se_plst00.wav")
if Sound_Effect_EnemyDelete == None:
    Sound_Effect_EnemyDelete = load_wav("se_enep00.wav")
if Sound_Effect_PlayerDead == None:
    Sound_Effect_PlayerDead = load_wav("se_pldead00.wav")
if Sound_Effect_Timeout == None:
    Sound_Effect_Timeout = load_wav("se_timeout.wav")