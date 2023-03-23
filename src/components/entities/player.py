import pygame

from src.components.entities.entity import Entity
from path import ASSETS_DIR
from src.config import Config

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self):
        self.image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + ".png")).convert_alpha() for i in range(4)]
        self.big_image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + "_inv.png")).convert_alpha() for i in range(4)]
        super().__init__("player", vec(4,4), 20, self.image_list)
        self.rect.center=vec(Config.WIDTH/2, Config.HEIGHT/2)
        self.hotbar = [None for i in range(9)]
        self.inventory = [[None for i in range(9)] for j in range(4)]
        self.gold = 0
    
    def add_in_inventory(self, item, inventory_ui):
        slots=self.empty_slots()
        
        if(len(slots[0])>0):
            self.hotbar[int(slots[0][0][0])]=item
            item.slot = slots[0][0]
            item.in_hotbar = True
            item.add(inventory_ui.hotbar_sprite_group)

        elif(len(slots[1])>0):
            self.inventory[int(slots[1][0][1])][int(slots[1][0][0])]=item
            item.slot = slots[1][0]
            item.add(inventory_ui.inventory_sprite_group)
        
        else:
            return(False)
        
        item.update(inventory_ui.inventory_rect.topleft, inventory_ui.hotbar_rect.topleft)
        return(True)

    def empty_slots(self):
        L=[[],[]]
        for i in range(len(self.hotbar)):
            if(not(self.hotbar[i])):
                L[0].append((vec(i,0)))

        for i in range(len(self.inventory)):
            for j in range(len(self.inventory[i])):
                if(not(self.inventory[i][j])):
                    L[1].append(vec(j,i))

        return(L)