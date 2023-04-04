import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Wand(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha()
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(Wand.IMAGE, (72,72))
        self.rect = self.image.get_rect()
        self.name = "baton"
        self.type = "wand"
        self.attack_type = "linear"
        self.description = "Un baton dangereux !"
        self.damage = 2
        self.durability = 15
        self.range = vec(3, 5)
        self.wall_ability = True