import pygame

vec = pygame.math.Vector2

class Entity:
    def __init__(self,name,coord,absolute_coord):
        self._name=name
        self._map_coord=coord
        self.absolute_coord=absolute_coord
    def __repr__(self):
        return(self._name)
    

        