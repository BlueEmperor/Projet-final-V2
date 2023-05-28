import pygame

from path import ASSETS_DIR,CARAC_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Potion(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "potion.png").convert_alpha()
    health= pygame.image.load(ASSETS_DIR / "heart_icon.png").convert_alpha()
    #health potion images
    commune_health=pygame.image.load(CARAC_DIR / "commune_health1.png").convert_alpha()
    rare_health=pygame.image.load(CARAC_DIR / "rare_health1.png").convert_alpha()
    epic_health=pygame.image.load(CARAC_DIR / "epic_health1.png").convert_alpha()
    legendary_health=pygame.image.load(CARAC_DIR / "legendary_health1.png").convert_alpha()
    #armor potion images
    commune_armor= pygame.image.load(CARAC_DIR / "commune_armor1.png").convert_alpha()
    rare_armor= pygame.image.load(CARAC_DIR / "rare_armor1.png").convert_alpha()
    epic_armor= pygame.image.load(CARAC_DIR / "epic_armor1.png").convert_alpha()
    legendary_armor= pygame.image.load(CARAC_DIR / "legendary_armor1.png").convert_alpha()
    #damage potion images
    commune_damage = pygame.image.load(CARAC_DIR / "commune_damage1.png").convert_alpha()
    rare_damage = pygame.image.load(CARAC_DIR / "rare_damage1.png").convert_alpha()
    epic_damage = pygame.image.load(CARAC_DIR / "epic_damage1.png").convert_alpha()
    legendary_damage =pygame.image.load(CARAC_DIR / "legendary_damage1.png").convert_alpha()

    #poison potion images
    commune_poison = pygame.image.load(CARAC_DIR / "commune_poison1.png").convert_alpha()
    rare_poison = pygame.image.load(CARAC_DIR / "rare_poison1.png").convert_alpha()
    epic_poison = pygame.image.load(CARAC_DIR / "epic_poison1.png").convert_alpha()
    legendary_poison = pygame.image.load(CARAC_DIR / "legendary_poison1.png").convert_alpha()

    #invisibility potion images

    
    HEALTH_POTION = [("PCSI Health Potion",commune_health,"Health",lambda hero, m: hero.heal(5), 1, health, 1,  " Up the health by 5") ,
                     ("Rare Health Potion",rare_health,"Health",lambda hero, m: hero.heal(10), 1, health,1, " Up the health by 5") ,
                     ("Epic Health Potion",epic_health, "Health",lambda hero, m: hero.heal(20), 1, health,1," Up the health by 5"),
                     ("Legendary Health Potion",legendary_health,"Health",lambda hero, m: hero.heal(hero.max_health), 1, health, 2," Up the health by 5")]
    
    ARMOR_BOOST_POTION = [("Classic Armor Potion",commune_armor,"Armor",lambda hero, m: hero.armor_bonus(1.1), 10),
                          ("Rare Armor Potion",rare_armor,"Armor",lambda hero, m: hero.armor_bonus(1.2), 10),
                          ("Epic Armor Potion",epic_armor,"Armor",lambda hero, m: hero.armor_bonus(1.3),10),
                          ("Monstruous Armor Potion",legendary_armor,"Armor",lambda hero, m: hero.armor_bonus(2),10)]
    
    DAMAGE_BOOST_POTION = [("Small Damage Potion",commune_damage,"Damage",lambda hero, m: hero.damage_bonus(1.2), 10, commune_damage, 1,"Increases the damages by 20% "),
                           ("Rare Damage Potion",rare_damage,"Damage",lambda hero, m: hero.damage_bonus(1.2), 20, rare_damage, 1,"Increases the damages by 20%" ),
                           ("Epic Damage Potion",epic_damage,"Damage",lambda hero, m: hero.damage_bonus(1.5), 20,epic_damage, 2,"Increases the damages by 50%" ),
                           ("Enormous Damage Potion",legendary_damage,"Damage",lambda hero : hero.damage_bonus(2), 20,legendary_damage, 2,"Increases the damages by 100%")]
    
    POISON_POTION = [("Commune Poison Potion",commune_poison,"Poison",lambda hero, m : hero.poison_attack(5,m), 1),
                     ("Rare Poison Potion",rare_poison,"Poison",lambda hero, m : hero.poison_attack(10,m), 1),
                     ("Epic Poison Potion",epic_poison,"Poison", lambda hero, m : hero.poison_attack(20,m),1),
                     ("Legendary Poison Potion",legendary_poison,"Poison", lambda hero, m : hero.poison_attack(50,m), 1)]
    
    INVISIBILITY_POTION = [("Short Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 3),
                           ("Rare Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 5),
                           ("Epic Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 10),
                           ("Legendary Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 20, 2)]
    
    LIST = [HEALTH_POTION, ARMOR_BOOST_POTION, DAMAGE_BOOST_POTION] #, POISON_POTION, INVISIBILITY_POTION]

    def __init__(self,name,image,usage,effect, turn,inventory_effect=None, durability=1, description=None):
        super().__init__()
        self.name = name
        self.image = image
        self.inventory_effect= inventory_effect
        self.effect = effect
        self.rect = self.image.get_rect()
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.durability = durability
        self.rarity= None
        self.description = description
        self.usage = usage
        self.turn = turn