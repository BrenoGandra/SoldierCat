# C
import pygame

C_GREEN = (140, 200, 20)
C_WHITE = (252, 252, 252)
C_YELLOW = (220, 225, 5)
C_BLUE = (10, 30, 210)
C_RED = (170, 0, 0)
C_GRAY = (190, 190, 190)
C_PINK = (210, 30, 190)


# E
ENTITY_SPEED = {
    'Player1': 3,
    'Player2': 3,
    'Player1Shot': 5,
    'Player2Shot': 5,
    'Enemy0': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
    'Enemy6': 1,
    'Enemy7': 1,
    'Enemy8': 1,
    'Enemy9': 1,
    'Enemy0Shot': 3,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
    'Enemy3Shot': 3,
    'Enemy4Shot': 5,
    'Enemy5Shot': 5,
    'Enemy6Shot': 4,
    'Enemy7Shot': 3,
    'Enemy8Shot': 5,
    'Enemy9Shot': 4,
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Level4Bg0': 0,
    'Level4Bg1': 1,
    'Level4Bg2': 2,
    'Level4Bg3': 3,
    'Level4Bg4': 4,
    'Level5Bg0': 0,
    'Level5Bg1': 1,
    'Level5Bg2': 2,
    'Level5Bg3': 3,
    'Level5Bg4': 4,
    'Level5Bg5': 5,
    'Level5Bg6': 6,
    'Level6Bg0': 0,
    'Level6Bg1': 1,
    'Level6Bg2': 2,
    'Level6Bg3': 3,


}
ENTITY_SHOT_DELAY = {
    'Enemy0': 60,
    'Enemy1': 60,
    'Enemy2': 60,
    'Enemy3': 60,
    'Enemy4': 60,
    'Enemy5': 60,
    'Enemy6': 60,
    'Enemy7': 60,
    'Enemy8': 60,
    'Enemy9': 60,
    'Player1': 15,
    'Player2': 15

}

ENTITY_HEALTH = {
    'Player1': 1000,
    'Player1Shot': 1,
    'Player2': 1000,
    'Player2Shot': 1,
    'Enemy0': 450,
    'Enemy1': 300,
    'Enemy2': 550,
    'Enemy3': 500,
    'Enemy4': 400,
    'Enemy5': 650,
    'Enemy6': 560,
    'Enemy7': 350,
    'Enemy8': 500,
    'Enemy9': 600,
    'Enemy0Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1,
    'Enemy4Shot': 1,
    'Enemy5Shot': 1,
    'Enemy6Shot': 1,
    'Enemy7Shot': 1,
    'Enemy8Shot': 1,
    'Enemy9Shot': 1,
    'Level1Bg0': 99999,
    'Level1Bg1': 99999,
    'Level1Bg2': 99999,
    'Level1Bg3': 99999,
    'Level1Bg4': 99999,
    'Level1Bg5': 99999,
    'Level2Bg0': 99999,
    'Level2Bg1': 99999,
    'Level2Bg2': 99999,
    'Level2Bg3': 99999,
    'Level2Bg4': 99999,
    'Level3Bg0': 99999,
    'Level3Bg1': 99999,
    'Level3Bg2': 99999,
    'Level3Bg3': 99999,
    'Level4Bg0': 99999,
    'Level4Bg1': 99999,
    'Level4Bg2': 99999,
    'Level4Bg3': 99999,
    'Level4Bg4': 99999,
    'Level5Bg0': 99999,
    'Level5Bg1': 99999,
    'Level5Bg2': 99999,
    'Level5Bg3': 99999,
    'Level5Bg4': 99999,
    'Level5Bg5': 99999,
    'Level5Bg6': 99999,
    'Level6Bg0': 99999,
    'Level6Bg1': 99999,
    'Level6Bg2': 99999,
    'Level6Bg3': 99999,


}

ENTITY_DAMAGE = {
    'Player1': 1,
    'Player1Shot': 60,
    'Player2': 1,
    'Player2Shot': 60,
    'Enemy0': 10,
    'Enemy1': 10,
    'Enemy2': 10,
    'Enemy3': 10,
    'Enemy4': 10,
    'Enemy5': 10,
    'Enemy6': 10,
    'Enemy7': 10,
    'Enemy8': 10,
    'Enemy9': 10,
    'Enemy0Shot': 40,
    'Enemy1Shot': 80,
    'Enemy2Shot': 50,
    'Enemy3Shot': 60,
    'Enemy4Shot': 50,
    'Enemy5Shot': 120,
    'Enemy6Shot': 70,
    'Enemy7Shot': 90,
    'Enemy8Shot': 110,
    'Enemy9Shot': 100,
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Level4Bg4': 0,
    'Level5Bg0': 0,
    'Level5Bg1': 0,
    'Level5Bg2': 0,
    'Level5Bg3': 0,
    'Level5Bg4': 0,
    'Level5Bg5': 0,
    'Level5Bg6': 0,
    'Level6Bg0': 0,
    'Level6Bg1': 0,
    'Level6Bg2': 0,
    'Level6Bg3': 0,


}

ENTITY_SCORE = {
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy0': 50,
    'Enemy1': 80,
    'Enemy2': 140,
    'Enemy3': 90,
    'Enemy4': 100,
    'Enemy5': 250,
    'Enemy6': 150,
    'Enemy7': 100,
    'Enemy8': 200,
    'Enemy9': 180,
    'Enemy0Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy3Shot': 0,
    'Enemy4Shot': 0,
    'Enemy5Shot': 0,
    'Enemy6Shot': 0,
    'Enemy7Shot': 0,
    'Enemy8Shot': 0,
    'Enemy9Shot': 0,
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Level4Bg4': 0,
    'Level5Bg0': 0,
    'Level5Bg1': 0,
    'Level5Bg2': 0,
    'Level5Bg3': 0,
    'Level5Bg4': 0,
    'Level5Bg5': 0,
    'Level5Bg6': 0,
    'Level6Bg0': 0,
    'Level6Bg1': 0,
    'Level6Bg2': 0,
    'Level6Bg3': 0,

}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = (
    'NEW GAME - 1P',
    'NEW GAME - COOP',
    'SCORE',
    'EXIT'
)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}


# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 10000

# W
WIN_WIDTH = 573
WIN_HEIGHT = 324

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Name': (WIN_WIDTH / 2, 90),
    'Label': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}


