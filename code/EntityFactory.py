import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'Level2Bg{i}', position))
                return list_bg
            case 'Player1':
                return Player('Player1', (40, WIN_HEIGHT / 2))
            case 'Enemy0' | 'Enemy1' | 'Enemy2' | 'Enemy3':
                return Enemy(entity_name, (WIN_WIDTH - 300, random.randint(0, WIN_HEIGHT)))