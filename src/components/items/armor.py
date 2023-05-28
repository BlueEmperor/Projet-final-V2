import pygame

from path import ARMOR_DIR
from src.components.items.item import Item 


class Armor(Item):
    #plastrons#
    wood_plastron=pygame.image.load(ARMOR_DIR / "wood_plastron.png").convert_alpha()
    silver_plastron= pygame.image.load(ARMOR_DIR / "silver_plastron.png").convert_alpha()
    golden_plastron=pygame.image.load(ARMOR_DIR / "golden_plastron.png").convert_alpha()
    diamond_plastron= pygame.image.load(ARMOR_DIR / "diamond_plastron.png").convert_alpha()

    WOOD_PLASTRON = ("Wood Armor", wood_plastron, 15)
    SILVER_PLASTRON = ("Silver Armor", silver_plastron, 30)
    GOLDEN_PLASTRON = ("Golden Armor", golden_plastron, 50)
    DIAMOND_PLASTRON = ("Diamond Armor", diamond_plastron, 75)
    PLASTRON_LIST = [WOOD_PLASTRON, SILVER_PLASTRON, GOLDEN_PLASTRON,DIAMOND_PLASTRON] # list des plastrons

    #casques#:
    #wood_helmet=pygame.image.load(ARMOR_DIR / "wood_helmet.png").convert_alpha()
    silver_helmet= pygame.image.load(ARMOR_DIR / "silver_helmet.png").convert_alpha()
    golden_helmet=pygame.image.load(ARMOR_DIR / "golden_helmet.png").convert_alpha()
    diamond_helmet= pygame.image.load(ARMOR_DIR / "diamond_helmet.png").convert_alpha()

    #WOOD_HELMET = ("Wood Armor", wood_helmet, 15)
    SILVER_HELMET = ("Silver Helmet", silver_helmet, 30)
    GOLDEN_HELMET = ("Golden Helmet", golden_helmet, 50)
    DIAMOND_HELMET = ("Diamond Helmet", diamond_helmet, 75)
    HELMET_LIST = [ SILVER_HELMET, GOLDEN_HELMET,DIAMOND_HELMET]

    #jambièèèères#
    wood_legs=pygame.image.load(ARMOR_DIR / "wood_legs.png").convert_alpha()
    silver_legs=pygame.image.load(ARMOR_DIR / "silver_legs.png").convert_alpha()
    golden_legs=pygame.image.load(ARMOR_DIR / "golden_legs.png").convert_alpha()
    diamond_legs=pygame.image.load(ARMOR_DIR / "diamond_legs.png").convert_alpha()

    WOOD_LEGS = ("Wood Legs", wood_legs, 15)
    SILVER_LEGS = ("Silver Legs", silver_legs, 30)
    GOLDEN_LEGS = ("Golden Legs", golden_legs, 50)
    DIAMOND_LEGS = ("Diamond Legs", diamond_legs, 75)
    LEGS_LIST = [WOOD_LEGS, SILVER_LEGS, GOLDEN_LEGS,DIAMOND_LEGS]
    



    LIST=  [HELMET_LIST, PLASTRON_LIST,LEGS_LIST]
    def __init__(self,name,image,value):
        super().__init__()
        self.name = name
        self.image = image
        self.value=value
        self.rect = pygame.Rect(0,0,32, 32)
        self.image_icon = pygame.transform.scale(self.image, (32, 32))