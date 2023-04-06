import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.entities.entity import Entity

vec = pygame.math.Vector2

class Coffre(Entity):
    COFFRE_EZ = [pygame.image.load(ASSETS_DIR / "coffre.png").convert_alpha()]
    HOVER_COFFRE = [pygame.image.load(ASSETS_DIR / "coffre_hover.png").convert_alpha()]
    def __init__(self,pos, open_time=1):
        super().__init__("coffre",pos,Coffre.COFFRE_EZ, Coffre.HOVER_COFFRE)
        self.description = "Un coffre"
        self.open_time = open_time
        self.wall_ability = False
        self.isopening = False

    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
        if self.isopening !=False:
            return
        else: 
            return

    
