import pygame

from path import ASSETS_DIR
from src.components.items.item import Item 


class Armor(Item):
    IMAGE=pygame.image.load(ASSETS_DIR / "diamond_plastron.png").convert_alpha()
    WOOD_ARMOR = ("Wood Armor", IMAGE, 15)
    IRON_ARMOR = ("Iron Armor", IMAGE, 30)
    GOLD_ARMOR = ("Gold Armor", IMAGE, 50)
    DIAMOND_ARMOR = ("Diamond Armor", IMAGE, 75)
    LIST = [WOOD_ARMOR, IRON_ARMOR, GOLD_ARMOR,DIAMOND_ARMOR]
    
    def __init__(self,name,image,value):
        super().__init__()
        self.name = name
        self.image = image
        self.value=value
        self.rect = pygame.Rect(0,0,32, 32)
        self.image_icon = pygame.transform.scale(self.image, (32, 32))