# C
import pygame

C_GREEN = (140, 200, 20)
C_WHITE = (252, 252, 252)
C_YELLOW = (220, 225, 5)
C_BLUE = (10, 30, 210)

# E
ENTITY_SPEED = {
    'Player1': 1,
    'Enemy0': 0.5,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 0.5

}
ENTITY_HEALTH = {
    'Player1': 1000,
    'Enemy0': 200,
    'Enemy1': 400,
    'Enemy2': 300,
    'Enemy3': 200

}

EVENT_ENEMY = pygame.USEREVENT + 1


# M
MENU_OPTION = (
    'NEW GAME ',
    'SCORE',
    'EXIT'
)

# W
WIN_WIDTH = 1280
WIN_HEIGHT = 720


