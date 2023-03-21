import pygame

from PIL import Image
from path import MAP_DIR, ASSETS_DIR
from src.config import Config
from random import randint
from src.components.entities.squelette import Squelette

vec = pygame.math.Vector2

class Map:
    DIR={pygame.K_z: vec(0,-1), pygame.K_s: vec(0,1), pygame.K_d: vec(1,0), pygame.K_q: vec(-1,0)}
    GROUND = "."
    WALL = "x"
    GROUND_TILE = [pygame.image.load(MAP_DIR / "ground" / ("ground"+str(i)+".png")).convert_alpha() for i in range(15)]
    WALL_TILE = pygame.image.load(MAP_DIR / "wall.png").convert_alpha()
    TOP_WALL_TILE = pygame.image.load(MAP_DIR / "top_wall" / "14.png").convert_alpha()
    LEFT_WALL_TILE = pygame.image.load(MAP_DIR / "left_wall" / "53.png").convert_alpha()
    RIGHT_WALL_TILE = pygame.image.load(MAP_DIR / "right_wall" / "01.png").convert_alpha()
    BOTTOM_WALL_TILE = pygame.image.load(MAP_DIR / "bottom_wall" / "20.png").convert_alpha()
    INTERN_CORNER_LEFT_WALL_TILE = pygame.image.load(MAP_DIR / "corners" / "54.png").convert_alpha()
    INTERN_CORNER_RIGHT_WALL_TILE = pygame.image.load(MAP_DIR / "corners" / "04.png").convert_alpha()
    EXTERN_CORNER_LEFT_WALL_TILE = pygame.image.load(MAP_DIR / "corners" / "45.png").convert_alpha()
    EXTERN_CORNER_RIGHT_WALL_TILE = pygame.image.load(MAP_DIR / "corners" / "55.png").convert_alpha()
    NOT_DEFINED_TILE = pygame.image.load(MAP_DIR / "rien.png").convert_alpha()

    def __init__(self, player):
        self._player = player
        self.im = Image.open(ASSETS_DIR / "map.png")
        self.map = [[[] for _ in range(self.im.size[0])] for _ in range(self.im.size[1])]
        self.map_by_image()
        self.tiles_sprites = []
        self.coords_draw = [(max(0,int(self._player.map_pos[0])-Config.WIDTH//96-2),max(0,int(self._player.map_pos[1])-Config.HEIGHT//96-2)),(min(len(self.map[0]),int(self._player.map_pos[0])+Config.WIDTH//96+2),min(len(self.map),int(self._player.map_pos[1])+Config.HEIGHT//96+3))]
        self.create_draw_map(self.map)
        self.moving_tick = 0
        self.monster_group = pygame.sprite.Group()
        Squelette(vec(5,2)).add(self.monster_group)
        Squelette(vec(3,4)).add(self.monster_group)
        

    def __repr__(self):
        return("\n".join("".join(j for j in i) for i in self.map)+"\n")

    def __contains__(self, coords):
        return(0<=int(coords[1])<len(self.map) and 0<=int(coords[0])<len(self.map[int(coords[1])]))

    def map_by_image(self):
        pixel=self.im.load()
        for i in range(self.im.size[0]):
            for j in range(self.im.size[1]):
                if(pixel[i,j]==0):
                    self.put(self.WALL, vec(i,j))
                else:
                    self.put(self.GROUND, vec(i,j))


    def get_item(self, coord):
        if(coord in self):
            return(self.map[int(coord[1])][int(coord[0])])
        return(Map.WALL)

    def put(self, elem, coord):
        if(coord in self):
            self.map[int(coord[1])][int(coord[0])]=elem

    def get_voisins(self, coord):
        L = [vec(-1,-1), vec(0,-1), vec(1,-1), vec(-1,0), vec(1,0), vec(-1,1), vec(0,1), vec(1, 1)]
        voisins = []
        for i in L:
            voisins.append(0 if(self.get_item(i+coord)==Map.GROUND) else 1)
        return(voisins)

    def create_draw_map(self, m):
        class Tile:
            def __init__(self, image, rect):
                self.image = image
                self.rect = rect
            
            def draw(self, SCREEN, m):
                SCREEN.blit(self.image, (self.rect.topleft[0]-m._player.absolute_pos[0]+Config.WIDTH/2-24, self.rect.topleft[1]-m._player.absolute_pos[1]+Config.HEIGHT/2-24))

        for j in range(len(m)):
            L=[]
            for i in range(len(m[j])): 
                voisins = self.get_voisins(vec(i,j))
                rect = pygame.Rect(0,0, 48,48)
                rect.topleft=vec(i,j)*48
                if(self.get_item(vec(i,j))==Map.GROUND):
                    L.append(Tile(Map.GROUND_TILE[randint(0,14)], rect))

                elif(voisins[1]==1 and voisins[6]==1 and (voisins[4]==0 or voisins[7]==0)):
                    L.append(Tile(Map.RIGHT_WALL_TILE, rect))

                elif(voisins[1]==1 and voisins[6]==1 and (voisins[3]==0 or voisins[5]==0)):
                    L.append(Tile(Map.LEFT_WALL_TILE, rect))

                elif(voisins[1]==0):
                    if(voisins[3]==1 and voisins[4]==1):
                        L.append(Tile(Map.TOP_WALL_TILE, rect))
                        
                    if(voisins[1]==0 and voisins[3]==0):
                        L.append(Tile(Map.EXTERN_CORNER_LEFT_WALL_TILE, rect))
                    
                    elif(voisins[1]==0 and voisins[4]==0):
                        L.append(Tile(Map.EXTERN_CORNER_RIGHT_WALL_TILE, rect))
                
                elif(voisins[0]==0 and voisins[1]==1 and voisins[3]==1):
                    L.append(Tile(Map.INTERN_CORNER_LEFT_WALL_TILE, rect))

                elif(voisins[2]==0 and voisins[1]==1 and voisins[4]==1):
                    L.append(Tile(Map.INTERN_CORNER_RIGHT_WALL_TILE, rect))

                elif(voisins[6]==0):
                    L.append(Tile(Map.BOTTOM_WALL_TILE, rect))

                elif(voisins == [1,1,1,1,1,1,1,1]):
                    L.append(Tile(Map.WALL_TILE, rect))

                else:
                    L.append(Tile(Map.NOT_DEFINED_TILE, rect))
            self.tiles_sprites.append(L)

    def update(self):
        if(not(self._player.ismoving)):
            keys=pygame.key.get_pressed()
            for key in self.DIR.keys():
                if(keys[key]):
                    if(self.get_item(self._player.map_pos+self.DIR[key])==self.GROUND):
                        self._player.ismoving=key
                        self.moving_tick = 12
                        self._player.map_pos += self.DIR[key]
                        self.coords_draw = [(max(0,int(self._player.map_pos[0])-Config.WIDTH//96-2),max(0,int(self._player.map_pos[1])-Config.HEIGHT//96-2)),(min(len(self.map[0]),int(self._player.map_pos[0])+Config.WIDTH//96+2),min(len(self.map),int(self._player.map_pos[1])+Config.HEIGHT//96+3))]
                        return
                    
        else:
            self.monster_groups.update(self._player)
            self._player.absolute_pos += self.DIR[self._player.ismoving]*4
            self.moving_tick-=1
            if(self.moving_tick==0):
                self._player.ismoving=False

    def draw(self, SCREEN):
        for i in range(self.coords_draw[0][0], self.coords_draw[1][0]):
            for j in range(self.coords_draw[0][1], self.coords_draw[1][1]):
                self.tiles_sprites[j][i].draw(SCREEN, self)
        
        self.monster_group.draw(SCREEN)