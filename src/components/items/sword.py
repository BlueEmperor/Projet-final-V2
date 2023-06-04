import pygame

from path import ASSETS_DIR, WEAPON_DIR
from src.components.items.item import Item
from src.components.animations.slash_animation import SlashAnimation
vec = pygame.math.Vector2

class Sword(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "sword_item.png").convert_alpha()
    wood_sword = pygame.image.load(WEAPON_DIR / "wood_sword.png").convert_alpha()
    silver_sword = pygame.image.load(WEAPON_DIR / "silver_sword.png").convert_alpha()
    golden_sword = pygame.image.load(WEAPON_DIR / "golden_sword.png").convert_alpha()
    diamond_sword = pygame.image.load(WEAPON_DIR / "diamond_sword.png").convert_alpha()
    SKELETON_SWORD =("Skeleton sword",IMAGE, 4, 200, vec(1,1),0, SlashAnimation)
    COMMUNE_SWORD = ("Jesus sword", wood_sword, 8, 50, vec(1,1),10, SlashAnimation)
    RARE_SWORD = ("SEXYSEB's sword", silver_sword, 15, 20, vec(1,1),10, SlashAnimation)
    EPIC_SWORD = ("Timozob' sword", golden_sword, 30, 50, vec(1,1),20, SlashAnimation)
    LEGENDARY_SWORD = ("3 FROMAGES' Sword", diamond_sword, 50, 100, vec(1,2),50, SlashAnimation)
    LIST = [COMMUNE_SWORD,RARE_SWORD,EPIC_SWORD,LEGENDARY_SWORD]
    
    def __init__(self, name, image, damage, durability, range,mana, animation = None):
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
        self.mana= mana
 