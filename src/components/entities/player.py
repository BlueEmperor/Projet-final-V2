import pygame

from src.components.entities.entity import Entity
from path import ASSETS_DIR
from src.config import Config
from src.components.entities.chest import Chest
from src.components.entities.monster import Monster

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self):
        self.image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + ".png")).convert_alpha() for i in range(4)]
        self.big_image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + "_inv.png")).convert_alpha() for i in range(4)]
        super().__init__("player", vec(4,4), self.image_list)
        self.rect.center=vec(Config.WIDTH/2, Config.HEIGHT/2)
        self.hotbar = [None for i in range(9)]
        self.inventory = [[None for i in range(9)] for j in range(4)]
        self.health = 15
        self.max_health = 20
        self.gold = 0
        self.mana = 96
        self.max_mana = 100
        self.level = 1
        self.armor = None
        self.usage = []
        self.durability = []
        self.duration = []
    
    def add_in_inventory(self, item, inventory_ui):
        slots=self.empty_slots()
        
        if(len(slots[0])>0):
            self.hotbar[int(slots[0][0][0])]=item
            item.slot = slots[0][0]
            item.location = "h"
            item.add(inventory_ui.hotbar_group)

        elif(len(slots[1])>0):
            self.inventory[int(slots[1][0][1])][int(slots[1][0][0])]=item
            item.slot = slots[1][0]
            item.location = "i"
            item.add(inventory_ui.inventory_group)
        
        else:
            return(False)
        
        item.update(inventory_ui.inventory_rect.topleft, inventory_ui.hotbar_rect.topleft)
        return(True)

    def empty_slots(self):
        L=[[],[]]#L= ()
        for i in range(len(self.hotbar)):
            if(not(self.hotbar[i])):
                L[0].append((vec(i,0)))

        for i in range(len(self.inventory)):
            for j in range(len(self.inventory[i])):
                if(not(self.inventory[i][j])):
                    L[1].append(vec(j,i))#changer parce que ca pue un peu

        return(L)

    def teleport(self, coord): #mettre if il est riche ,le tp plus loin avec expovariate
        self.map_pos = coord
        self.absolute_pos = coord*48

    def heal(self, number):
        if(self.health + number > self.max_health):
            self.health = self.max_health
        else:
            self.health += number

    def armor_boost(self,number):
        if self.armor.health + number > self.armor.max_health:
            self.armor.health = self.armor.max_health
        else:
            self.armor.health += number

    def damage_boost(self,number,tour):
        return tour
        
        #self.weapon.damage+=number
        #while self.weapon.durability
        #while tour > 0:
            #pass
        #self.weapon.damage-=number

    def poison_attack(self,number,m):
        for i in m.get_item_room(self):
            print(i)
            if isinstance(i,Monster) and i.health!=None:
                if i.health<=number:
                    i.kill
                elif i.health>number:
                    i.health-=number

    def invisibility(self,number):
        pass
