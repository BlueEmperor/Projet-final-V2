import pygame

from src.components.entities.entity import Entity
from src.config import Config

vec=pygame.math.Vector2

class Monster(Entity):
    def __init__(self,name,pos,health,image_list):
        super().__init__(name,pos,health,image_list)

    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
    
    def turn_action(self, m):
        print("zob")