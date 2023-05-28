import pygame

from path import ARMOR_DIR
from src.components.items.item import Item 


class Armor(Item):
    #plastrons#

    CHESTPLATE = [("Wood Armor", pygame.image.load(ARMOR_DIR / "wood_plastron.png").convert_alpha(), 15),
                  ("Silver Armor", pygame.image.load(ARMOR_DIR / "silver_plastron.png").convert_alpha(), 30),
                  ("Golden Armor", pygame.image.load(ARMOR_DIR / "golden_plastron.png").convert_alpha(), 50),
                  ("Diamond Armor", pygame.image.load(ARMOR_DIR / "diamond_plastron.png").convert_alpha(), 75)]
    
    HELMET = [("Wood Armor", pygame.image.load(ARMOR_DIR / "wood_helmet.png").convert_alpha(), 15),
              ("Silver Helmet", pygame.image.load(ARMOR_DIR / "silver_helmet.png").convert_alpha(), 30),
              ("Golden Helmet", pygame.image.load(ARMOR_DIR / "golden_helmet.png").convert_alpha(), 50),
              ("Diamond Helmet", pygame.image.load(ARMOR_DIR / "diamond_helmet.png").convert_alpha(), 75)]

    LEGGING = [("Wood Legs", pygame.image.load(ARMOR_DIR / "wood_legs.png").convert_alpha(), 15),
               ("Silver Legs", pygame.image.load(ARMOR_DIR / "silver_legs.png").convert_alpha(), 30),
               ("Golden Legs", pygame.image.load(ARMOR_DIR / "golden_legs.png").convert_alpha(), 50),
               ("Diamond Legs", pygame.image.load(ARMOR_DIR / "diamond_legs.png").convert_alpha(), 75)]
    



    LIST =  [CHESTPLATE, HELMET, LEGGING]
    def __init__(self,name,image,defense):
        super().__init__()
        self.name = name
        self.image = image
        self.defense = defense
        self.rect = self.image.get_rect()
        self.image_icon = pygame.transform.scale(self.image, (48, 48))