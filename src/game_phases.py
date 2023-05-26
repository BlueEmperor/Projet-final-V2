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
from src.components.items.potions import Potion

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

player = Player()
inventory_ui = InventoryUI(player)
stat_ui = StatUI(player)
m = Map(player)
minimap = MiniMap(m)
hover = Hover(m)
animation = []

for i in range(1):
    a=Sword(*Sword.LIST[0])
    a.damage = 1000
    a.range=[1,4]
    player.add_in_inventory(a, inventory_ui)
    b=Wand(*Wand.LIST[0])
    b.damage = 700000
    player.add_in_inventory(b, inventory_ui)
    player.add_in_inventory(Potion(*Potion.HEALTH_POTION[0]), inventory_ui)

def main_menu_phase(events):
    pass

def gameplay_phase(events):
    global animation

    GlobalState.SCREEN.fill((37,19,26)) # type: ignore
    if(len(animation) == 0):
        for event in events:
            #Mouses events
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    m.left_click_down_event(animation)
                    inventory_ui.left_click_down_event(m)

                elif(event.button == 3):
                    inventory_ui.right_click_down_event()

            elif(event.type == pygame.MOUSEBUTTONUP):
                if(event.button == 1):
                    inventory_ui.left_click_up_event(m)

                elif(event.button == 3):
                    inventory_ui.right_click_up_event()
            
            #keyboard events
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_e):
                    inventory_ui.e_down_event()
                
                elif(event.key == pygame.K_m):
                    minimap.m_down_event()
                
                elif(event.key == pygame.K_f):
                    m.f_down_event(inventory_ui)

            elif(event.type == pygame.KEYUP):
                pass
    
    if(not(minimap.open)):
        m.update(animation)
        inventory_ui.update()
        hover.update(animation)
        m.draw(GlobalState.SCREEN)
        player.draw(GlobalState.SCREEN)

        #ANIMATION /!\ NE PAS TOUCHER OU CA EXPLOSE /!\
        anim(animation)

        # ------------------------------------------
        hover.draw(GlobalState.SCREEN)
        GlobalState.SCREEN.blit(Map.DARK_EFFECT, (0,0))
        stat_ui.draw(GlobalState.SCREEN)
        inventory_ui.draw(GlobalState.SCREEN)
    
    minimap.draw(GlobalState.SCREEN)
    
def end_menu_phase(events):
    pass

def anim(animation):
    if(len(animation) != 0 and animation[0].update(m, player)):
        animation.pop(0)

    if(len(animation) != 0):
        animation[0].draw(GlobalState.SCREEN)