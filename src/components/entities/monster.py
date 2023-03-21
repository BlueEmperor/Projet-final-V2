import pygame

from src.components.entities.entity import Entity

vec=pygame.math.Vector2

class Monster(Entity):
    def __init__(self,name,pos,health,image_list):
        super().__init__(name,pos,health,image_list)
        self.deplacement=vec(0,0)
        
    def update(self, player):
        self.deplacement=vec(self.map_pos[0],self.map_pos[1])-vec(player.map_pos[0],player.map_pos[1])
        self.absolute_pos+=self.deplacement