import pygame

from PIL import Image
from path import MAP_DIR, ASSETS_DIR
from src.config import Config

vec = pygame.math.Vector2

class Map:
    GROUND = "."
    WALL = "x"
    GROUND_TILE = pygame.image.load(MAP_DIR / "ground" / "27.png").convert_alpha()
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
        self.map = None
        self.map_by_image()
        self.draw_map = self.create_draw_map(self.map)
        print(self)

    def __repr__(self):
        return("\n".join("".join(j for j in i) for i in self.map)+"\n")

    def __contains__(self, coords):
        return(0<=int(coords[1])<len(self.map) and 0<=int(coords[0])<len(self.map[int(coords[1])]))
    
    def map_by_image(self):
        im=Image.open(ASSETS_DIR / "map.png")
        pixel=im.load()
        self.map=[[[] for _ in range(im.size[0])] for _ in range(im.size[1])]
        for i in range(im.size[0]):
            for j in range(im.size[1]):
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
        draw_map = []
        for j in range(len(m)):
            for i in range(len(m[j])): 
                voisins = self.get_voisins(vec(i,j))
                rect = pygame.Rect(0,0, 32,32)
                rect.center=vec(Config.WIDTH/2, Config.HEIGHT/2)+(vec(i,j)-vec(1,1))*48
                if(self.get_item(vec(i,j))==Map.GROUND):
                    draw_map.append([Map.GROUND_TILE, rect])

                elif(voisins[1]==1 and voisins[6]==1 and (voisins[4]==0 or voisins[7]==0)):
                    draw_map.append([Map.RIGHT_WALL_TILE, rect])

                elif(voisins[1]==1 and voisins[6]==1 and (voisins[3]==0 or voisins[5]==0)):
                    draw_map.append([Map.LEFT_WALL_TILE, rect])

                elif(voisins[1]==0):
                    if(voisins[3]==1 and voisins[4]==1):
                        draw_map.append([Map.TOP_WALL_TILE, rect])
                        
                    if(voisins[1]==0 and voisins[3]==0):
                        draw_map.append([Map.EXTERN_CORNER_LEFT_WALL_TILE, rect])
                    
                    elif(voisins[1]==0 and voisins[4]==0):
                        draw_map.append([Map.EXTERN_CORNER_RIGHT_WALL_TILE, rect])
                
                elif(voisins[0]==0 and voisins[1]==1 and voisins[3]==1):
                    draw_map.append([Map.INTERN_CORNER_LEFT_WALL_TILE, rect])

                elif(voisins[2]==0 and voisins[1]==1 and voisins[4]==1):
                    draw_map.append([Map.INTERN_CORNER_RIGHT_WALL_TILE, rect])

                elif(voisins[6]==0):
                    draw_map.append([Map.BOTTOM_WALL_TILE, rect])

                else:
                    draw_map.append([Map.NOT_DEFINED_TILE, rect])
                    
        return(draw_map)

    def update(self):
        pass

    def draw(self, SCREEN):
        for tile in self.draw_map:
            SCREEN.blit(tile[0], tile[1])