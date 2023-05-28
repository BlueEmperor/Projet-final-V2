import pygame
import random
from path import ASSETS_DIR, AUDIO_DIR
from src.components.UI.inventory import InventoryUI
from src.components.entities.entity import Entity
from src.components.items.sword import Sword
from src.components.items.wand import Wand
from src.components.items.bow import Bow
from src.components.items.potions import Potion
from src.components.items.armor import Armor
from src.components.items.item import Item
from src.components.items.throw_dagger import ThrowableDager
vec = pygame.math.Vector2

class Chest(Entity):
    OPEN_CHEST = [[pygame.image.load(ASSETS_DIR / "chest/open_chest.png").convert_alpha()], [pygame.image.load(ASSETS_DIR / "chest/open_chest_hover.png")]]
    CLOSE_CHEST = [[pygame.image.load(ASSETS_DIR / "chest/close_chest.png").convert_alpha()], [pygame.image.load(ASSETS_DIR / "chest/close_chest_hover.png")]]
    RARITY_CHEST = ["Coffre Commun"]*10 + ["Coffre Rare"]*5 + ["Coffre Epique"]*3 + ["Coffre Legendaire"]
    RARITY_TABLE = {"Coffre Commun":0, "Coffre Rare":1, "Coffre Epique":2, "Coffre Legendaire":3}
    ITEM_LIST = (Sword,Wand,Bow,Potion, ThrowableDager) #Armor
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
        self.RARITY = self.RARITY_CHEST[self.rarity(player)]
        self.RARITY_NUMBER = Chest.RARITY_TABLE[self.RARITY]
        self.name = self.RARITY
        self.inventory_creation()

        #for i in range(random.randint(1,3)):
            #item = random.choice(self.ITEM_LIST)
            #self.inventory.append(item(*random.choice(item.LIST)))


    def rarity(self,player):
        return(random.randint(0,18))
    
    def inventory_creation(self):
        for i in range(2):#(random.randint(2,3)):
            #a=random.randint(0,3)
            item=random.choice(self.ITEM_LIST)
            if item==(Potion):# or Armor):
                b=random.choice(item.LIST)
                #print(a(*b[self.RARITY_NUMBER]))
                self.inventory.append(item(*b[self.RARITY_NUMBER]))
                continue

            
            self.inventory.append(item(*item.LIST[self.RARITY_NUMBER]))


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

    
