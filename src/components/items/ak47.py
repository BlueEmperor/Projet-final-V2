import pygame

from path import WEAPON_DIR
from src.components.items.item import Item
from src.components.animations.fire_shot_animation import FireShotAnimation

vec = pygame.math.Vector2

class Ak(Item):
    IMAGE = pygame.image.load(WEAPON_DIR / "bluegem_ak.png").convert_alpha()
    classic_ak = pygame.image.load(WEAPON_DIR / "classic_ak.png").convert_alpha()
    silver_ak = pygame.image.load(WEAPON_DIR / "silver_ak.png").convert_alpha()
    golden_ak = pygame.image.load(WEAPON_DIR / "golden_ak.png").convert_alpha()
    bluegem_ak = pygame.image.load(WEAPON_DIR / "bluegem_ak.png").convert_alpha()

    #SKELETON_AK =("timothée's ak",IMAGE, 20, 200, vec(1,1),FireShotAnimation)
    COMMUNE_AK = ("Marseille ak", classic_ak, 20, 50, vec(1,8),FireShotAnimation)
    RARE_AK = ("terrorist ak", silver_ak, 50, 20, vec(1,8),FireShotAnimation)
    EPIC_AK = ("quiet kid's ak", golden_ak, 100, 50, vec(1,8),FireShotAnimation)
    LEGENDARY_AK = ("Iran ak", bluegem_ak, 200, 100, vec(1,8),FireShotAnimation)
    LIST = [COMMUNE_AK,RARE_AK,EPIC_AK,LEGENDARY_AK]
    
    def __init__(self, name, image, damage, durability, range, animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "zone"
        self.description = "Si je sors la AK je sais qu ils feront tous caca"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = False
        self.animation = animation