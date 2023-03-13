import pygame

from src.global_state import GlobalState
GlobalState.load_main_screen()

from src.components.map import Map

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

m = Map(1)

def main_menu_phase(events):
    pass

def gameplay_phase(events):
    for event in events:
        0
    
    m.update()
    
    m.draw(GlobalState.SCREEN)

def end_menu_phase(events):
    pass