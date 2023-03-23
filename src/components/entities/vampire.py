import pygame

from src.components.entities.monster import Monster
from path import ASSETS_DIR
class Vampire(Monster):
    def __init__(self,position):
        self.image_list = [pygame.image.load(ASSETS_DIR / ("vampire.png")).convert_alpha()]
        super().__init__(name="Vampire", pos=position, health=10,image_list=self.image_list)