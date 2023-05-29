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
from src.components.items.rocket_launcher import Rocket_launcher
from src.message_display import MessageDisplay
from src.config import Config
from src.components.items.throw_dagger import ThrowableDager

vec = pygame.math.Vector2

pygame.mouse.set_visible(False)

player = Player()
inventory_ui = InventoryUI(player)
stat_ui = StatUI(player)
m = Map(player)
minimap = MiniMap(m)
hover = Hover(m)
animations = []
messages = []

for i in range(1):
    a=Sword(*Sword.LIST[0])
    a.damage = 1000
    a.range=[1,4]
    player.add_in_inventory(a, inventory_ui)
    b=Wand(*Wand.LIST[0])
    b.damage = 700000
    b.durability = 100000
    player.add_in_inventory(b, inventory_ui)
    
    for j in range(4):
        player.add_in_inventory(Armor(*Armor.CHESTPLATE[j]),inventory_ui)
        player.add_in_inventory(Armor(*Armor.LEGGING[j]),inventory_ui)
        player.add_in_inventory(Armor(*Armor.HELMET[j]),inventory_ui)
        player.add_in_inventory(Armor(*Armor.BOOTS[j]),inventory_ui)
        player.add_in_inventory(Ak(*Ak.LIST[j]), inventory_ui)
        player.add_in_inventory(Sword(*Sword.LIST[j]), inventory_ui)
        player.add_in_inventory(Rocket_launcher(*Rocket_launcher.LIST[j]), inventory_ui)
    for j in range(3):
        player.add_in_inventory(Potion(*Potion.LIST[j][2]), inventory_ui)

    #player.add_in_inventory(Armor(*Armor.WOOD_PLASTRON),inventory_ui)


def main_menu_phase(events):
    pass

def gameplay_phase(events):
    global animations

    GlobalState.SCREEN.fill((37,19,26)) # type: ignore
    if(len(animations) == 0):
        for event in events:
            #Mouses events
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
                    m.left_click_down_event(animations, inventory_ui)
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
        m.update(animations)
        inventory_ui.update()
        hover.update(animations)
        m.draw(GlobalState.SCREEN)
        player.draw(GlobalState.SCREEN, m)

        #ANIMATION /!\ NE PAS TOUCHER OU CA EXPLOSE /!\
        anim(animations)

        # ------------------------------------------
        hover.draw(GlobalState.SCREEN)
        GlobalState.SCREEN.blit(Map.DARK_EFFECT, (0,0))
        stat_ui.draw(GlobalState.SCREEN)
        inventory_ui.draw(GlobalState.SCREEN)

        mess(messages)
    
    minimap.draw(GlobalState.SCREEN)
    
def end_menu_phase(events):
    pass

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
