import pygame
pygame.init()

from sys import exit
from time import time

from src.config import Config
from src.global_state import GlobalState
from src.status import GameStatus
from src.game_phases import main_menu_phase, gameplay_phase, end_menu_phase
from src.draw_cursor import DrawCursor

FramePerSec = pygame.time.Clock()

def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


def main():
    while True:
        fps = time()
        events = pygame.event.get()
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase(events)
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase(events)
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            end_menu_phase(events)

        DrawCursor(GlobalState.SCREEN)
        for event in events:
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
        
        update_game_display()
        GlobalState.SCREEN.fill((0,0,0))
        pygame.display.set_caption(str(int(1/(time()-fps))))


if __name__ == "__main__":
    main()
