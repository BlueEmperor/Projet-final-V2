import pygame

from src.components.entities.monster import Monster
from src.components.entities.player import Player

vec = pygame.math.Vector2

class Error(Exception):
    @staticmethod
    def isinstance_all_class(object, class_name):
        for class_ in class_name:
            if not isinstance(object, class_):
                raise TypeError(f"Expected {class_.__name__} but got {type(object).__name__}")

    @staticmethod
    def in_map(coord, m):
        if(coord[0] < 0 or coord[1] < 0 or coord[0] >= len(m.map[0]) or coord[1] >= len(m.map)):
            raise IndexError(f"Expected coord in map but got {coord}")

    @staticmethod
    def CheckCoord(coord, m):
        Error.isinstance_all_class(coord, vec)
        Error.in_map(coord, m)

    @staticmethod
    def CheckMonster(monster, m):
        Error.isinstance_all_class(monster, [Monster, Player])
        Error.in_map(monster.map_pos, m)