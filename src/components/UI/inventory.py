import pygame

from path import ASSETS_DIR, AUDIO_DIR
from src.config import Config
from src.global_state import GlobalState
from src.status import PlayerStatus
from src.components.items.bow import Bow
from src.components.items.sword import Sword
from src.components.items.wand import Wand
from src.components.items.potions import Potion
vec = pygame.math.Vector2

class InventoryUI:
    SELECTED_SOUND = pygame.mixer.Sound(AUDIO_DIR / "sounds" / "select_sound.mp3")
    SELECTED_SOUND.set_volume(0.08)
    SELECT_IMAGE = pygame.image.load(ASSETS_DIR / "blue_hotbar.png").convert_alpha()

    def __init__(self, player):
        #inventory image and rect
        self.inventory_image = pygame.image.load(ASSETS_DIR / "inventory.png").convert_alpha()
        self.inventory_rect = self.inventory_image.get_rect()
        self.inventory_rect.center = (-Config.WIDTH//2, Config.HEIGHT//2)

        #hotbar image and rect
        self.hotbar_image = pygame.image.load(ASSETS_DIR / "hotbar.png").convert_alpha()
        self.hotbar_rect = self.hotbar_image.get_rect()
        self.hotbar_rect.center = (Config.WIDTH//2, Config.HEIGHT-self.hotbar_rect.center[1])

        #fonts
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 48)
        self.font2 = pygame.font.Font(ASSETS_DIR / "font.ttf", 36)

        self._player = player
    
        self.inventory_group = pygame.sprite.Group()
        self.hotbar_group = pygame.sprite.Group()
        
        #open and close variable
        self.isopen = False
        self.animation = 0
        self.dir = 1

        #hover variable
        self.hover_object = None
        self.hover_coord = vec(0,0)

        #drag variable
        self.drag_item = None
        self.drag_offset = vec(0,0)

        #selected item
        self.select_item = None

        #right clicked item
        self.right_click_item = None
        self.right_click_coord = vec(0,0)

        #select rectangle when hover
        self.select_surface = pygame.Surface((69,69), pygame.SRCALPHA)
        self.select_surface.fill((25,212,255, 100))

    def __repr__(self) -> str:
        return("\n################################################\n\n"+"\n".join("".join(j.name[0] if(j) else "." for j in self._player.inventory[i]) for i in range(len(self._player.inventory)))+"\n\n"+"".join(i.name[0] if(i) else "." for i in self._player.hotbar))
    
    #--------------------------- Utilities functions --------------------------------
    #Return the item at the coord depending on the location
    def get_item(self, coord, location):
        if(location == "i"):
            item = self._player.inventory[int(coord[1])][int(coord[0])]
            return(item)
        elif(location == "h"):
            item = self._player.hotbar[int(coord[0])]
            return(item)
        return(None)
    
    #Put an item in the location without checking if an item was already present
    def put(self, item, coord, location):
        if(item != None):
            item.location = location
            item.slot = coord
            item.kill()
            item.add(self.inventory_group) if(location == "i") else item.add(self.hotbar_group)

        if(location == "i"):
            self._player.inventory[int(coord[1])][int(coord[0])] = item

        elif(location == "h"):
            self._player.hotbar[int(coord[0])] = item
    
    #Replace an item with None on the location
    def remove(self, coord, location) -> None:
        if(location == "i"):
            self._player.inventory[int(coord[1])][int(coord[0])].remove(self.inventory_group)
            self._player.inventory[int(coord[1])][int(coord[0])] = None
        elif(location == "h"):
            self._player.hotbar[int(coord[0])].remove(self.hotbar_group)
            self._player.hotbar[int(coord[0])] = None
            
    #--------------------------- Events functions --------------------------------
    def e_down_event(self):
        #If not in animation
        if(self.animation==0):
            self.animation = 12 #Number of frame of the animation
            self.dir*=(-1) #Invert the direction for the animation
            self.isopen=not(self.isopen) #Invert the state of the inventory
            if(self.drag_item != None):
                self.drag_item.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)
                self.drag_item=None #Remove the drag item
                
            if(self.select_item != None and self.select_item.location == "i"):
                self.select_item=None #Remove the select item
            
            if(self.right_click_item != None and self.right_click_item.location == "i"):
                self.right_click_item = None

    def left_click_down_event(self, m):
        if(self.animation != 0):
            return
        
        if(self.right_click_item == None):
            GlobalState.PLAYER_STATE = PlayerStatus.MOVEMENT
            #Make the select item default to None
            self.select_item = None
            
            #Get the select item with the hover coord
            self.select_item = self.get_item(self.hover_coord, self.hover_object)
            self.drag_item = self.select_item

            self._player.weapon = None
            if(self.drag_item != None and self.drag_item.location == "h"):
                self._player.weapon = self.drag_item
                

            #Set the offset with the mouse
            if(self.drag_item!=None):
                self.drag_offset = vec(pygame.mouse.get_pos())-self.drag_item.rect.topleft
        
        else:
            button_list = []
            if(self.right_click_item.effect != None):
                button_list.append(self.right_click_item.effect)

            if(self.right_click_item.effect == None):
                taille = 1
            else:
                taille = 2

            correct = 0
            if(self.right_click_coord[1]+taille*30 > Config.HEIGHT):
                correct = 30*taille

            for i in range(len(button_list)):
                if(pygame.Rect(self.right_click_coord + vec(0, i*30-correct), (105, 30)).collidepoint(pygame.mouse.get_pos())):
                    button_list[i](self._player, m)
                    self.remove(self.right_click_item.slot, self.right_click_item.location)


            if(pygame.Rect(self.right_click_coord + vec(0, len(button_list)*30-correct), (105, 30)).collidepoint(pygame.mouse.get_pos())):
                self.remove(self.right_click_item.slot, self.right_click_item.location)

            self.right_click_item = None
    
    def left_click_up_event(self, m):
        if(self.drag_item!=None):
            if(self.hover_object != None):
                hover_item = self.get_item(self.hover_coord, self.hover_object)

                #Exchange the 2 items slots
                self.put(hover_item, self.drag_item.slot, self.drag_item.location)
                self.put(self.drag_item, self.hover_coord, self.hover_object)

                self._player.weapon = None
            
            #Update coord of the 2 items
                if(hover_item!=None):
                    hover_item.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)
            
            if(self.drag_item.location == "h"):
                self._player.weapon = self.drag_item
                if(isinstance(self._player.weapon, (Bow, Sword, Wand))):
                    GlobalState.PLAYER_STATE = PlayerStatus.ATTACK # type: ignore
                    m.create_attack_zone(self._player.map_pos, self._player.weapon)

            self.drag_item.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)

            self.drag_item = None

    def right_click_down_event(self):
        if(isinstance(self.get_item(self.hover_coord, self.hover_object), str)):
            return
        
        self.right_click_item = self.get_item(self.hover_coord, self.hover_object)
        self.right_click_coord = pygame.mouse.get_pos()

    def right_click_up_event(self):
        pass

    #--------------------------- update functions --------------------------------
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.hover_object = None
        self.hover_coord = vec(0,0)
        
        #If in animation
        if(self.animation!=0):
            self.animation -= 1
            self.inventory_rect.center=(self.dir*(Config.WIDTH*(self.animation-6)//12), Config.HEIGHT//2)

            #Update inventory items while in animation
            for item in self.inventory_group:
                item.update(self.inventory_rect.topleft, self.hotbar_rect.topleft)
        
        else:
            #If an item is dragged, put his center at the mouse position
            if(self.drag_item!=None):
                self.drag_item.rect.topleft=mouse_pos-self.drag_offset

        #If mouse collide with inventory
        if(self.isopen and self.inventory_rect.collidepoint(mouse_pos)):
            if((vec(mouse_pos)-self.inventory_rect.topleft)[0]>=306):
                #calculate the position in the inventory
                #topleft : (322, 34)
                self.hover_coord = (mouse_pos - vec(322, 34) - vec(self.inventory_rect.topleft))//72
                if(0<=self.hover_coord[1]<len(self._player.inventory) and 0<=self.hover_coord[0]<len(self._player.inventory[0])):
                    self.hover_object = "i"
            
            else:
                #Armor equipment
                pass

        #If mouse collide with hotbar
        elif(self.hotbar_rect.collidepoint(mouse_pos)):
            #calculate the position in the hotbar
            #topleft : (88, 10)
            self.hover_coord = (mouse_pos - vec(88, 16) - vec(self.hotbar_rect.topleft))//72
            if(self.hover_coord[1]==0 and 0<=self.hover_coord[0]<len(self._player.hotbar)):
                self.hover_object = "h"

    #--------------------------- draw functions --------------------------------
    def draw(self, SCREEN):
        #draw hotbar image
        SCREEN.blit(self.hotbar_image, self.hotbar_rect)

        #inventory select rectangle draw in hotbar
        if(self.hover_object == "h"):
            SCREEN.blit(self.select_surface, vec(90, 18) + vec(self.hotbar_rect.topleft) + self.hover_coord*72)
        
        #if not in animation and inventory is open, draw everything
        if(self.isopen or self.animation!=0):
            #draw inventory image
            SCREEN.blit(self.inventory_image, self.inventory_rect)
            
            #inventory select rectangle draw in inventory
            if(self.hover_object == "i"):
                SCREEN.blit(self.select_surface, vec(324, 36) + vec(self.inventory_rect.topleft) + self.hover_coord*72)
            
            #player sprite draw
            SCREEN.blit(self._player.big_image_list[self._player.current_image], self.inventory_rect.topleft+vec(130,210))

            #Draw the information of the select item
            self.draw_select_information(SCREEN)

            #health
            SCREEN.blit(self.font.render(f"{int(self._player.health)}/{int(self._player.max_health)}",True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(60,391))

            #gold
            SCREEN.blit(self.font.render(f"{self._player.gold}",True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(195,391))

            #inventory items draw
            self.inventory_group.draw(SCREEN)
        
        #hotbar items draw
        self.hotbar_group.draw(SCREEN)

        #Draw the dragged item
        if(self.drag_item!=None):
            self.drag_item.draw(SCREEN)
        
        elif(self.select_item!=None):
            #Draw select image if there is not an item dragged
            SCREEN.blit(InventoryUI.SELECT_IMAGE, self.select_item.rect)
        
        if(self.right_click_item!=None):
            L = ["Destroy"]
            correct = 0
            if(self.right_click_item.effect == None):
                taille = 1
            else:
                taille = 2
                L.insert(0, "use")

            if(self.right_click_coord[1]+taille*30 > Config.HEIGHT):
                correct = 30*taille
                
            pygame.draw.rect(SCREEN, (30,30, 30), pygame.Rect(self.right_click_coord + vec(0,-correct), (105, taille*30)))
            for i in range(taille):
                if(pygame.Rect(self.right_click_coord + vec(0, i*30-correct), (105, 30)).collidepoint(pygame.mouse.get_pos())):
                    pygame.draw.rect(SCREEN, (80,80,80), pygame.Rect(self.right_click_coord + vec(0,i*30-correct), (105, 30)))
                SCREEN.blit(self.font2.render(L[i],True,(255, 255, 255)), self.right_click_coord + vec(8, 1+i*30-correct))


    #Draw the information of the select item
    def draw_select_information(self, SCREEN):
        if(self.select_item != None):
            if(isinstance(self.select_item, (Bow, Sword, Wand))):
                SCREEN.blit(self.font2.render("Description : " + str(self.select_item.description),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(330,334))
                SCREEN.blit(self.font2.render("Damage : " + str(self.select_item.damage),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(330,363))
                SCREEN.blit(self.font2.render("Durability : " + str(self.select_item.durability),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(330,392))

            elif (isinstance(self.select_item,Potion)):
                SCREEN.blit(self.font2.render("Description : " + str(self.select_item.description),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(330,334))
                SCREEN.blit(self.font2.render(self.select_item.name + str(self.select_item.effect),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(330,363))
                SCREEN.blit(self.font2.render("Durability : " + str(self.select_item.durability),True,(255, 255, 255)), vec(self.inventory_rect.topleft)+vec(330,392))
