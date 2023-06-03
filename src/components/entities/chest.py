import pygame
import random
from path import ASSETS_DIR
from src.components.entities.entity import Entity
from src.components.items.sword import Sword
from src.components.items.wand import Wand
from src.components.items.bow import Bow
from src.components.items.potions import Potion
from src.components.items.armor import Armor
from src.components.items.ak47 import Ak 
from src.components.items.throw_dagger import ThrowableDager
vec = pygame.math.Vector2

class Chest(Entity):
    OPEN_CHEST = [[pygame.image.load(ASSETS_DIR / "chest/open_chest.png").convert_alpha()], [pygame.image.load(ASSETS_DIR / "chest/open_chest_hover.png")]]
    CLOSE_CHEST = [[pygame.image.load(ASSETS_DIR / "chest/close_chest.png").convert_alpha()], [pygame.image.load(ASSETS_DIR / "chest/close_chest_hover.png")]]
    RARITY_CHEST = ["Coffre Commun"]*10 + ["Coffre Rare"]*5 + ["Coffre Epique"]*3 + ["Coffre Legendaire"]
    RARITY_TABLE = {"Coffre Commun":0, "Coffre Rare":1, "Coffre Epique":2, "Coffre Legendaire":3}
    ITEM_LIST = (Sword,Wand,Bow,Potion, ThrowableDager, Armor,Ak)
    def __init__(self,pos, player, open_time=1):
        super().__init__("coffre",pos,self.CLOSE_CHEST[0],health=0)
        self.hover_list = self.CLOSE_CHEST[1]
        self.description = "Un coffre"
        self.inventory=[]
        if self.health==0:
            self.health = None
        self.gold = random.randint(1,5)
        self.xp = 0
        self.open_time = open_time
        self.wall_ability = False
        self.RARITY = self.RARITY_CHEST[self.rarity()]
        self.RARITY_NUMBER = Chest.RARITY_TABLE[self.RARITY]
        self.name = self.RARITY
        self.inventory_creation()

        #for i in range(random.randint(1,3)):
            #item = random.choice(self.ITEM_LIST)
            #self.inventory.append(item(*random.choice(item.LIST)))


    def rarity(self):
        return(random.randint(0,18))
    
    def inventory_creation(self):
        for _ in range(2):
            item = random.choice(Chest.ITEM_LIST)
            if item in (Potion, Armor):
                obj = item(*random.choice(item.LIST)[self.RARITY_NUMBER])
            else:
                obj = item(*item.LIST[self.RARITY_NUMBER])

            self.inventory.append(obj)


    def open_chest(self, player, inventory_ui):
        if self.inventory==[]:
            return
        
        self.image = self.OPEN_CHEST[0][0]
        self.image_list = self.OPEN_CHEST[0]
        self.hover_list = self.OPEN_CHEST[1]
        for i in self.inventory:
            player.add_in_inventory(i, inventory_ui)
        self.inventory = []
        
    def update(self, player):
        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos

    
