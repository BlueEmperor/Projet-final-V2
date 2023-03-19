import pygame

from path import ASSETS_DIR, AUDIO_DIR

vec = pygame.math.Vector2

class Sword(pygame.sprite.Sprite):
    NOT_SELECTED_IMAGE = pygame.image.load(ASSETS_DIR / "sword_icon.png").convert_alpha()
    SELECTED_IMAGE = pygame.image.load(ASSETS_DIR / "sword_icon_selected.png").convert_alpha()
    def __init__(self):
        super().__init__()
        self.image = Sword.NOT_SELECTED_IMAGE
        self.rect = self.image.get_rect()
        self.slot = vec(0,0)
        self.description = "Une épée qui fait mal !"
        self.damage = 3
        self.durability = 10
    
    def update(self, coord):
        self.rect.topleft = vec(215,23)+vec(coord)+self.slot*48