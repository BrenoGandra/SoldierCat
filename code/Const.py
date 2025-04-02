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
    'Player1': 4,
    'Player2': 4,
    'Player1Shot': 5,
    'Player2Shot': 5,
    'Enemy0': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy0Shot': 3,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
    'Enemy3Shot': 3,
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

}
ENTITY_SHOT_DELAY = {
    'Enemy0': 60,
    'Enemy1': 60,
    'Enemy2': 60,
    'Enemy3': 60,
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
    'Enemy0Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1,
    'Level1Bg0': 9999,
    'Level1Bg1': 9999,
    'Level1Bg2': 9999,
    'Level1Bg3': 9999,
    'Level1Bg4': 9999,
    'Level1Bg5': 9999,
    'Level2Bg0': 9999,
    'Level2Bg1': 9999,
    'Level2Bg2': 9999,
    'Level2Bg3': 9999,
    'Level2Bg4': 9999,
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
    'Enemy0Shot': 40,
    'Enemy1Shot': 40,
    'Enemy2Shot': 40,
    'Enemy3Shot': 40,
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
}

ENTITY_SCORE = {
    'Player1': 0,
    'Player1Shot': 0,
    'Player2':0,
    'Player2Shot': 0,
    'Enemy0': 150,
    'Enemy1': 200,
    'Enemy2': 300,
    'Enemy3': 250,
    'Enemy0Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy3Shot': 0,
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
SPAWN_TIME = 5000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 40000

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


