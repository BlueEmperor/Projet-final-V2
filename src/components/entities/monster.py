import pygame

from path import ASSETS_DIR
from src.config import Config
from src.components.entities.entity import Entity
from src.components.items.sword import Sword
from src.components.items.wand import Wand


vec=pygame.math.Vector2

class Monster(Entity):
    SQUELETTE = ("Squelette", 8, 1, Sword(*Sword.SKELETON_SWORD), [pygame.image.load(ASSETS_DIR / ("squelette.png")).convert_alpha(), pygame.image.load(ASSETS_DIR / ("squelette_hover.png")).convert_alpha()], 8)
    VAMPIRE = ("Vampire", 15, 1, Wand(*Wand.COMMUNE_WAND), [pygame.image.load(ASSETS_DIR / ("vampire.png")).convert_alpha(), pygame.image.load(ASSETS_DIR / ("vampire_hover.png")).convert_alpha()], 12)
    MONSTER_LIST = [SQUELETTE, VAMPIRE]
    
    def __init__(self,name,health,speed, weapon, image_list, xp, pos):
        super().__init__(name, pos,image_list, health)
        self.speed = speed
        self.weapon = weapon
        self.aggro = False
        self.xp = xp

    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
        if self.ismoving !=False:
            self.absolute_pos += self.ismoving
            self.moving_tick-=1
            if(self.moving_tick==0):
                self.ismoving=False
    
    def move(self,m):
        coord = (self.map_pos-m._player.map_pos)
        if((coord[0]**2+coord[1]**2)**0.5>8 and not(m.line_of_sight(self.map_pos, m._player.map_pos))):
            return
        
        chemin=m.A_star(self.map_pos, m._player.map_pos)
        if(len(chemin) == 0):
            return
        
        m.move(self.map_pos,chemin[-1])
        self.ismoving=(chemin[-1]-self.map_pos)*4
        self.map_pos=chemin[-1]
        self.moving_tick = 12
       
    
    def turn_action(self, m, animation):
        if(self.aggro):
            if self.can_attack(m._player, m):
                self.meet(m._player, m, animation)
            else:
                self.move(m)
