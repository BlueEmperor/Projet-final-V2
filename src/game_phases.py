import pygame

from src.global_state import GlobalState
GlobalState.load_main_screen()
from src.components.map import Map
from src.components.entities.player import Player
from src.components.UI.inventory import Inventory

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

player = Player()
inventory = Inventory(player)
player.inventory = inventory
m = Map(player)

def main_menu_phase(events):
    pass

def gameplay_phase(events):
    for event in events:
        if(event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                inventory.left_click_event(event.type == pygame.MOUSEBUTTONDOWN)
            elif(event.button == 3):
                inventory.right_click_event(event.type == pygame.MOUSEBUTTONDOWN)
    
    m.update()
    
    m.draw(GlobalState.SCREEN)
    player.draw(GlobalState.SCREEN)
    inventory.draw(GlobalState.SCREEN)

def end_menu_phase(events):
    pass