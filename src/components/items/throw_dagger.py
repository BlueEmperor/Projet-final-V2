import pygame

from src.components.items.item import Item
from path import ASSETS_DIR
from src.components.animations.dagger_animation import DaggerAnimation

class ThrowableDager(Item):
    COMMON_DAGGER = ("Common Dagger", pygame.image.load(ASSETS_DIR / "dagger.png").convert_alpha(), 4, [1,3], DaggerAnimation)
    RARE_DAGGER = ("Common Dagger", pygame.image.load(ASSETS_DIR / "dagger.png").convert_alpha(), 7, [1,4], DaggerAnimation)
    EPIC_DAGGER = ("Common Dagger", pygame.image.load(ASSETS_DIR / "dagger.png").convert_alpha(), 10, [1,4], DaggerAnimation)
    LEGENDARY_DAGGER = ("Common Dagger", pygame.image.load(ASSETS_DIR / "dagger.png").convert_alpha(), 20, [1,5], DaggerAnimation)
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