import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Sword(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha()
    SKELETON_SWORD =("Skeleton sword",pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha(), 4, 200, vec(1,1) )
    SWORD1 = ("Jesus sword", pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha(), 5, 50, vec(2,2))
    SWORD2 = ("SEXYSEB' sword", pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha(), 8, 20, vec(2,2))
    SWORD3 = ("Timozob' sword", pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha(), 10, 50, vec(2,2))
    LIST = [SWORD1,SWORD2,SWORD3]
    def __init__(self, name, image, damage, durability, range):
        super().__init__()
        self.image = pygame.transform.scale(Sword.IMAGE, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = "sword"
        self.type = "sword"
        self.attack_type = "zone"
        self.description = "Une épée qui fait mal !"
        self.damage = 3
        self.durability = 10
        self.range = vec(1,1)
        self.wall_ability = False
 