import pygame

from src.components.entities.entity import Entity

class player(Entity):
    def __init__(self,name,coord,absolute_coord):
        super().__init__(name,coord,absolute_coord)
        self.ismoving = False
        
    def update(self):
        if(self.ismoving):
            pass