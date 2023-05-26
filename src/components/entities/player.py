import pygame

from path import ASSETS_DIR
from src.config import Config
from src.components.entities.entity import Entity
from src.components.entities.chest import Chest
from src.components.entities.monster import Monster
from src.components.items.item import Item

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self):
        self.image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + ".png")).convert_alpha() for i in range(4)]
        self.big_image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + "_inv.png")).convert_alpha() for i in range(4)]
        super().__init__("player", vec(4,4), self.image_list)
        self.rect.center=vec(Config.WIDTH/2, Config.HEIGHT/2)
        self.hotbar = [None for _ in range(9)]
        self.inventory = [[None for _ in range(9)] for _ in range(4)]
        self.armor = [None for _ in range(4)]
        self.health = 20
        self.max_health = 20
        self.health_boost = 0
        self.gold = 0
        self.mana = 60
        self.max_mana = self.mana
        self.mana_boost = 0
        self.defense = 0
        self.defense_boost = 0
        self.level = 1
        self.experience = 0
        self.experience_to_level_up = lambda: int((self.level+1)**2.2 + 12)
        self.xp = 0 #Juste pour que le jeu ne crash pas quand le player meurt, ne sert pas sinon
        self.effects = [] #[[function lambda, duration, name of the effect], ...]
    
    #def get_item(self,n):
    def effect(self, m):
        i = 0
        while(i < len(self.effects)):
            self.effects[i][1] -= 1
            self.effects[i][0](self, m)
            if(self.effects[i][1] == 0):
                self.effects.pop(0)
                i -= 1
            i += 1

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


    def add_experience(self, number):
        self.experience += number
        while(self.experience >= self.experience_to_level_up()):
            self.experience -= self.experience_to_level_up()
            self.level += 1
            self.max_health += 3
            self.health += 3
            self.mana += 20
            self.max_mana += 20

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
        self.health += number
        if(self.health > self.max_health):
            self.health = self.max_health

    def armor_boost(self,number):
        self.defense += number

    def damage_boost(self,function,tour):
        self.effects.append([])
        
        #self.weapon.damage+=number
        #while self.weapon.durability
        #while tour > 0:
            #pass
        #self.weapon.damage-=number

    def poison_attack(self,number,m=None):
        item=m.get_item(m.mouse_pos)
        for i in m.get_item_room(self):
            if isinstance(i,Monster) and i.health!=None:
                if i.health<=number:
                    i.kill
                elif i.health>number:
                    i.health-=number
        self.remove_inventory(item)
        return number

    def invisibility(self,number):
        return number
