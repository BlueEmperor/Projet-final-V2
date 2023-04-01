import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.entities.entity import Entity

vec = pygame.math.Vector2

class Coffre(Entity):
    COFFRE_EZ = ("coffre_ez",pygame.image.load(ASSETS_DIR / "coffre.png").convert_alpha(),1)
    def __init__(self,pos,name,image_list, open_time=1):
        super().__init__(name,pos,image_list)
        self.description = "Un coffre"
        self.open_time = open_time
        self.wall_ability = False

    def update(self, player):
        self.rect.topleft = vec(self.rect.topleft)
        if self.isopening !=False:
            return
        else: 
            return

    
