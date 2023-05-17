import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Wand(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha()
    VAMPIRE_WAND = ("Vampire's wand", pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha(), 2, 30 ,vec(4,4))
    WAND1 =("Harry Potter's wand", pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha(), 2, 30 ,vec(5,5))
    WAND2 =("Hermione's wand", pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha(), 5, 50 ,vec(3,3))
    WAND3 =("APAGNAN's wand", pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha(), 10, 50 ,vec(4,4))
    LIST=[WAND1,WAND2,WAND3]
    def __init__(self,name,image,damage,durability,range):
        super().__init__()
        self.image = pygame.transform.scale(Wand.IMAGE, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = "baton"
        self.type = "wand"
        self.attack_type = "linear"
        self.description = "Un baton dangereux !"
        self.damage = 2
        self.durability = 15
        self.range = vec(1, 5)
        self.wall_ability = True