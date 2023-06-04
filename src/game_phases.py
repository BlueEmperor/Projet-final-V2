import pygame

from path import ASSETS_DIR
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
from src.components.items.armor import Armor
from src.components.items.ak47 import Ak
from src.components.items.bow import Bow
from src.components.items.rocket_launcher import Rocket_launcher
from src.components.UI.main_menu import MainMenu
from src.components.UI.death_menu import DeathMenu
from src.components.items.throw_dagger import ThrowableDager

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

player = Player()
inventory_ui = InventoryUI(player)
stat_ui = StatUI(player)
m = Map(player)
minimap = MiniMap(m)
hover = Hover(m)
main_menu = MainMenu()
animations = []
messages = []
death_menu = DeathMenu(m, player, animations, messages, inventory_ui, stat_ui, minimap, hover)


player.add_in_inventory(Wand(*Wand.LIST[0]), inventory_ui)
player.add_in_inventory(Sword(*Sword.LIST[0]), inventory_ui)   
player.add_in_inventory(ThrowableDager(*ThrowableDager.LIST[0]), inventory_ui)       
for j in range(4):
    player.add_in_inventory(Armor(*Armor.CHESTPLATE[j]),inventory_ui)
    player.add_in_inventory(Armor(*Armor.LEGGING[j]),inventory_ui)
    player.add_in_inventory(Armor(*Armor.HELMET[j]),inventory_ui)
    player.add_in_inventory(Armor(*Armor.BOOTS[j]),inventory_ui)
    player.add_in_inventory(Bow(*Bow.LIST[j]), inventory_ui)
    player.add_in_inventory(Wand(*Wand.LIST[j]), inventory_ui)
    player.add_in_inventory(Ak(*Ak.LIST[j]), inventory_ui)
    #player.add_in_inventory(Sword(*Sword.LIST[j]), inventory_ui)
    #player.add_in_inventory(Rocket_launcher(*Rocket_launcher.LIST[j]), inventory_ui)
    #player.add_in_inventory(Potion(*Potion.LIST[j][2]), inventory_ui)

    #player.add_in_inventory(Armor(*Armor.WOOD_PLASTRON),inventory_ui)


def main_menu_phase(events):
    main_menu.update(events)
    main_menu.draw(GlobalState.SCREEN)

def gameplay_phase(events):
    global animations

    GlobalState.SCREEN.fill((37,19,26)) # type: ignore
    for event in events:
        if(event.type == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                inventory_ui.left_click_up_event(m)

            elif(event.button == 3):
                inventory_ui.right_click_up_event()

        if(len(animations) == 0):
            #Mouses events
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    m.left_click_down_event(animations, inventory_ui,GlobalState.SCREEN,stat_ui)
                    inventory_ui.left_click_down_event(m)

                elif(event.button == 3):
                    inventory_ui.right_click_down_event()

            
            #keyboard events
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_e):
                    inventory_ui.e_down_event()
                
                elif(event.key == pygame.K_m):
                    minimap.m_down_event()
                
                elif(event.key == pygame.K_f):
                    m.f_down_event(inventory_ui)
                
                elif(event.key == pygame.K_SPACE):
                    player.health = 20000
                    print("cheat activated")

            elif(event.type == pygame.KEYUP):
                pass
    
    if(not(minimap.open)):
        m.update(animations)
        inventory_ui.update()
        stat_ui.update()
        hover.update(animations)
        m.draw(GlobalState.SCREEN)
        player.draw(GlobalState.SCREEN, m)

        # ------------------------------------------
        hover.draw(GlobalState.SCREEN)
        GlobalState.SCREEN.blit(Map.DARK_EFFECT, (0,0)) # type: ignore
        stat_ui.draw(GlobalState.SCREEN)
        inventory_ui.draw(GlobalState.SCREEN)

        mess(messages)
    
    minimap.draw(GlobalState.SCREEN)

    if(not(minimap.open)):
        anim(animations)
    
def end_menu_phase(events):
    death_menu.update(events)
    death_menu.draw(GlobalState.SCREEN)

def anim(animations):
    global messages
    if(len(animations) != 0 and animations[0].update(m, player, messages)):
        animations.pop(0)

    if(len(animations) != 0):
        animations[0].draw(GlobalState.SCREEN)

def mess(messages):
    i = 0
    while(i < len(messages)):
        messages[i].update()
        messages[i].draw(GlobalState.SCREEN)
        if(messages[i].timer == 0):
            messages.pop(i)
            i -= 1
        i += 1
