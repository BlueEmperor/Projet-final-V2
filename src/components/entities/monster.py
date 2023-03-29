import pygame

from src.components.entities.entity import Entity
from src.config import Config
from src.components.items.sword import Sword
from path import ASSETS_DIR

vec=pygame.math.Vector2

class Monster(Entity):
    SQUELETTE = ("Squelette", 8, 1, Sword(), [pygame.image.load(ASSETS_DIR / ("squelette.png")).convert_alpha()])
    VAMPIRE = ("Vampire", 15, 1, Sword(), [pygame.image.load(ASSETS_DIR / ("vampire.png")).convert_alpha()])
    MONSTER_LIST = [SQUELETTE, VAMPIRE]
    
    def __init__(self,name,health,speed, weapon, image_list, pos):
        super().__init__(name,pos,image_list)
        self.speed = speed
        self.weapon = weapon
        self.health = health
        self.max_health = health
        self.aggro = True

    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
        if self.ismoving !=False:
            self.absolute_pos += self.ismoving
            self.moving_tick-=1
            if(self.moving_tick==0):
                self.ismoving=False

    def can_attack(self,other,m):
        return False
    
    def move(self,m):
        coord = (self.map_pos-m._player.map_pos)
        if((coord[0]**2+coord[1]**2)**0.5>8 or not(self.aggro)):
            return
        
        chemin=m.A_star(self.map_pos, m._player.map_pos)
        if(len(chemin)==0):
            return
        
        m.move(self.map_pos,chemin[-1])
        self.ismoving=(chemin[-1]-self.map_pos)*4
        self.map_pos=chemin[-1]
        self.moving_tick = 12
       
    
    def turn_action(self, m,player):
        if self.can_attack(player,m):
            pass
        else:
            self.move(m)
