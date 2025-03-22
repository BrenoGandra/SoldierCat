import random

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, C_GREEN, WIN_HEIGHT, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntitymMediator import EntityMediator


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.entity_List: list[Entity] = []
        self.game_mode = game_mode
        self.entity_List.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_List.append(EntityFactory.get_entity('Player1'))
        self.timeout = 30000
        pygame.time.set_timer(EVENT_ENEMY, millis= 1800)

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))
            print(f"Entidades ativas: {[ent.name for ent in self.entity_List]}")
            for ent in self.entity_List:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy0', 'Enemy3', 'Enemy1', 'Enemy2'))
                    enemy = EntityFactory.get_entity(choice)
                    if enemy:  # Verifica se enemy não é None
                        self.entity_List.append(enemy)
            for ent in self.entity_List:
                self.window.blit(source=ent.surf, dest=ent.rect)

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=C_WHITE, text_pos=(150, 20))
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
