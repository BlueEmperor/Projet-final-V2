import pygame

from src.components.items.item import Item
from path import ASSETS_DIR, WEAPON_DIR
from src.components.animations.dagger_animation import DaggerAnimation

class ThrowableDager(Item):
    common_dagger = pygame.image.load(WEAPON_DIR / "wood_dagger.png").convert_alpha()
    rare_dagger = pygame.image.load(WEAPON_DIR / "silver_dagger.png").convert_alpha()
    epic_dagger = pygame.image.load(WEAPON_DIR / "golden_dagger.png").convert_alpha()
    legendary_dagger = pygame.image.load(WEAPON_DIR / "diamond_dagger.png").convert_alpha()
    COMMON_DAGGER = ("Common Dagger", common_dagger, 10, [1,5], DaggerAnimation)
    RARE_DAGGER = ("Rare Dagger", rare_dagger,20, [1,5], DaggerAnimation)
    EPIC_DAGGER = ("Epic Dagger", epic_dagger, 30, [1,5], DaggerAnimation)
    LEGENDARY_DAGGER = ("Epic Dagger", legendary_dagger, 50, [1,5], DaggerAnimation)
    LIST = [COMMON_DAGGER, RARE_DAGGER, EPIC_DAGGER, LEGENDARY_DAGGER]
    def __init__(self, name, image, damage, range, animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "zone"
        self.description = "Attention, ça se lance"
        self.damage = damage
        self.durability = 1
        self.range = range
        self.wall_ability = False
        self.animation = animation