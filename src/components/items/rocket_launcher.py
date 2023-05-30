import pygame

from path import ASSETS_DIR, AUDIO_DIR,WEAPON_DIR
from src.components.items.item import Item
from src.components.animations.rpg_animation import RpgAnimation

vec = pygame.math.Vector2

class Rocket_launcher(Item):
    IMAGE = pygame.image.load(WEAPON_DIR / "diamond_rocket_launcher.png").convert_alpha()
    classic_rocket_launcher = pygame.image.load(WEAPON_DIR / "wood_rocket_launcher.png").convert_alpha()
    silver_rocket_launcher = pygame.image.load(WEAPON_DIR / "silver_rocket_launcher.png").convert_alpha()
    golden_rocket_launcher = pygame.image.load(WEAPON_DIR / "golden_rocket_launcher.png").convert_alpha()
    bluegem_rocket_launcher = pygame.image.load(WEAPON_DIR / "diamond_rocket_launcher.png").convert_alpha()

    SKELETON_rocket_launcher =("timothée's rocket_launcher",IMAGE, 20, 200, vec(1,1) )
    COMMUNE_ROCKET_LAUNCHER = ("Marseille rocket_launcher", classic_rocket_launcher, 20, 50, vec(1,8),RpgAnimation)
    RARE_ROCKET_LAUNCHER = ("terrorist rocket_launcher", silver_rocket_launcher, 50, 20, vec(1,8),RpgAnimation)
    EPIC_ROCKET_LAUNCHER = ("Kim Jon HUng rocket_launcher", golden_rocket_launcher, 100, 50, vec(1,8),RpgAnimation)
    LEGENDARY_ROCKET_LAUNCHER = ("USA rocket_launcher", bluegem_rocket_launcher, 200, 100, vec(1,8),RpgAnimation)
    LIST = [COMMUNE_ROCKET_LAUNCHER,RARE_ROCKET_LAUNCHER,EPIC_ROCKET_LAUNCHER,LEGENDARY_ROCKET_LAUNCHER]
    
    def __init__(self, name, image, damage, durability, range, animation = None):
        super().__init__()
        self.image = pygame.transform.scale(image, (72,72))
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.name = name
        self.attack_type = "continuous"
        self.description = "Vous aimez les explosions?"
        self.damage = damage
        self.durability = durability
        self.range = range
        self.wall_ability = False
        self.animation = animation