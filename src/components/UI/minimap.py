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

    def m_down_event(self):
        self.open = not(self.open)
    
    def draw(self, SCREEN):
        if(self.open):
            SCREEN.fill((0, 0, 0))
            taille = len(self._map.see_map)
            r = 15
            pygame.draw.rect(SCREEN, [240]*3, pygame.Rect(Config.WIDTH/2-r*taille/2-10, Config.HEIGHT/2-r*taille/2-10, r*taille+20, r*taille+20))
            pygame.draw.rect(SCREEN, (100,70,30), pygame.Rect(Config.WIDTH/2-r*taille/2, Config.HEIGHT/2-r*taille/2, r*taille, r*taille))
            for i in range(taille):
                for j in range(taille):
                    if(self._map.see_map[j][i] == self._map.GROUND and self._map.map[j][i] != self._map.WALL):
                        pygame.draw.rect(SCREEN, (200,150,70), pygame.Rect(Config.WIDTH/2-r*taille/2+i*r, Config.HEIGHT/2-r*taille/2+j*r, r, r)) # type: ignore
            
            pygame.draw.rect(SCREEN, (0, 255, 0), pygame.Rect(Config.WIDTH/2-r*taille/2+self._map._player.map_pos[0]*r, Config.HEIGHT/2-r*taille/2+self._map._player.map_pos[1]*r, r, r))
        else:
            return
            pygame.draw.rect(SCREEN, [220]*3, self.rect)
            pygame.draw.rect(SCREEN, [20]*3, self.rect2)
        