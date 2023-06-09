import pygame

from path import ASSETS_DIR, WEAPON_DIR
from src.components.items.item import Item
from src.components.animations.bow_animation import BowAnimation

vec = pygame.math.Vector2

class Bow(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "bow_icon.png").convert_alpha()
    silver_bow = pygame.image.load(WEAPON_DIR / "silver_bow.png").convert_alpha()
    golden_bow = pygame.image.load(WEAPON_DIR / "golden_bow.png").convert_alpha()
    diamond_bow = pygame.image.load(WEAPON_DIR / "diamond_bow.png").convert_alpha()
    ARCHER_BOW = ("Archer's bow", IMAGE, 2, 30 ,vec(1,4))
    COMMUNE_BOW =("Everyday's bow", IMAGE, 5, 30 ,vec(2,5))
    RARE_BOW =("David Bowie's bow", silver_bow, 10, 50 ,vec(2,5))
    EPIC_BOW =("Bo bow", golden_bow, 20, 50 ,vec(2,5))
    LEGENDARY_BOW =("Racist bow",diamond_bow, 40, 100, vec(2,5))
    LIST=[COMMUNE_BOW,RARE_BOW,EPIC_BOW,LEGENDARY_BOW]
    
    def __init__(self,name,image,damage,durability,range,animation = BowAnimation):
        super().__init__()
        self.image = pygame.transform.scale(image,(72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "zone"
        self.description = "Un arc magique !"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = True
        self.animation = animation