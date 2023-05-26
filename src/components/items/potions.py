import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Potion(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "potion.png").convert_alpha()
    HEALTH_POTION = (("PCSI Health Potion",IMAGE,"Health",lambda hero, m: hero.heal(5), 1) ,
                     ("Rare Health Potion",IMAGE,"Health",lambda hero, m: hero.heal(10), 1),
                     ("Epic Health Potion",IMAGE, "Health",lambda hero, m: hero.heal(20), 1, 2),
                     ("Legendary Health Potion",IMAGE,"Health",lambda hero, m: hero.heal(hero.max_health), 1, 2))
    
    ARMOR_BOOST_POTION = (("Classic Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(1.1), 10),
                          ("Rare Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(1.2), 10),
                          ("Epic Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(1.3),10),
                          ("Monstruous Armor Potion",IMAGE,"Armor",lambda hero, m: hero.armor_boost(2),10))
    
    DAMAGE_BOOST_POTION = (("Small Damage Potion",IMAGE,"Damage",lambda hero, m: hero.damage_boost(1.2), 10),
                           ("Rare Damage Potion",IMAGE,"Damage",lambda hero, m: hero.damage_boost(1.2), 20),
                           ("Epic Damage Potion",IMAGE,"Damage",lambda hero, m: hero.damage_boost(1.5), 20),
                           ("Enormous Damage Potion",IMAGE,"Damage",lambda hero : hero.damage_boost(2), 20))
    
    POISON_POTION = (("Commune Poison Potion",IMAGE,"Poison",lambda hero, m : hero.poison_attack(5,m), 1),
                     ("Rare Poison Potion",IMAGE,"Poison",lambda hero, m : hero.poison_attack(10,m), 1),
                     ("Epic Poison Potion",IMAGE,"Poison", lambda hero, m : hero.poison_attack(20,m),1),
                     ("Legendary Poison Potion",IMAGE,"Poison", lambda hero, m : hero.poison_attack(50,m), 1))
    
    INVISIBILITY_POTION = (("Short Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 3),
                           ("Rare Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 5),
                           ("Epic Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 10),
                           ("Legendary Invisibility Potion",IMAGE,"Invisibility", lambda hero, m: hero.invibility(), 20, 2))
    
    LIST = [HEALTH_POTION]#[HEALTH_POTION,ARMOR_BOOST_POTION,DAMAGE_BOOST_POTION,INVISIBILITY_POTION,POISON_POTION]

    def __init__(self,name,image,usage,effect, turn, durability=1):
        super().__init__()
        self.name = name
        self.image = image
        self.image_icon = self.image
        self.effect = effect
        self.rect = pygame.Rect(0,0,32, 32)
        self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.durability = durability
        self.rarity= None
        self.description = "Une potion magique"
        self.usage = usage
        self.turn = turn
        



    


