import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Potion(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "potion.png").convert_alpha()
    HEALTH_POTION = (("PCSI Health Potion",IMAGE,lambda hero: hero.heal(5), 1) ,("Rare Health Potion",IMAGE,lambda hero: hero.heal(10), 1), ("Epic Health Potion",IMAGE, lambda hero: hero.heal(20), 2), (" Legendary Health Potion",IMAGE,lambda hero: hero.heal(hero.max_health), 2))
    ARMOR_BOOST_POTION = (("Classic Armor Potion",IMAGE,lambda hero : hero.armor_boost(10),1),("Rare Armor Potion",IMAGE,lambda hero : hero.armor_boost(20),1),("Epic Armor Potion",IMAGE,lambda hero : hero.armor_boost(30),1),("Monstruous Armor Potion",IMAGE,lambda hero : hero.armor_boost(hero.max_armor),1))
    DAMAGE_BOOST_POTION = ((" Small Damage Potion",IMAGE,lambda hero : hero.damage_boost(20,10)),(" Rare Damage Potion",IMAGE,lambda hero : hero.damage_boost(20,20)),("Epic Damage Potion",IMAGE,lambda hero : hero.damage_boost(50,20)),(" Enormous Damage Potion",IMAGE,lambda hero : hero.damage_boost(100,20)))
    POISON_POTION = (("Commune Poison Potion",IMAGE,lambda hero,m : hero.poison_attack(5,m),1),("Rare Poison Potion",IMAGE,lambda hero,m : hero.poison_attack(10,m),1),("Epic Poison Potion",IMAGE,lambda hero,m : hero.poison_attack(20,m),1),("Legendary Poison Potion",IMAGE,lambda hero,m : hero.poison_attack(50,m),1))
    INVISIBILITY_POTION = (("Short Invisibility Potion",IMAGE,lambda hero: hero.invibility(3),1),("Rare Invisibility Potion",IMAGE,lambda hero: hero.invibility(5),1),("Epic Invisibility Potion",IMAGE,lambda hero: hero.invibility(10),1),("Legendary Invisibility Potion",IMAGE,lambda hero: hero.invibility(20),2))
    LIST = [HEALTH_POTION,ARMOR_BOOST_POTION,DAMAGE_BOOST_POTION,INVISIBILITY_POTION,POISON_POTION]#[POISON_POTION]#
    def __init__(self,name,image,effect, durability=1):
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
        self.type = "Potion"
        self.usage = None
        if "Health" in self.name:
            self.usage="Health"
        elif "Armor" in self.name :
            self.usage = "Armor"
        elif "Damage" in self.name:
            self.usage="Damage"
        elif "Poison" in self.name :
            self.usage = "Poison"
        elif "Invisibility" in self.name:
            self.usage="Invisibility"


