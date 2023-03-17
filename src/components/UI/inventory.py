import pygame

from path import ASSETS_DIR
from src.config import Config

vec = pygame.math.Vector2

class InventoryUI:
    def __init__(self, player):
        self.image = pygame.image.load(ASSETS_DIR / "inventory.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (-Config.WIDTH/2, Config.HEIGHT/2)
        self._player = player
        self.isopen = False
        self.animation = 0
        self.direction = 1
        self.offset = 0

    def add(self, item):
        if(len(self._inv)<self.size):
            self._inv.append(item)
            return(True)
        return(False)

    def delete(self, item):
        self._inv.pop(self._inv.index(item))

    def K_e_event(self, key):
        if(not(self.animation)):
            self.animation = 16
            if(self.isopen):
                self.direction = -1
            else:
                self.direction = 1
            self.isopen = not(self.isopen)

    def left_click_down_event(self, mouse):
        if(self.isopen and not(self.animation)):
            pass
    
    def right_click_down_event(self, mouse):
        if(self.isopen and not(self.animation)):
            pass

    def update(self):
        if(self.animation != 0):
            self.animation -= 1
            self.offset += Config.WIDTH/16*self.direction

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.topleft[0]+self.offset, self.rect.topleft[1]))
        SCREEN.blit(self._player.image, (self.rect.topleft[0]+self.offset+87, self.rect.topleft[1]+140))