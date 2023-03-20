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
        self.inventory_image = pygame.image.load(ASSETS_DIR / "inventory.png").convert_alpha()
        self.inventory_rect = self.inventory_image.get_rect()
        self.inventory_rect.center = (-Config.WIDTH//2, Config.HEIGHT//2)

        self.hotbar_image = pygame.image.load(ASSETS_DIR / "hotbar.png").convert_alpha()
        self.hotbar_rect = self.hotbar_image.get_rect()
        self.hotbar_rect.center = (Config.WIDTH//2, self.hotbar_rect.center[1])

        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 48)
        self.font2 = pygame.font.Font(ASSETS_DIR / "font.ttf", 36)

        self._player = player
        self.inventory_sprite_group = pygame.sprite.Group()
        self.hotbar_sprite_group = pygame.sprite.Group()

        self.isopen = False
        self.animation = 0
        self.direction = 1

        self.hover = None
        self.selected = None
        self.drag = None

        self.delta_drag = vec(0,0)
        self.alpha_surface = pygame.Surface((Config.WIDTH, Config.HEIGHT), pygame.SRCALPHA)

    def __repr__(self) -> str:
        return("--------------------------------\n"+"".join("@" if(i) else "." for i in self._player.hotbar)+"\n\n"+"\n".join("".join("@" if(j) else "." for j in self._player.inventory[i]) for i in range(len(self._player.inventory))))
    
    def replace(self, item, pos, hotbar):
        if(hotbar):
            self._player.hotbar[int(pos[0])] = item
        else:
            self._player.inventory[int(pos[1])][int(pos[0])] = item

        if(item):
            item.in_hotbar = hotbar
            item.slot = pos

    def delete(self, item):
        #self._player.inventory.pop(self._player.inventory.index(item))
        return
        item.remove(self.items_sprite_group)
    
    def K_e_event(self, key):
        if(not(self.animation)):
            self.animation = 16
            if(self.isopen):
                self.direction = -1
            else:
                self.direction = 1
            self.isopen = not(self.isopen)

    def left_click_down_event(self):
        #drag and drop
        for sprite in self.hotbar_sprite_group:
            if(sprite.rect.collidepoint(pygame.mouse.get_pos())):
                #stockage du sprite sélectionné
                self.selected = sprite
                self.drag = sprite
                self.delta_drag = vec(sprite.rect.topleft) - pygame.mouse.get_pos()
                #InventoryUI.SELECTED_SOUND.play()
                return

        if(self.isopen and not(self.animation)):
            for sprite in self.inventory_sprite_group:
                if(sprite.rect.collidepoint(pygame.mouse.get_pos())):
                    #stockage du sprite sélectionné
                    self.selected = sprite
                    self.drag = sprite
                    self.delta_drag = vec(sprite.rect.topleft) - pygame.mouse.get_pos()
                    #InventoryUI.SELECTED_SOUND.play()
                    return
                
        self.selected = None
    
    def left_click_up_event(self):
        #drag and drop
        if(self.drag):
            if(self.hover!=None):
                #échange de slot
                if(self.hotbar_rect.collidepoint(pygame.mouse.get_pos())):
                    a=self._player.hotbar[int(self.hover[0])]
                else:
                    a=self._player.inventory[int(self.hover[1])][int(self.hover[0])]
                self.replace(a, self.drag.slot, self.drag.in_hotbar)
                if(a):
                    a.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)
            
                self.replace(self.drag, self.hover, self.hotbar_rect.collidepoint(pygame.mouse.get_pos()))

            self.drag.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)
            self.drag = None
            print(self)
            #print(self._player.hotbar, self._player.inventory)

    def right_click_down_event(self):
        if(self.isopen and not(self.animation)):
            pass
            
    def update(self):
        if(self.animation != 0):
            self.animation -= 1
            self.inventory_rect.topleft += vec(1,0)*(Config.WIDTH/16)*self.direction
            self.inventory_sprite_group.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)

        mouse_pos = pygame.mouse.get_pos()
        
        if(self.drag):
            self.drag.rect.topleft = mouse_pos+self.delta_drag

        if(self.hotbar_rect.collidepoint(mouse_pos)):
            self.hover = (vec(mouse_pos)-(vec(self.hotbar_rect.topleft)+vec(89,11)))//72
            if(not(self.hover[1]==0 and 0<=self.hover[0]<len(self._player.hotbar))):
                self.hover=None


        if((self.isopen or (self.animation))):
            if(self.inventory_rect.collidepoint(mouse_pos)):
                self.hover = (vec(mouse_pos)-(vec(self.inventory_rect.topleft)+vec(323,35)))//72
                if(not(0<=self.hover[1]<len(self._player.inventory) and 0<=self.hover[0]<len(self._player.inventory[int(self.hover[1])]))):
                    self.hover=None
            
            
            
    def draw(self, SCREEN):
        SCREEN.blit(self.inventory_image, vec(self.inventory_rect.topleft))
        SCREEN.blit(self.hotbar_image, vec(self.hotbar_rect.topleft))
        
        #hover tile
        if(self.hover!=None):
            self.alpha_surface.fill((0,0,0,0))
            if(self.hotbar_rect.collidepoint(pygame.mouse.get_pos())):
                pygame.draw.rect(self.alpha_surface, (150,150,150, 100), (vec(self.hotbar_rect.topleft)+vec(89,11)+self.hover*72,(70,70)))
                
            elif(self.inventory_rect.collidepoint(pygame.mouse.get_pos())):
                if((self.isopen  and not(self.animation))):
                    pygame.draw.rect(self.alpha_surface, (150,150,150, 100), (vec(self.inventory_rect.topleft)+vec(324,36)+self.hover*72,(70,70)))
            
            SCREEN.blit(self.alpha_surface, (0,0))

        if(self.selected):
                SCREEN.blit(InventoryUI.SELECT_IMAGE, self.selected.rect.center-vec(37,37))

        if(self.isopen or (self.animation)):
            #player image
            SCREEN.blit(self._player.big_image_list[self._player.current_image], vec(self.inventory_rect.topleft) + vec(87, 140)*1.5)

            #health
            SCREEN.blit(self.font.render(str(self._player.health)+"/"+str(self._player.max_health),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(40, 260)*1.5)

            #gold
            SCREEN.blit(self.font.render(str(self._player.gold),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(130, 260)*1.5)
            
            #draw sprites
            self.inventory_sprite_group.draw(SCREEN)

            if(self.selected):
                SCREEN.blit(InventoryUI.SELECT_IMAGE, self.selected.rect.center-vec(37,37))

                #info display
                #top left : (216, 220)
                SCREEN.blit(self.font2.render("Description : " + str(self.selected.description),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(220,223)*1.5)
                SCREEN.blit(self.font2.render("Damage : " + str(self.selected.damage),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(220,242)*1.5)