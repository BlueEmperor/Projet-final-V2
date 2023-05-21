import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item
from src.config import Config
from src.components.animations.fireball_animation import FireballAnimation

vec = pygame.math.Vector2

class Wand(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha()
    VAMPIRE_WAND = ("Vampire's wand", IMAGE, 2, 30 ,vec(1,4))
    COMMUNE_WAND =("Harry Potter's wand", IMAGE, 2, 30 ,vec(1,5), FireballAnimation)
    RARE_WAND =("Hermione's wand", IMAGE, 5, 50 ,vec(1,3))
    EPIC_WAND =("APAGNAN's wand", IMAGE, 10, 50 ,vec(1,4))
    LEGENDARY_WAND =("CROPINOU's wand",IMAGE, 15, 100, vec(1,5))
    LIST=[COMMUNE_WAND,RARE_WAND,EPIC_WAND,LEGENDARY_WAND]
    def __init__(self,name,image,damage,durability,range,animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image,(72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "linear"
        self.description = "Un baton dangereux !"
        self.type="wand"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = True
        self.animation = animation