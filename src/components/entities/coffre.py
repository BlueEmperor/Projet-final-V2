import pygame
import random
from path import ASSETS_DIR, AUDIO_DIR
from src.components.entities.entity import Entity
from src.components.items.sword import Sword
from src.components.items.wand import Wand
from src.components.items.item import Item
vec = pygame.math.Vector2

class Coffre(Entity):
    COFFRE_EZ = [pygame.image.load(ASSETS_DIR / "coffre.png").convert_alpha()]
    HOVER_COFFRE = [pygame.image.load(ASSETS_DIR / "coffre_hover.png").convert_alpha()]
    RARITY_COFFRE = ["Coffre Commun"]*10 + ["Coffre Rare"]*5 + ["Coffre Epique"]*3 + ["Coffre Legendaire"]
    ITEM_LIST = (Sword,Wand)
    def __init__(self,pos, player, open_time=1):
        super().__init__("coffre",pos,Coffre.COFFRE_EZ, Coffre.HOVER_COFFRE)
        self.description = "Un coffre"
        self.inventory=[]
        self.gold = random.randint(1,5)
        self.xp = 0
        self.open_time = open_time
        self.wall_ability = False
        self.isopening = False
        self.RARITY = self.RARITY_COFFRE[self.rarity(player)]
        self.RARITY_NUMBER = 0
        if self.RARITY== "Coffre Commun":
            self.RARITY_NUMBER = 0
        elif self.RARITY=="Coffre Rare":
            self.RARITY_NUMBER = 1
        if self.RARITY== "Coffre Epique":
            self.RARITY_NUMBER = 2
        elif self.RARITY=="Coffre Legendaire":
            self.RARITY_NUMBER = 3
        self.name = self.RARITY
        print (self.RARITY)
        for i in range(random.randint(1,3)):
            item = random.choice(self.ITEM_LIST)
            self.inventory.append(item(*random.choice(item.LIST)))


    def rarity(self,player):
        return(random.randint(0,18))
    
    def inventory_creation(self):
        for i in range(2):#(random.randint(2,3)):
            self.inventory.append(self.ITEM_LIST[random.randint].LIST[self.RARITY_NUMBER])

    
    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
        if self.isopening !=False:
            return
        else: 
            return

    
