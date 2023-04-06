import pygame

from src.global_state import GlobalState
GlobalState.load_main_screen()
from src.components.map.map import Map
from src.components.entities.player import Player
from src.components.UI.inventory import InventoryUI
from src.components.UI.stats import StatUI
from src.components.UI.minimap import MiniMap
from src.components.UI.hover import Hover
from src.components.items.sword import Sword
from src.components.items.wand import Wand

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

player = Player()
inventory_ui = InventoryUI(player)
stat_ui = StatUI(player)
m = Map(player)
minimap = MiniMap(m)
hover = Hover(m)

for i in range(10):
    a=Sword()
    a.damage = 5
    player.add_in_inventory(a, inventory_ui)
    b=Wand()
    b.damage = 7
    player.add_in_inventory(b, inventory_ui)
    
def main_menu_phase(events):
    pass

def gameplay_phase(events):
    GlobalState.SCREEN.fill((37,19,26)) # type: ignore
    for event in events:
        #Mouses events
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                m.left_click_down_event()
                inventory_ui.left_click_down_event()

            elif(event.button == 3):
                inventory_ui.right_click_down_event()

        elif(event.type == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                inventory_ui.left_click_up_event(m)

            elif(event.button == 3):
                inventory_ui.right_click_up_event()
        
        #keyboard events
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_e):
                inventory_ui.e_down_event()
            elif(event.key == pygame.K_m):
                minimap.m_down_event()
        elif(event.type == pygame.KEYUP):
            pass
    
    if(not(minimap.open)):
        m.update()
        inventory_ui.update()
        hover.update()

        m.draw(GlobalState.SCREEN)
        player.draw(GlobalState.SCREEN)
        hover.draw(GlobalState.SCREEN)
        GlobalState.SCREEN.blit(Map.DARK_EFFECT, (0,0))
        stat_ui.draw(GlobalState.SCREEN)
        inventory_ui.draw(GlobalState.SCREEN)

    minimap.draw(GlobalState.SCREEN)
    
def end_menu_phase(events):
    pass