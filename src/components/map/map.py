import pygame
import random
from math import cos, sin, pi

from src.components.entities.chest import Chest
from path import MAP_DIR, ASSETS_DIR
from src.config import Config
from src.components.map.node import Node
from src.components.map.room import Room
from src.components.entities.monster import Monster
from src.components.items.wand import Wand
from src.components.items.potions import Potion
from src.components.items.armor import Armor
from src.global_state import GlobalState
from src.status import PlayerStatus
from src.components.entities.entity import Entity
from src.components.animations.stair_animation import StairAnimation
from src.components.UI.stats import StatUI
from src.error import Error

vec = pygame.math.Vector2

class Map:
    DIR={pygame.K_z: vec(0,-1), pygame.K_s: vec(0,1), pygame.K_d: vec(1,0), pygame.K_q: vec(-1,0)}

    GROUND = "."
    WALL = "x"
    STAIR = "E"

    GROUND_TILE = [pygame.image.load(MAP_DIR / "ground" / ("ground"+str(i)+".png")).convert_alpha() for i in range(16)]
    WALL_TILE = pygame.image.load(MAP_DIR / "wall.png").convert_alpha()
    STAIR_TILE = pygame.image.load(MAP_DIR / "stair.png").convert_alpha()
    TOP_WALL_TILE = pygame.image.load(MAP_DIR / "top_wall.png").convert_alpha()
    LEFT_WALL_TILE = pygame.image.load(MAP_DIR / "left_wall.png").convert_alpha()
    RIGHT_WALL_TILE = pygame.image.load(MAP_DIR / "right_wall.png").convert_alpha()
    BOTTOM_WALL_TILE = pygame.image.load(MAP_DIR / "bottom_wall.png").convert_alpha()
    INTERN_CORNER_LEFT_WALL_TILE = pygame.image.load(MAP_DIR / "intern_corner_left.png").convert_alpha()
    INTERN_CORNER_RIGHT_WALL_TILE = pygame.image.load(MAP_DIR / "intern_corner_right.png").convert_alpha()
    EXTERN_CORNER_LEFT_WALL_TILE = pygame.image.load(MAP_DIR / "extern_corner_left.png").convert_alpha()
    EXTERN_CORNER_RIGHT_WALL_TILE = pygame.image.load(MAP_DIR / "extern_corner_right.png").convert_alpha()
    RIGHT_FULL_CORNER_TILE = pygame.image.load(MAP_DIR / "right_full_corner.png").convert_alpha()
    LEFT_FULL_CORNER_TILE = pygame.image.load(MAP_DIR / "left_full_corner.png").convert_alpha()
    TOP_FULL_CORNER_TILE = pygame.image.load(MAP_DIR / "top_full_corner.png").convert_alpha()
    BOTTOM_FULL_CORNER_TILE = pygame.image.load(MAP_DIR / "bottom_full_corner.png").convert_alpha()
    DUAL_VERTICAL_WALL_TILE = pygame.image.load(MAP_DIR / "dual_vertical_wall.png").convert_alpha()
    DUAL_INTERN_CORNER_TILE = pygame.image.load(MAP_DIR / "dual_intern_corner.png").convert_alpha()
    LEFT_WALL_AND_CORNER_TILE = pygame.image.load(MAP_DIR / "left_wall_and_corner.png").convert_alpha()
    RIGHT_WALL_AND_CORNER_TILE = pygame.image.load(MAP_DIR / "right_wall_and_corner.png").convert_alpha()
    ATTACK_TILE_BLUE = pygame.image.load(ASSETS_DIR / "attack_tile_blue.png").convert_alpha()
    ATTACK_TILE_RED = pygame.image.load(ASSETS_DIR / "attack_tile_red.png").convert_alpha()
    ATTACK_TILE_LIGHT_BLUE = pygame.image.load(ASSETS_DIR / "attack_tile_light_blue.png").convert_alpha()
    ATTACK_TILE_LIGHT_RED = pygame.image.load(ASSETS_DIR / "attack_tile_light_red.png").convert_alpha()
    HOVER_TILE = pygame.image.load(ASSETS_DIR / "hover_tile.png").convert_alpha()
    NOT_DEFINED_TILE = pygame.image.load(MAP_DIR / "rien.png").convert_alpha()
    DARK_EFFECT = pygame.image.load(ASSETS_DIR / "dark_effect.png").convert_alpha()

    def __init__(self, player, size=50, nbrooms=20):
        self._player = player
        self.map = [[self.WALL]*size for _ in range(size)]
        self.see_map = [[self.WALL]*size for _ in range(size)]
        self.see_map_entities = [[self.WALL]*size for _ in range(size)]
        self.monster_group = pygame.sprite.Group()
        self.box_group = pygame.sprite.Group()
        self.attack_tile = []
        self.nbrooms = nbrooms
        self._roomsToReach = []
        self._rooms = []
        self.generateRooms(nbrooms)
        self.monster_zob()
        self.coffre_zob()
        self.reachAllRooms()
        self._player.teleport(self._rooms[0].center())
        self.put(player,self._rooms[0].center())
        self.tiles_sprites = []
        self.coords_draw = [(max(0,int(self._player.map_pos[0])-Config.WIDTH//96-2),max(0,int(self._player.map_pos[1])-Config.HEIGHT//96-2)),(min(len(self.map[0]),int(self._player.map_pos[0])+Config.WIDTH//96+2),min(len(self.map),int(self._player.map_pos[1])+Config.HEIGHT//96+3))]
        coord = self._rooms[-1].center()
        self.put(Map.STAIR, coord)
        self.create_draw_map(self.map)
        self.monster_group.update(player)
        self.box_group.update(player)
        self.moving_tick = 0
        self.turn = []
        self.update_see_map()
        self.timer = -1
        print(self)

        

    def __repr__(self):
        return("\n".join("".join(str(j) for j in i) for i in self.map)+"\n")

    def __contains__(self, coords):
        return(0<=int(coords[1])<len(self.map) and 0<=int(coords[0])<len(self.map[int(coords[1])]))
    
    def __len__(self):
        return(len(self.map))
    
    
    #--------------------------- Utilities functions --------------------------------
    #Remove the entity in the map
    def rm(self, entity):
        Error.CheckMonster(entity, self)
        self.map[int(entity.map_pos[1])][int(entity.map_pos[0])] = Map.GROUND

    #Put the entity in the map at the coord
    def put(self, entity, coord):
        if(coord in self):
            self.map[int(coord[1])][int(coord[0])]=entity

    #Get the item at the coord
    def get_item(self, coord):
        if(coord in self):
            return(self.map[int(coord[1])][int(coord[0])])
        return(Map.WALL)
    
    #get the room that contains the coord or the element
    def get_room(self, object):
        if isinstance(object,Entity):
            for room in self._rooms:
                if self.pos(object) in room:
                    return room
        else:
            for room in self._rooms:
                if object in room:
                    return room
                
    def get_item_room(self, object):
        room=self.get_room(object)
        items=[]
        for i in range(abs(int(room.c1.x - room.c2.x))):
            for j in range(abs(int(room.c1.y - room.c2.y))):
        #for i in room:
                item = self.get_item(vec(i,j))
                if(isinstance(item, Monster)):
                    items.append(item)
        return items

    #Get the pos of the element
    def pos(self, element):
        for i in range(len(self)):
            for j in range(len(self)):
                if(self.map[j][i]==element):
                    return(vec(i,j))
    
    def move(self, monster, destination):
        Error.is_entity(monster)
        self.rm(monster)
        self.put(monster, destination)
        monster.map_pos=destination

    #--------------------------- Utilities algorithmes functions --------------------------------
    def A_star(self,start_coord,end_coord):
        open=[Node(start_coord,-1,end_coord)]
        close=[]
        current=open[0]
        while(True):
            if(len(open)==0):
                return([])
            
            current=Node.lowest_node(open)
            open.remove(current)
            close.append(current)

            if(current.coord==vec(end_coord)):
                break
            
            for voisin in Node.voisins(current):
                if((voisin.coord != end_coord and self.get_item(voisin.coord)!=self.GROUND) or (voisin.coord in [i.coord for i in close])):
                    continue

                if(not(voisin.coord in [node.coord for node in open]) or voisin.is_shortest(open)):
                    if(not(voisin.coord in [node.coord for node in open])):
                        open.append(voisin)
        
        list=[]
        while(current.parent!=None):
            list.append(current.coord)
            current=current.parent
        return(list[1:])
    
    def line_of_sight(self, coord1, coord2, entity = True):
        list = []
        x1,y1,x2,y2 = coord1[0], coord1[1], coord2[0], coord2[1]
        x,y = x1,y1
        length = abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1))
        dx = (x2-x1)/float(length)
        dy = (y2-y1)/float(length)
        list.append([round(x),round(y)])
        for i in range(int(length)):
            x += dx
            y += dy
            list.append([round(x),round(y)])

        if(entity):
            for i in list:
                if(not(self.map[int(i[1])][int(i[0])] in (Map.GROUND, Map.STAIR) or i in (coord1,coord2))):
                    return(False)
        
        else:
            for i in list:
                if(self.map[int(i[1])][int(i[0])] == Map.WALL and not(i in (coord1,coord2))):
                    return(False)
                
        return(True)
    
    
    def create_attack_zone(self, coord, weapon):
        if(isinstance(weapon, (Potion, Armor))):
           return
        
        self.attack_tile = []
        if(weapon.attack_type == "linear"):
            for i in range(4):
                for j in range(int(weapon.range[0]), int(weapon.range[1])+1):
                    c = vec(round(sin(pi/2*i)*j+coord[0]),round(cos(pi/2*i)*j+coord[1]))
                    item = self.get_item(c)
                    if(vec(c) in self and item != Map.WALL and self.see_map[int(c[1])][int(c[0])] != Map.WALL):
                        if(self.line_of_sight(c, coord)):
                            if(item in (Map.GROUND, Map.STAIR)):
                                self.attack_tile.append((c,Map.ATTACK_TILE_BLUE))
                            else:
                                self.attack_tile.append((c,Map.ATTACK_TILE_RED))
                        
                        else:
                            if(item in (Map.GROUND, Map.STAIR) or self.see_map_entities[int(c[1])][int(c[0])] == Map.WALL):
                                self.attack_tile.append((c,Map.ATTACK_TILE_LIGHT_BLUE))
                            else:
                                self.attack_tile.append((c,Map.ATTACK_TILE_LIGHT_RED))

        elif(weapon.attack_type == "zone"):
            for i in range(int(-weapon.range[1]), int(weapon.range[1]+1)):
                for j in range(int(-weapon.range[1]), int(weapon.range[1]+1)):
                    c = vec(i+coord[0], j+coord[1])
                    if(c in self and self.get_item(c) != Map.WALL and self.see_map[int(c[1])][int(c[0])] != Map.WALL):
                        diff = c - coord
                        if(weapon.range[0]<=abs(diff[0])+abs(diff[1])<=weapon.range[1]):
                            item = self.get_item(c)
                            if(vec(c) in self and item != Map.WALL):
                                if(self.line_of_sight(c, coord)):
                                    if(item in (Map.GROUND, Map.STAIR)):
                                        self.attack_tile.append((c,Map.ATTACK_TILE_BLUE))
                                    else:
                                        self.attack_tile.append((c,Map.ATTACK_TILE_RED))
                                
                                else:
                                    if(item in (Map.GROUND, Map.STAIR) or self.see_map_entities[int(c[1])][int(c[0])] == Map.WALL):
                                        self.attack_tile.append((c,Map.ATTACK_TILE_LIGHT_BLUE))
                                    else:
                                        self.attack_tile.append((c,Map.ATTACK_TILE_LIGHT_RED))
                                


        elif (weapon.attack_type==None):
            for i in range(4):
                for j in range(int(weapon.range[0]), int(weapon.range[1])+1):
                    c = vec(round(sin(pi/2*i)*j+coord[0]),round(cos(pi/2*i)*j+coord[1]))
                    item = self.get_item(c)
                    if(vec(c) in self and item != Map.WALL):
                        if(item in (Map.GROUND, Map.STAIR)):
                            self.attack_tile.append((c,Map.ATTACK_TILE_BLUE))
                        else:
                            self.attack_tile.append((c,Map.ATTACK_TILE_RED))
                    

                        #if(item == Map.GROUND):
                            #self.attack_tile.append((c,Map.ATTACK_TILE_LIGHT_BLUE))
                        #else:
                            #self.attack_tile.append((c,Map.ATTACK_TILE_LIGHT_RED))
                            
    #--------------------------- Map generation --------------------------------
    def addRoom(self, room):
        self._roomsToReach.append(room)
        for i in range(int(room.c1.x), int(room.c2.x)):
            for j in range(int(room.c1.y), int(room.c2.y)):
                self.map[j][i]=Map.GROUND
        
    
    def findRoom(self, coord):
        for room in self._roomsToReach:
            if(coord in room):
                return(room)
        return(False)
    
    def intersectNone(self, r):
        for room in self._roomsToReach:
            if(r.intersect(room)):
                return(False)
        return(True)
    
    def dig(self, coord):
        if(isinstance(self.get_item(coord), Monster)):
            self.get_item(coord).remove(self.monster_group)
            self.rm(self.get_item(coord))
            
        elif(isinstance(self.get_item(coord), Chest)):
            self.get_item(coord).remove(self.box_group)
            self.rm(self.get_item(coord))

        self.map[int(coord.y)][int(coord.x)] = Map.GROUND
        r=self.findRoom(coord)
        if(r):
            self._rooms.append(r)
            del self._roomsToReach[self._roomsToReach.index(r)]
    
    def corridor(self, start, end):
        dir_x = 1 if(start.x < end.x) else -1
        dir_y = 1 if(start.y < end.y) else -1
        for i in range(int(start.y), int(end.y), dir_y):
            self.dig(vec(start.x,i))

        for i in range(int(start.x), int(end.x+dir_x), dir_x):
            self.dig(vec(i, end.y))
    
    def reach(self):
        self.corridor(random.choice(self._rooms).center(), random.choice(self._roomsToReach).center())

    def reachAllRooms(self):
        self._rooms.append(self._roomsToReach.pop(0))
        while(len(self._roomsToReach)):
            self.reach()
    
    def randRoom(self):
        taille=len(self)
        x1=random.randint(1,taille-3)
        y1=random.randint(1,taille-3)
        largeur=random.randint(5,9)
        hauteur=random.randint(5,9)
        return(Room(vec(x1,y1), vec(min(x1+largeur, taille-1), min(y1+hauteur, taille-1))))
        
    def generateRooms(self, n):
        for _ in range(n):
            r=self.randRoom()
            if(self.intersectNone(r)):
                self.addRoom(r)
        
    
    def monster_zob(self):
        temp = self._roomsToReach[1:]
        for room in temp:
            for _ in range(random.randint(1,3)):
                x=random.randint(room.c1.x,room.c2.x-1)
                y=random.randint(room.c1.y,room.c2.y-1)
                #Try to put the monster in the room until the pos is empty
                while(self.get_item(vec(x,y))!=self.GROUND):
                    x=random.randint(room.c1.x,room.c2.x-1)
                    y=random.randint(room.c1.y,room.c2.y-1)

                monster=Monster(*random.choice(Monster.MONSTER_LIST[self._player.map_level]), vec(x,y)) # type: ignore
                self.put(monster, vec(x,y))
                monster.add(self.monster_group)

    def coffre_zob(self):
        for room in self._roomsToReach:
            for _ in range(random.randint(0,1)):
                x=random.randint(room.c1.x,room.c2.x-1)
                y=random.randint(room.c1.y,room.c2.y-1)

                while(self.get_item(vec(x,y))!=self.GROUND):
                    x=random.randint(room.c1.x,room.c2.x-1)
                    y=random.randint(room.c1.y,room.c2.y-1)
                
                box=Chest(vec(x,y),self._player)
                self.put(box, vec(x,y))
                box.add(self.box_group)



    #--------------------------- Draw map generation --------------------------------
    #Get the neighbors of the tile
    def get_voisins(self, coord):
        L = [vec(-1,-1), vec(0,-1), vec(1,-1), vec(-1,0),vec(0,0), vec(1,0), vec(-1,1), vec(0,1), vec(1, 1)]
        voisins = []
        for i in L:
            voisins.append(1 if(self.get_item(i+coord)==Map.WALL) else 0)
        return(voisins)

    #Create the list of the sprites for the map
    def create_draw_map(self, m):
        class Tile:
            def __init__(self, image, rect):
                self.image = image
                self.rect = rect
            
            def update(self, m, pos):
                self.rect.topleft = (pos[0]*48-m._player.absolute_pos[0]+Config.WIDTH/2-24, pos[1]*48-m._player.absolute_pos[1]+Config.HEIGHT/2-24)

            def draw(self, SCREEN):
                SCREEN.blit(self.image, self.rect)

        for j in range(len(m)):
            L=[]
            for i in range(len(m[j])): 
                voisins = self.get_voisins(vec(i,j))
                rect = pygame.Rect(0,0, 48,48)
                rect.topleft=vec(i,j)*48 # type: ignore
                if(not(self.get_item(vec(i,j)) in (Map.WALL, Map.STAIR))):
                    L.append(Tile(random.choice(Map.GROUND_TILE), rect))
                
                elif(self.get_item(vec(i,j)) == Map.STAIR):
                    L.append(Tile(Map.STAIR_TILE, rect))

                elif(voisins==[1]*9):
                    L.append(None)

                elif(voisins[7]==0):
                    L.append(Tile(Map.BOTTOM_WALL_TILE, rect))
                
                elif((voisins[3]==0 or voisins[6]==0) and (voisins[5]==0 or voisins[8]==0)):
                    if(voisins[1]==0):
                        L.append(Tile(Map.TOP_FULL_CORNER_TILE, rect))
                    else:
                        L.append(Tile(Map.DUAL_VERTICAL_WALL_TILE, rect))

                elif(voisins[1]==0):
                    if((voisins[0]==0 and voisins[3]==0) or voisins[6]==0):
                        L.append(Tile(Map.EXTERN_CORNER_LEFT_WALL_TILE, rect))

                    elif((voisins[2]==0 and voisins[5]==0) or voisins[8]==0):
                        L.append(Tile(Map.EXTERN_CORNER_RIGHT_WALL_TILE, rect))
                    
                    else:
                        L.append(Tile(Map.TOP_WALL_TILE, rect))

                elif(voisins[3]==0 or voisins[6]==0):
                    if(voisins[2]==0):
                        L.append(Tile(Map.LEFT_WALL_AND_CORNER_TILE, rect))

                    else:
                        L.append(Tile(Map.LEFT_WALL_TILE, rect))

                elif(voisins[5]==0 or voisins[8]==0):
                    if(voisins[0]==0):
                        L.append(Tile(Map.RIGHT_WALL_AND_CORNER_TILE, rect))

                    else:
                        L.append(Tile(Map.RIGHT_WALL_TILE, rect))
                
                elif(voisins[1]==1):
                    if(voisins[0]==0 and voisins[2]==0):
                        L.append(Tile(Map.DUAL_INTERN_CORNER_TILE, rect))

                    elif(voisins[0]==0):
                        L.append(Tile(Map.INTERN_CORNER_LEFT_WALL_TILE, rect))

                    elif(voisins[2]==0):
                        L.append(Tile(Map.INTERN_CORNER_RIGHT_WALL_TILE, rect))

                else:
                    L.append(Tile(Map.NOT_DEFINED_TILE, rect))
                
                if(L[-1] != None):
                    L[-1].update(self, vec(i, j))
            self.tiles_sprites.append(L)

    def update_see_map(self):
        for i in range(self.coords_draw[0][0], self.coords_draw[1][0]):
            for j in range(self.coords_draw[0][1], self.coords_draw[1][1]):
                if(self.tiles_sprites[j][i]!=None and (vec(i,j) == self._player.map_pos or self.line_of_sight(vec(i,j), self._player.map_pos, False))):
                    self.see_map[j][i] = Map.GROUND
        
        self.see_map_entities = [[self.WALL]*len(self.map) for _ in range(len(self.map))]
        for i in range(self.coords_draw[0][0], self.coords_draw[1][0]):
            for j in range(self.coords_draw[0][1], self.coords_draw[1][1]):
                if(self.tiles_sprites[j][i]!=None and (vec(i,j) == self._player.map_pos or self.line_of_sight(vec(i,j), self._player.map_pos, False))):
                    self.see_map_entities[j][i] = Map.GROUND

    #--------------------------- Events functions --------------------------------
    def left_click_down_event(self, animation, inventory_ui, SCREEN=None, stat_ui = None):
        if stat_ui!=None:
            item = stat_ui.get_self()
        if item==None:
            item = self.get_item(self.mouse_pos)

        if(not(GlobalState.PLAYER_STATE == PlayerStatus.ATTACK)):
            if (isinstance(item,StatUI)):
                item.open_effects(self._player, SCREEN)
            print("not attack")
            return
        

        if(not(isinstance(item,Monster))):
            print("not a monster")
            return
        
        if(not(self._player.can_attack(item, self))):
            print("can't attack")
            return
        
        if(isinstance(self._player.weapon, Wand)):
            if(self._player.mana - self._player.weapon.mana < 0):
                return

            
            self._player.mana -= self._player.weapon.mana

        self._player.effect(self)

        self._player.meet(item, self, animation)


        
        self._player.weapon.durability -= 1
        if self._player.weapon.durability==0:
            inventory_ui.remove(self._player.weapon.slot, self._player.weapon.location)
            
        for monster in self.monster_group:
            self.turn.append(monster)


    def f_down_event(self, inventory_ui):
        item = self.get_item(self.mouse_pos)
        if(isinstance(item, Chest)):
            if(((self._player.map_pos[0]-self.mouse_pos[0])**2+(self._player.map_pos[1]-self.mouse_pos[1])**2)**0.5<=1):
                item.open_chest(self._player, inventory_ui)
        elif (isinstance(item,StatUI)):
            pass


        #elif(isinstance(self._player.weapon,Potion)):
        #    pot = self._player.weapon
         #   self._player.effects.append([pot.effect, pot.turn, pot.usage])
          #  pot.durability -= 1
           # if(pot.durability == 0):
            #    inventory_ui.remove(pot.slot, pot.location)
            #self._player.effect(self)


    #--------------------------- Update functions --------------------------------
    def update(self, animation):
        self.mouse_pos = (vec(pygame.mouse.get_pos())-self._player.rect.topleft+self._player.absolute_pos)//48
        self.timer -= 1
        if(self.timer == 0):
            self.__init__(self._player)
            
        if(self._player.ismoving):
            #Update the visual position of every entities
            self._player.absolute_pos += self._player.ismoving*4
            for i in range(self.coords_draw[0][0], self.coords_draw[1][0]):
                for j in range(self.coords_draw[0][1], self.coords_draw[1][1]):
                    if(self.tiles_sprites[j][i]!=None):
                        self.tiles_sprites[j][i].update(self, vec(i,j))

            self.moving_tick-=1
            if(self.moving_tick==0):
                self._player.ismoving=False
        else:
            if(len(animation) != 0):
                return
        
            if(len(self.turn) != 0):
                while(len(animation) == 0 and len(self.turn) != 0):
                    monster = self.turn.pop(0)
                    if(monster.health > 0):
                        monster.turn_action(self, animation)

                return
            
            if(GlobalState.PLAYER_STATE == PlayerStatus.MOVEMENT):
                #Check if a key is pressed
                keys=pygame.key.get_pressed()
                for key in self.DIR.keys():
                    if(keys[key]):
                        #Check if the player can move
                        if(self.get_item(self._player.map_pos+self.DIR[key])==Map.GROUND):
                            #Is executed at every move of the player
                            self._player.mana += 2
                            if(self._player.max_mana < self._player.mana):
                                self._player.mana = self._player.max_mana

                            self._player.ismoving=self.DIR[key]
                            self.moving_tick = 12
                            
                            #Move the player on the map
                            self.rm(self._player)
                            self._player.map_pos += self.DIR[key]
                            self.put(self._player, self._player.map_pos)

                            self._player.effect(self)

                            for monster in self.monster_group:
                                self.turn.append(monster)
                                if(self.line_of_sight(self._player.map_pos, monster.map_pos)):
                                    monster.aggro = True

                            self.update_see_map()
                            #Update the numbers of the tile to draw
                            self.coords_draw = [(max(0,int(self._player.map_pos[0])-Config.WIDTH//96-2),max(0,int(self._player.map_pos[1])-Config.HEIGHT//96-2)),(min(len(self.map[0]),int(self._player.map_pos[0])+Config.WIDTH//96+2),min(len(self.map),int(self._player.map_pos[1])+Config.HEIGHT//96+3))]
                            return
                        
                        elif(self.get_item(self._player.map_pos+self.DIR[key]) == Map.STAIR):
                            animation.append(StairAnimation(0, 0, 0))
                            self.timer = 65
                            self._player.map_level+=1
                            for i in range(4):
                                Chest.RARITY_CHEST.pop(0)
        self._player.update()
        self.monster_group.update(self._player)
        self.box_group.update(self._player)
        

    #--------------------------- Draw functions --------------------------------
    def draw(self, SCREEN):
        #Draw the map
        for i in range(self.coords_draw[0][0], self.coords_draw[1][0]):
            for j in range(self.coords_draw[0][1], self.coords_draw[1][1]):
                if(self.tiles_sprites[j][i]!=None and self.see_map[j][i] == Map.GROUND):
                    self.tiles_sprites[j][i].draw(SCREEN)


        #Draw attack tiles
        if(GlobalState.PLAYER_STATE == PlayerStatus.ATTACK):
            for tile in self.attack_tile:

                coord = vec(self._player.rect.topleft)-self._player.absolute_pos+tile[0]*48
                SCREEN.blit(tile[1],coord)
        
                if(tile[0] == self.mouse_pos):
                    SCREEN.blit(Map.HOVER_TILE, self.mouse_pos*48-self._player.absolute_pos+self._player.rect.topleft)

        #Draw the monsters
        for monster in self.monster_group:
            monster.draw(SCREEN, self)
        #Draw chest
        for chest in self.box_group:
            chest.draw(SCREEN, self)