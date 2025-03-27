import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, C_GREEN, WIN_HEIGHT, EVENT_ENEMY, C_BLUE, EVENT_TIMEOUT, SPAWN_TIME, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntitymMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.entity_List: list[Entity] = []
        self.game_mode = game_mode
        self.entity_List.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player_score = player_score[0]
        self.entity_List.append(player)
        print(f"Entidades no início do Level: {[ent.name for ent in self.entity_List]}")
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            for ent in self.entity_List:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_List.append(shot)
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player - Health: {ent.health} | Score: {ent.score}', text_color=C_BLUE,
                                    text_pos=(200, WIN_HEIGHT - 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy0', 'Enemy3', 'Enemy1', 'Enemy2'))
                    enemy = EntityFactory.get_entity(choice)
                    if enemy:  # Verifica se enemy não é None
                        self.entity_List.append(enemy)
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_List:
                            if isinstance(ent, Player)and ent.name == 'Player':
                                player_score[0] = ent.score

                        return True

                found_player = False
                for ent in self.entity_List:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            for ent in self.entity_List:
                self.window.blit(source=ent.surf, dest=ent.rect)

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=C_WHITE, text_pos=(150, 20))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color= C_WHITE, text_pos=(150, WIN_HEIGHT - 40))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_List)}', text_color= C_WHITE, text_pos=(150, WIN_HEIGHT - 20))
            pygame.display.flip()
            # collisions
            EntityMediator.verify_collision(entity_list=self.entity_List)
            EntityMediator.verify_health(entity_list=self.entity_List)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
