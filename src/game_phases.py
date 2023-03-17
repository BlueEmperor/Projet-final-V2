import pygame

from src.global_state import GlobalState
GlobalState.load_main_screen()
from src.components.map import Map
from src.components.entities.player import Player
from src.components.UI.inventory import InventoryUI

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

player = Player()
inventory_ui = InventoryUI(player)
m = Map(player)

def main_menu_phase(events):
    pass

def gameplay_phase(events):
    for event in events:
        #Mouses events
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                inventory_ui.left_click_down_event(event.type == pygame.MOUSEBUTTONDOWN)
                continue
            elif(event.button == 3):
                inventory_ui.right_click_down_event(event.type == pygame.MOUSEBUTTONDOWN)
                continue

        elif(event.type == pygame.MOUSEBUTTONUP):
            pass
        
        #keyboard events
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_e):
                inventory_ui.K_e_event(event.type == pygame.KEYDOWN)
                continue

        elif(event.type == pygame.KEYUP):
            pass


    if(not(inventory_ui.isopen)):
        m.update()
    inventory_ui.update()

    m.draw(GlobalState.SCREEN)
    player.draw(GlobalState.SCREEN)
    inventory_ui.draw(GlobalState.SCREEN)

def end_menu_phase(events):
    pass