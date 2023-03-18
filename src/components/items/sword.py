import pygame

from path import ASSETS_DIR

vec = pygame.math.Vector2

class Sword(pygame.sprite.Sprite):
    NOT_SELECTED_IMAGE = pygame.image.load(ASSETS_DIR / "sword_icon.png").convert_alpha()
    SELECTED_IMAGE = pygame.image.load(ASSETS_DIR / "sword_icon_selected.png").convert_alpha()
    def __init__(self):
        super().__init__()
        self.image = Sword.NOT_SELECTED_IMAGE
        self.rect = self.image.get_rect()
        self.slot = vec(0,0)
    
    def update(self, coord):
        self.rect.topleft = vec(215,23)+vec(coord[0], coord[1])+self.slot*48
        if(self.rect.collidepoint(pygame.mouse.get_pos())):
            self.image = Sword.SELECTED_IMAGE
        else:
            self.image = Sword.NOT_SELECTED_IMAGE