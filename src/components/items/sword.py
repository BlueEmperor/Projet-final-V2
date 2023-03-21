import pygame

from path import ASSETS_DIR, AUDIO_DIR

vec = pygame.math.Vector2

class Sword(pygame.sprite.Sprite):
    NOT_SELECTED_IMAGE = pygame.image.load(ASSETS_DIR / "sword_icon.png").convert_alpha()
    SELECTED_IMAGE = pygame.image.load(ASSETS_DIR / "sword_icon_selected.png").convert_alpha()
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(Sword.NOT_SELECTED_IMAGE, (72,72))
        self.rect = self.image.get_rect()
        self.slot = vec(0,0)
        self.in_hotbar = False
        self.description = "Une épée qui fait mal !"
        self.damage = 3
        self.durability = 10
    
    def update(self, inventory_topleft, hotbar_topleft):
        if(self.in_hotbar):
            self.rect.topleft = vec(89,11)+vec(hotbar_topleft)+self.slot*72
        else:
            self.rect.topleft = vec(323,35)+vec(inventory_topleft)+self.slot*72