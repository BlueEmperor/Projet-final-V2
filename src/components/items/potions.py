import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.components.items.item import Item

vec = pygame.math.Vector2

class Potion(Item):
    IMAGE = pygame.image.load(ASSETS_DIR / "potion.png").convert_alpha()
    HEALTH_POTION = (("PCSI Potion",IMAGE,1,5) ,("Rare health Potion",IMAGE,1,10), ("Epic Health Potion",IMAGE,1,20), (" Legendary Health Potion",IMAGE,1,True))
    ARMOR_BOOST_POTION = (("Classic Armor Potion",IMAGE,1,None,10),("Rare Armor Potion",IMAGE,1,None,20),("Epic Armor Potion",IMAGE,1,None,30),("Monstruous Armor Potion",IMAGE,1,None,50))
    DAMAGE_BOOST_POTION = ((" Small Damage Potion",IMAGE,1,None,None,10),(" Rare Damage Potion",IMAGE,1,None,None,50),("Epic Damage Potion",IMAGE,1,None,None,70),(" Enormous Damage Potion",IMAGE,1,None,None,100))
    POISON_POTION = (("Poison Potion",IMAGE,1,None,None,None,5),("Poison Potion",IMAGE,1,None,None,None,10),("Poison Potion",IMAGE,1,None,None,None,20),("Poison Potion",IMAGE,1,None,None,None,50))
    INVISIBILITY_POTION = (("Short Invisibility Potion",IMAGE,1,None,None,None,None,3),("Rare Invisibility Potion",IMAGE,1,None,None,None,None,5),("Epic Invisibility Potion",IMAGE,1,None,None,None,None,10),("Short Invisibility Potion",IMAGE,3,None,None,None,None,15))
    LIST = [HEALTH_POTION, ARMOR_BOOST_POTION,DAMAGE_BOOST_POTION,POISON_POTION,INVISIBILITY_POTION]
    def __init__(self,name,image,durability=1,health=None,armorBoost=None,damageBoost=None,poison=None,invisibility=None):
        super().__init__()
        self.name = name
        self.image = image
        self.image_icon = self.image
        #self.image_icon = pygame.transform.scale(self.image, (32, 32))
        self.durability = durability
        self.health = health
        self.armorBoost = armorBoost
        self.damageBoost = damageBoost
        self.poison = poison
        self.rarity= None
        self.description = "Une potion magique"


