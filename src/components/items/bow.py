import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item
from src.components.animations.bow_animation import BowAnimation

vec = pygame.math.Vector2

class Bow(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "bow_icon.png").convert_alpha()
    ARCHER_BOW = ("Archer's bow", IMAGE, 2, 30 ,vec(1,4))
    COMMUNE_BOW =("Everyday's bow", IMAGE, 2, 30 ,vec(1,6))
    RARE_BOW =("David Bowie's bow", IMAGE, 5, 50 ,vec(1,6))
    EPIC_BOW =("Bo bow", IMAGE, 10, 50 ,vec(1,6))
    LEGENDARY_BOW =("Racist bow",IMAGE, 15, 100, vec(1,7))
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