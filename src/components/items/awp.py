import pygame

from path import ASSETS_DIR, AUDIO_DIR,WEAPON_DIR
from src.components.items.item import Item
from src.components.animations.fire_shot_animation import FireShotAnimation

vec = pygame.math.Vector2

class Awp(Item):
    #IMAGE = pygame.image.load(WEAPON_DIR / "bluegem_awp.png").convert_alpha()
    classic_awp = pygame.image.load(WEAPON_DIR / "commune_awp.png").convert_alpha()
    dragonlore_awp = pygame.image.load(WEAPON_DIR / "epic_awp.png").convert_alpha()
    golden_awp = pygame.image.load(WEAPON_DIR / "golden_awp.png").convert_alpha()
    legendary_awp = pygame.image.load(WEAPON_DIR / "gugnir_awp.png").convert_alpha()

    #SKELETON_awp =("timothée's awp",IMAGE, 20, 200, vec(1,1),FireShotAnimation)
    COMMUNE_AWP = ("Marseille awp", classic_awp, 100, 50, vec(1,8),FireShotAnimation)
    RARE_AWP = ("terrorist awp", dragonlore_awp, 150, 20, vec(1,8),FireShotAnimation)
    EPIC_AWP = ("quiet kid's awp", golden_awp, 200, 50, vec(1,8),FireShotAnimation)
    LEGENDARY_AWP = ("Iran awp", legendary_awp, 250, 100, vec(1,8),FireShotAnimation)
    LIST = [COMMUNE_AWP,RARE_AWP,EPIC_AWP,LEGENDARY_AWP]
    
    def __init__(self, name, image, damage, durability, range, animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "zone"
        self.description = "Si je sors la awp je sais qu ils feront tous caca"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = False
        self.animation = animation