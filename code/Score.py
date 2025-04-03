import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_BLUE, SCORE_POS, MENU_OPTION, C_WHITE, C_YELLOW, C_GRAY, C_RED
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save_score(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size=48, text='YOU WIN!!!', text_color=C_BLUE, text_center_pos=SCORE_POS['Title'])
            text = 'Enter your name(MAX: 8 characters): '
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter team name(MAX: 8 characters): '
            self.score_text(text_size=22, text=text, text_color=C_GRAY, text_center_pos=SCORE_POS['EnterName'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 8:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 8:
                            name += event.unicode
            self.score_text(text_size=30, text=name, text_color=C_WHITE, text_center_pos=SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show_score(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(text_size=50, text='TOP 10 SCORE', text_color=C_YELLOW, text_center_pos=SCORE_POS['Title'])
        SCORE_POS['Label'] = (288, 90)
        self.score_text(text_size=24, text='NAME        SCORE       DATE      ', text_color=C_RED,
                        text_center_pos=SCORE_POS['Label'])

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()
        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(text_size=18, text=f'{name}        {score:05d}        {date}', text_color=C_WHITE,
                            text_center_pos=SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"