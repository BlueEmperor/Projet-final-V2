import pygame

from src.global_state import GlobalState
from src.components.map import Map

vec = pygame.math.Vector2

GlobalState.load_main_screen()
pygame.mouse.set_visible(False)


def main_menu_phase(events):
    pass

def gameplay_phase(events):
    for event in events:
        0


def end_menu_phase(events):
    pass