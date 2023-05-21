import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Sword(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha()
    SKELETON_SWORD =("Skeleton sword",IMAGE, 4, 200, vec(1,1) )
    COMMUNE_SWORD = ("Jesus sword", IMAGE, 5, 50, vec(1,1))
    RARE_SWORD = ("SEXYSEB's sword", IMAGE, 8, 20, vec(1,1))
    EPIC_SWORD = ("Timozob' sword", IMAGE, 10, 50, vec(1,1))
    LEGENDARY_SWORD = ("3 FROMAGES' Sword", IMAGE, 15, 100, vec(1,2))
    LIST = [COMMUNE_SWORD,RARE_SWORD,EPIC_SWORD,LEGENDARY_SWORD]
    def __init__(self, name, image, damage, durability, range, animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "zone"
        self.description = "Une épée qui fait mal !"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = False
        self.animation = animation
 