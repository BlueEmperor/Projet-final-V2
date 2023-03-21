import pygame

from src.components.entities.monster import Monster
from path import ASSETS_DIR
class Squelette(Monster):
    def __init__(self,position):
        self.image_list = [pygame.image.load(ASSETS_DIR / ("squelette.png")).convert_alpha()]
        super().__init__(name="Squelette", pos=position, health=10,image_list=self.image_list)

    