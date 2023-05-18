import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Potion(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "potion.png").convert_alpha()
    HEALTH_POTION = (("PCSI Potion",IMAGE,lambda hero: hero.heal(5), 1) ,("Rare health Potion",IMAGE,lambda hero: hero.heal(10), 1), ("Epic Health Potion",IMAGE, lambda hero: hero.heal(20), 2), (" Legendary Health Potion",IMAGE,lambda hero: hero.heal(hero.max_health), 2))
    ARMOR_BOOST_POTION = (("Classic Armor Potion",IMAGE,1,None,10),("Rare Armor Potion",IMAGE,1,None,20),("Epic Armor Potion",IMAGE,1,None,30),("Monstruous Armor Potion",IMAGE,1,None,50))
    DAMAGE_BOOST_POTION = ((" Small Damage Potion",IMAGE,1,None,None,10),(" Rare Damage Potion",IMAGE,1,None,None,50),("Epic Damage Potion",IMAGE,1,None,None,70),(" Enormous Damage Potion",IMAGE,1,None,None,100))
    POISON_POTION = (("Poison Potion",IMAGE,1,None,None,None,5),("Poison Potion",IMAGE,1,None,None,None,10),("Poison Potion",IMAGE,1,None,None,None,20),("Poison Potion",IMAGE,1,None,None,None,50))
    INVISIBILITY_POTION = (("Short Invisibility Potion",IMAGE,1,None,None,None,None,3),("Rare Invisibility Potion",IMAGE,1,None,None,None,None,5),("Epic Invisibility Potion",IMAGE,1,None,None,None,None,10),("Short Invisibility Potion",IMAGE,3,None,None,None,None,15))
    LIST = [HEALTH_POTION]#, ARMOR_BOOST_POTION,DAMAGE_BOOST_POTION,POISON_POTION,INVISIBILITY_POTION]
    def __init__(self,name,image,effect, durability=1):
        super().__init__()
        self.name = name
        self.image = image
        self.image_icon = self.image
        self.effect = effect
        self.rect = pygame.Rect(0,0,32, 32)
        #self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.durability = durability
        self.rarity= None
        self.description = "Une potion magique"


