import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.config import Config
from src.components.items.sword import Sword

vec = pygame.math.Vector2

class InventoryUI:
    SELECTED_SOUND = pygame.mixer.Sound(AUDIO_DIR / "sounds" / "select_sound.mp3")
    SELECT_IMAGE = pygame.image.load(ASSETS_DIR / "blue_hotbar.png").convert_alpha()
    SELECTED_SOUND.set_volume(0.08)
    def __init__(self, player):
        self.image = pygame.image.load(ASSETS_DIR / "inventory.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 32)
        self.rect.center = (-Config.WIDTH//2, Config.HEIGHT//2)
        self._player = player
        self.items_sprite_group = pygame.sprite.Group()
        for i in range(12):
            self.add(Sword())
        self.inventory_slot_rect = [[pygame.Rect(vec(215,23)+vec(self.rect.topleft+vec(Config.WIDTH, 0))+vec(i,j)*48, (48,48)) for i in range(len(player.inventory[j]))] for j in range(len(player.inventory))]
        self.isopen = False
        self.animation = 0
        self.direction = 1
        self.offset = 0
        self.hover = None
        self.selected = None
        self.drag = None
        self.delta_drag = vec(0,0)

    def add(self, item):
        slots=self.empty_slots()
        if(len(slots)>0):
            self._player.inventory[int(slots[0][1])][int(slots[0][0])]=item
            item.update(self.rect, self)
            item.add(self.items_sprite_group)
            item.slot = slots[0]
            return(True)
        return(False)

    def replace(self, item, pos):
        self._player.inventory[int(pos[1])][int(pos[0])] = item
        if(item):
            item.slot = pos

    def delete(self, item):
        #self._player.inventory.pop(self._player.inventory.index(item))
        return
        item.remove(self.items_sprite_group)
    
    def empty_slots(self):
        L=[]
        for i in range(len(self._player.inventory)):
            for j in range(len(self._player.inventory[i])):
                if(not(self._player.inventory[i][j])):
                    L.append(vec(j,i))
        return(L)
    
    def K_e_event(self, key):
        if(not(self.animation)):
            self.animation = 16
            if(self.isopen):
                self.direction = -1
            else:
                self.direction = 1
            self.isopen = not(self.isopen)

    def left_click_down_event(self):
        if(self.isopen and not(self.animation)):
            for sprite in self.items_sprite_group:
                if(sprite.rect.collidepoint(pygame.mouse.get_pos())):
                    self.selected = sprite
                    self.drag = sprite
                    self.delta_drag = vec(sprite.rect.topleft) - pygame.mouse.get_pos()
                    InventoryUI.SELECTED_SOUND.play()
                    return
    
    def left_click_up_event(self):
        if(self.drag):
            for i in range(len(self.inventory_slot_rect)):
                for j in range(len(self.inventory_slot_rect[i])):
                    if(self.inventory_slot_rect[i][j].collidepoint(pygame.mouse.get_pos())):
                        self.replace(self._player.inventory[i][j], self.drag.slot)
                        self.replace(self.drag, vec(j,i))
                        self.drag = None
        self.drag = None

    def right_click_down_event(self):
        if(self.isopen and not(self.animation)):
            pass
            
    def update(self):
        if(self.animation != 0):
            self.animation -= 1
            self.rect.topleft += vec(1,0)*Config.WIDTH/16*self.direction

        if((self.isopen or self.animation)):
            if(self.drag):
                self.drag.rect.topleft = pygame.mouse.get_pos()+self.delta_drag
            else:
                self.items_sprite_group.update(self.rect, self)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.topleft[0], self.rect.topleft[1]))
        if(self.isopen or (self.animation)):
            SCREEN.blit(self._player.image, (self.rect.topleft[0]+87, self.rect.topleft[1]+140))
            #health
            SCREEN.blit(self.font.render(str(self._player.health)+"/"+str(self._player.max_health),True,(255, 255, 255)), (self.rect.topleft[0]+40, self.rect.topleft[1]+260))
            #gold
            SCREEN.blit(self.font.render(str(self._player.gold),True,(255, 255, 255)), (self.rect.topleft[0]+130, self.rect.topleft[1]+260))

            #sword
            self.items_sprite_group.draw(SCREEN)
            
            if(self.selected):
                SCREEN.blit(InventoryUI.SELECT_IMAGE, self.selected.rect)