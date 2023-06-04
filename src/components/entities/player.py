import pygame

from path import ASSETS_DIR
from src.config import Config
from src.components.entities.entity import Entity
from src.global_state import GlobalState
from src.status import GameStatus

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self):
        self.image_list = [pygame.image.load(ASSETS_DIR / ("entities/player/player" + str(i+1) + ".png")).convert_alpha() for i in range(4)]
        self.big_image_list = [pygame.image.load(ASSETS_DIR / ("entities/player/player" + str(i+1) + "_inv.png")).convert_alpha() for i in range(4)]
        super().__init__("player", vec(4,4), self.image_list)
        
        self.rect.center=vec(Config.WIDTH/2, Config.HEIGHT/2)
        self.hotbar = [None for _ in range(9)]
        self.inventory = [[None for _ in range(9)] for _ in range(4)]
        self.armor = [[None for _ in range(2)] for _ in range(2)]
        self.health = 20
        self.max_health = 20
        self.gold = 0
        self.mana = 60
        self.max_mana = self.mana
        self.level = 1
        self.experience = 0
        self.experience_to_level_up = lambda: int((self.level+1)**2.2 + 12)
        self.xp = 0 #Juste pour que le jeu ne crash pas quand le player meurt, ne sert pas sinon
        self.effects = [] #[[function lambda, duration, name of the effect, image of the potion], ...]
        self.map_level = 0
    
    #def get_item(self,n):
    def effect(self, m):
        self.health_boost, self.defense_boost, self.damage_boost, self.mana_boost = 1, 1, 1, 1

        i = 0
        while(i < len(self.effects)):
            self.effects[i][1] -= 1
            self.effects[i][0](self, m)
            if(self.effects[i][1] <= 0):
                self.effects.pop(i)
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

    def armor_bonus(self,number):
        self.defense_boost = number

    def damage_bonus(self,number):
        self.damage_boost = number
    
    def update_defense(self):
        self.defense = 0
        for i in range(2):
            for j in range(2):
                self.defense += self.armor[j][i].defense if(self.armor[j][i] != None) else 0

    def update(self):
        if(self.actual_frame == 0):
            self.actual_frame = 15
            self.current_image += 1
            if(self.current_image >= len(self.image_list)):
                self.current_image = 0
            self.image = self.image_list[self.current_image]
            
        self.actual_frame -= 1
        if(self.health <= 0):
            GlobalState.GAME_STATE = GameStatus.GAME_END
