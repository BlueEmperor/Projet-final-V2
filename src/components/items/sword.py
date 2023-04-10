import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Sword(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha()
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(Sword.IMAGE, (72,72))
        self.rect = self.image.get_rect()
        self.name = "sword"
        self.type = "sword"
        self.attack_type = "zone"
        self.description = "Une épée qui fait mal !"
        self.damage = 3
        self.durability = 10
        self.range = vec(1,1)
        self.wall_ability = False