import pygame

from src.components.entities.monster import Monster
from src.components.entities.player import Player
from src.components.entities.chest import Chest

vec = pygame.math.Vector2

class Error(Exception):
    @staticmethod
    def is_entity(entity):
        if(not isinstance(entity, (Player, Monster, Chest))):
            raise TypeError(f"Expected entity but got {entity.__class__.__name__}")
        
    @staticmethod
    def in_map(coord, m):
        if(coord[0] < 0 or coord[1] < 0 or coord[0] >= len(m.map[0]) or coord[1] >= len(m.map)):
            raise IndexError(f"Expected coord in map but got {coord}")

    @staticmethod
    def CheckCoord(coord, m):
        Error.in_map(coord, m)

    @staticmethod
    def CheckMonster(monster, m):
        Error.is_entity(monster)
        Error.in_map(monster.map_pos, m)