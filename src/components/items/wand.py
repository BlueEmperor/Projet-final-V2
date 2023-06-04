import pygame

from path import ASSETS_DIR, WEAPON_DIR
from src.components.items.item import Item
from src.components.animations.fireball_animation import FireballAnimation

vec = pygame.math.Vector2

class Wand(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha()
    silver_wand = pygame.image.load(WEAPON_DIR / "silver_wand.png").convert_alpha()
    golden_wand = pygame.image.load(WEAPON_DIR / "golden_wand.png").convert_alpha()
    diamond_wand = pygame.image.load(WEAPON_DIR / "diamond_wand.png").convert_alpha()
    VAMPIRE_WAND = ("Vampire's wand", IMAGE, 8, 30 ,vec(1,4), 0, FireballAnimation)
    COMMUNE_WAND =("Harry Potter's wand", IMAGE, 5, 30 ,vec(1,4), 25, FireballAnimation)
    RARE_WAND =("Hermione's wand", silver_wand, 10, 50 ,vec(1,4), 30,FireballAnimation)
    EPIC_WAND =("APAGNAN's wand", golden_wand, 20, 50 ,vec(1,4), 40,FireballAnimation)
    LEGENDARY_WAND =("CROPINOU's wand",diamond_wand, 50, 100, vec(1,4), 50,FireballAnimation)
    LIST=[COMMUNE_WAND,RARE_WAND,EPIC_WAND,LEGENDARY_WAND]

    def __init__(self,name,image,damage,durability,range,mana,animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image,(72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "linear"
        self.description = "Un baton dangereux !"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = True
        self.animation = animation
        self.mana = mana