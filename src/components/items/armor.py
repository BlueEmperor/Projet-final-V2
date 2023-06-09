import pygame

from path import ARMOR_DIR
from src.components.items.item import Item 


class Armor(Item):
    #plastrons#

    CHESTPLATE = [("Wood Armor", pygame.image.load(ARMOR_DIR / "wood_plastron.png").convert_alpha(), 30, "Chestplate"),
                  ("Silver Armor", pygame.image.load(ARMOR_DIR / "silver_plastron.png").convert_alpha(), 45,  "Chestplate"),
                  ("Golden Armor", pygame.image.load(ARMOR_DIR / "golden_plastron.png").convert_alpha(), 60,  "Chestplate"),
                  ("Diamond Armor", pygame.image.load(ARMOR_DIR / "diamond_plastron.png").convert_alpha(), 100,  "Chestplate")]
    
    HELMET = [("Wood Armor", pygame.image.load(ARMOR_DIR / "wood_helmet.png").convert_alpha(), 15, "Helmet"),
              ("Silver Helmet", pygame.image.load(ARMOR_DIR / "silver_helmet.png").convert_alpha(), 30, "Helmet"),
              ("Golden Helmet", pygame.image.load(ARMOR_DIR / "golden_helmet.png").convert_alpha(), 40, "Helmet"),
              ("Diamond Helmet", pygame.image.load(ARMOR_DIR / "diamond_helmet.png").convert_alpha(), 60, "Helmet")]

    LEGGING = [("Wood Legs", pygame.image.load(ARMOR_DIR / "wood_legs.png").convert_alpha(), 25, "Legging"),
               ("Silver Legs", pygame.image.load(ARMOR_DIR / "silver_legs.png").convert_alpha(), 40, "Legging"),
               ("Golden Legs", pygame.image.load(ARMOR_DIR / "golden_legs.png").convert_alpha(), 55, "Legging"),
               ("Diamond Legs", pygame.image.load(ARMOR_DIR / "diamond_legs.png").convert_alpha(), 80, "Legging")]

    BOOTS = [("Wood Boots", pygame.image.load(ARMOR_DIR / "wood_boot.png").convert_alpha(), 15, "Boot"),
             ("Silver Boots", pygame.image.load(ARMOR_DIR / "silver_boot.png").convert_alpha(), 30, "Boot"),
             ("Golden Boots", pygame.image.load(ARMOR_DIR / "golden_boot.png").convert_alpha(), 40, "Boot"),
             ("Diamond Boots", pygame.image.load(ARMOR_DIR / "diamond_boot.png").convert_alpha(), 60, "Boot")]
    
    LIST =  [CHESTPLATE, HELMET, LEGGING, BOOTS]
    def __init__(self,name,image,defense, category):
        super().__init__()
        self.name = name
        self.image = image
        self.defense = defense
        self.rect = self.image.get_rect()
        self.image_icon = pygame.transform.scale(self.image, (48, 48))
        self.category = category