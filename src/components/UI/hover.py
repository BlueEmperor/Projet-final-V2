import pygame

from path import ASSETS_DIR
from src.components.entities.monster import Monster
from src.components.entities.player import Player
from src.components.entities.chest import Chest
from src.components.items.sword import Sword
from src.components.items.wand import Wand
from src.components.items.potions import Potion
from src.components.items.armor import Armor

vec = pygame.math.Vector2

class Hover:
    HOVER_RECTANGLE = pygame.image.load(ASSETS_DIR / "hover_info.png").convert_alpha()
    HEART_ICON = pygame.image.load(ASSETS_DIR / "heart_icon.png").convert_alpha()
    SWORD_ICON = pygame.image.load(ASSETS_DIR / "sword_icon.png").convert_alpha()
    WAND_ICON = pygame.image.load(ASSETS_DIR / "bdf_staff.png").convert_alpha()
    BOW_ICON = pygame.image.load(ASSETS_DIR / "bow_icon.png").convert_alpha()
    TARGET_ICON = pygame.image.load(ASSETS_DIR / "target_icon.png").convert_alpha()

    def __init__(self, m):
        self._map = m
        self.current_hover = None
        self.image = Hover.HOVER_RECTANGLE
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 36)
        
    def update(self, animation):
        item = self._map.get_item(self._map.mouse_pos)
        if(self.current_hover != None):
            self.current_hover.image=self.current_hover.image_list[0]
        self.current_hover = None
        if(len(animation) != 0):
            return
        
        if(item in (self._map.GROUND, self._map.WALL)):
            return
        
        if(isinstance(item, Player)):
            return
        
        self.current_hover = item
        self.rect.center = self.current_hover.rect.center + vec(0, -85)
        #self._map._player.meet(self.current_hover,self._map)
        #self.current_hover.update(self._map._player)
        self.current_hover.image = self.current_hover.image_list[1]

    def draw(self, SCREEN):
        item = self._map.get_item(self._map.mouse_pos)
        if(self.current_hover != None):
            SCREEN.blit(self.image, self.rect)
            if(isinstance(self.current_hover, Monster)):
                #Name
                name_text = self.font.render(self.current_hover.name,True,(255,255,255))
                name_text_rect = name_text.get_rect()
                name_text_rect.centerx = self.rect.centerx
                name_text_rect.y = self.rect.y + 10
                SCREEN.blit(name_text, name_text_rect)

                #Health
                h = 37
                SCREEN.blit(Hover.HEART_ICON, vec(self.rect.topleft)+vec(15,h))
                pygame.draw.rect(SCREEN, [55]*3, pygame.Rect(self.rect.topleft + vec(50, h+2), vec(125, 21)))
                pygame.draw.rect(SCREEN, (244,45,66), pygame.Rect(self.rect.topleft + vec(50, h+2), vec(125*self.current_hover.health/self.current_hover.max_health, 21)))
                SCREEN.blit(self.font.render(f"{int(self.current_hover.health)}/{int(self.current_hover.max_health)}",True,(255, 255, 255)), self.rect.topleft + vec(55, h))

                #Damage
                h = 70
                SCREEN.blit(Hover.SWORD_ICON, vec(self.rect.topleft)+vec(15,h))
                SCREEN.blit(self.font.render(f"{int(self.current_hover.weapon.damage)}",True,(255, 255, 255)), self.rect.topleft + vec(50, h))

                #Range
                SCREEN.blit(Hover.TARGET_ICON, vec(self.rect.topleft)+vec(90,h))
                SCREEN.blit(self.font.render(" : ".join(str(int(i)) for i in self.current_hover.weapon.range),True,(255, 255, 255)), self.rect.topleft + vec(120, h-2))
            
            elif(isinstance(self.current_hover, Chest)):
                name_text = self.font.render(self.current_hover.name,True,(255,255,255))
                name_text_rect = name_text.get_rect()
                name_text_rect.centerx = self.rect.centerx
                name_text_rect.y = self.rect.y + 10
                SCREEN.blit(name_text, name_text_rect)

                #information:
                h = 37
                phase = 0
                for i in self.current_hover.inventory:
                    #SCREEN.blit(i.image_icon, vec(self.rect.topleft)+vec(50+phase,h))
                    phase += 50
                    if isinstance(i, Potion):
                        SCREEN.blit(self.font.render(f"{(i.usage[0][-1])}",True,(255, 255, 255)), self.rect.topleft + vec(5+phase, h+30))
                        #SCREEN.blit(i.image_icon, vec(self.rect.topleft)+vec(phase,h))
                    elif isinstance(i, Armor):
                        return    
                    else:
                        SCREEN.blit(self.font.render(f"{int(i.damage)}",True,(255, 255, 255)), self.rect.topleft + vec(5+phase, h+30))
                    SCREEN.blit(i.image_icon, vec(self.rect.topleft)+vec(phase,h))