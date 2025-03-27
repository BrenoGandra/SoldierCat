# C
import pygame

C_GREEN = (140, 200, 20)
C_WHITE = (252, 252, 252)
C_YELLOW = (220, 225, 5)
C_BLUE = (10, 30, 210)

# E
ENTITY_SPEED = {
    'Player1': 1,
    'Player1Shot': 5,
    'Enemy0': 0.5,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 0.5,
    'Enemy0Shot': 4,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
    'Enemy3Shot': 4,
    'Level2Bg0': 0,
    'Level1Bg0': 0

}
ENTITY_SHOT_DELAY = {
    'Enemy0': 0.5,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 0.,
    'Player1': 2,
    'Enemy0Shot': 14,
    'Enemy1Shot': 13,
    'Enemy2Shot': 13,
    'Enemy3Shot': 14,
    'Level1Bg0': 0,
    'Level2Bg0': 0
}

ENTITY_HEALTH = {
    'Player1': 1000,
    'Player1Shot': 1,
    'Enemy0': 200,
    'Enemy1': 400,
    'Enemy2': 300,
    'Enemy3': 200,
    'Enemy0Shot': 4,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
    'Enemy3Shot': 4,
    'Level1Bg0': 0,
    'Level2Bg0': 0
}

ENTITY_DAMAGE = {
    'Player1': 1,
    'Player1Shot': 1,
    'Enemy0': 2,
    'Enemy1': 4,
    'Enemy2': 3,
    'Enemy3': 2,
    'Enemy0Shot': 4,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
    'Enemy3Shot': 4,
    'Level1Bg0': 0,
    'Level2Bg0': 0
}

ENTITY_SCORE = {
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy0': 200,
    'Enemy1': 400,
    'Enemy2': 300,
    'Enemy3': 200,
    'Enemy0Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy3Shot': 0,
    'Level1Bg0': 0,
    'Level2Bg0': 0
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2


# M
MENU_OPTION = (
    'NEW GAME ',
    'SCORE',
    'EXIT'
)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1':pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_RIGHT}
PLAYER_KEY_SHOT = {'Player1':pygame.K_RCTRL}


# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000

# W
WIN_WIDTH = 1280
WIN_HEIGHT = 720

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 90),
    'EnterName': (WIN_WIDTH / 2, 70),
    'Name': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 150),
    0: (WIN_WIDTH / 2, 200),
    1: (WIN_WIDTH / 2, 240),
    2: (WIN_WIDTH / 2, 280),
    3: (WIN_WIDTH / 2, 320),
    4: (WIN_WIDTH / 2, 360),
    5: (WIN_WIDTH / 2, 400),
    6: (WIN_WIDTH / 2, 440),
    7: (WIN_WIDTH / 2, 480),
    8: (WIN_WIDTH / 2, 520),
    9: (WIN_WIDTH / 2, 560),

}
