import pygame

from path import ASSETS_DIR
from src.components.entities.monster import Monster
from src.components.entities.player import Player

vec = pygame.math.Vector2

class Hover:
    HOVER_RECTANGLE = pygame.image.load(ASSETS_DIR / "hover_info.png").convert_alpha()

    def __init__(self, m):
        self._map = m
        self.current_hover = None
        self.image = Hover.HOVER_RECTANGLE
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 30)
        
    def update(self):
        item = self._map.get_item(self._map.mouse_pos)
        if(self.current_hover != None):
            self.current_hover.image = self.current_hover.image_list[0]
        self.current_hover = None

        if(not(item in (self._map.GROUND, self._map.WALL))):
            if(not(isinstance(item, Player))):
                self.current_hover = item
                self.rect.center = self.current_hover.rect.center + vec(0, -85)
                self.current_hover.image = self.current_hover.hover_list[0]

    def draw(self, SCREEN):
        if(self.current_hover != None):
            SCREEN.blit(self.image, self.rect)
            if(isinstance(self.current_hover, Monster)):
                SCREEN.blit(self.font.render("Health : " + str(self.current_hover.health) + "/" + str(self.current_hover.max_health),True,(255, 255, 255)), vec(self.rect.topleft)+vec(15,12))