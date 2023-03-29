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

    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
    
    def turn_action(self, m):
        print("zob")