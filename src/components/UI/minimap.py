import pygame

from src.config import Config
from src.components.entities.player import Player

vec = pygame.math.Vector2

class MiniMap:
    def __init__(self,m):
        size = 200
        self.rect = pygame.Rect(Config.WIDTH-size, 0, size, size)
        self.rect2 = pygame.Rect(Config.WIDTH-size*19/20, size/20, size*9/10, size*9/10)
        self._map = m
        self.open = False
        self.draw_minimap = self.minimap_init(m)

    def m_down_event(self):
        self.open = not(self.open)
        self.draw_minimap = self.minimap_init(self._map)

    def minimap_init(self, map):
        L = [[None]*len(map) for _ in range(len(map))]
        for i in range(len(map)):
            for j in range(len(map)):
                item = map.get_item(vec(i,j))
                if(item == map.WALL):
                    L[i][j] = (100,70,30) # type: ignore
                
                elif(isinstance(item, Player)):
                    L[i][j] = (0, 255, 0) # type: ignore

                else:
                    L[i][j] = (200,150,70) # type: ignore
        
        return(L)
    
    def draw(self, SCREEN):
        if(self.open):
            SCREEN.fill((0, 0, 0))
            taille = len(self.draw_minimap)
            r = 15
            pygame.draw.rect(SCREEN, [240]*3, pygame.Rect(Config.WIDTH/2-r*taille/2-10, Config.HEIGHT/2-r*taille/2-10, r*taille+20, r*taille+20))
            for i in range(taille):
                for j in range(taille):
                    pygame.draw.rect(SCREEN, self.draw_minimap[i][j], pygame.Rect(Config.WIDTH/2-r*taille/2+i*r, Config.HEIGHT/2-r*taille/2+j*r, r, r)) # type: ignore
        else:
            return
            pygame.draw.rect(SCREEN, [220]*3, self.rect)
            pygame.draw.rect(SCREEN, [20]*3, self.rect2)
        