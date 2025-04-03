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
                for i in range(6):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', position))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level3Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level3Bg{i}', position))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level4Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level4Bg{i}', position))
                    list_bg.append(Background(f'Level4Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level5Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level5Bg{i}', position))
                    list_bg.append(Background(f'Level5Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level6Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level6Bg{i}', position))
                    list_bg.append(Background(f'Level6Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (20, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (20, WIN_HEIGHT / 2 + 30))

            case 'Enemy0' | 'Enemy1' | 'Enemy2' | 'Enemy3':
                return Enemy(entity_name, (WIN_WIDTH + 20, random.randint(30, WIN_HEIGHT - 30)))
