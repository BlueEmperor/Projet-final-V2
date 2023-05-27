import pygame

from path import ASSETS_DIR,CARAC_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Potion(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "potion.png").convert_alpha()
    health_inventory_effect= pygame.image.load(ASSETS_DIR / "heart_icon.png").convert_alpha()
    commune_damage_inventory_effect = pygame.image.load(CARAC_DIR / "commune_damage1.png").convert_alpha()
    rare_damage_inventory_effect = pygame.image.load(CARAC_DIR / "rare_damage1.png").convert_alpha()
    epic_damage_inventory_effect = pygame.image.load(CARAC_DIR / "epic_damage1.png").convert_alpha()
    legendary_damage_inventory_effect =pygame.image.load(CARAC_DIR / "legendary_damage1.png").convert_alpha()
    HEALTH_POTION = (("PCSI Health Potion",IMAGE,"Health",lambda hero, m: hero.heal(5), 1, health_inventory_effect, 1,  " Up the health by 5") ,
                     ("Rare Health Potion",IMAGE,"Health",lambda hero, m: hero.heal(10), 1, health_inventory_effect,1, " Up the health by 5") ,
                     ("Epic Health Potion",IMAGE, "Health",lambda hero, m: hero.heal(20), 1, health_inventory_effect,1," Up the health by 5"),
                     ("Legendary Health Potion",IMAGE,"Health",lambda hero, m: hero.heal(hero.max_health), 1, health_inventory_effect, 2," Up the health by 5"))
    
    ARMOR_BOOST_POTION = (("Classic Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(1.1), 10),
                          ("Rare Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(1.2), 10),
                          ("Epic Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(1.3),10),
                          ("Monstruous Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(2),10))
    
    DAMAGE_BOOST_POTION = (("Small Damage Potion",IMAGE,"Damage",lambda hero, m: hero.damage_boost(1.2), 10, commune_damage_inventory_effect, 1,"Increases the damages by 20% "),
                           ("Rare Damage Potion",IMAGE,"Damage",lambda hero, m: hero.damage_boost(1.2), 20, rare_damage_inventory_effect, 1,"Increases the damages by 20%" ),
                           ("Epic Damage Potion",IMAGE,"Damage",lambda hero, m: hero.damage_boost(1.5), 20,epic_damage_inventory_effect, 2,"Increases the damages by 50%" ),
                           ("Enormous Damage Potion",IMAGE,"Damage",lambda hero : hero.damage_boost(2), 20,legendary_damage_inventory_effect, 2,"Increases the damages by 100%"))
    
    POISON_POTION = (("Commune Poison Potion",IMAGE,"Poison",lambda hero, m : hero.poison_attack(5,m), 1),
                     ("Rare Poison Potion",IMAGE,"Poison",lambda hero, m : hero.poison_attack(10,m), 1),
                     ("Epic Poison Potion",IMAGE,"Poison", lambda hero, m : hero.poison_attack(20,m),1),
                     ("Legendary Poison Potion",IMAGE,"Poison", lambda hero, m : hero.poison_attack(50,m), 1))
    
    INVISIBILITY_POTION = (("Short Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 3),
                           ("Rare Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 5),
                           ("Epic Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 10),
                           ("Legendary Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 20, 2))
    
    LIST = [ DAMAGE_BOOST_POTION]#[HEALTH_POTION,ARMOR_BOOST_POTION,DAMAGE_BOOST_POTION,INVISIBILITY_POTION,POISON_POTION]

    def __init__(self,name,image,usage,effect, turn,inventory_effect=None, durability=1, description=None):
        super().__init__()
        self.name = name
        self.image = image
        self.image_icon = self.image
        self.inventory_effect= inventory_effect
        self.effect = effect
        self.rect = pygame.Rect(0,0,32, 32)
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.durability = durability
        self.rarity= None
        self.description = description
        self.usage = usage
        self.turn = turn
        



    


