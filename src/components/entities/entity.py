import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,name,pos, health, image_list):
        super().__init__()
        self.name = name
        self.map_pos = pos
        self.health = health
        self.max_health = health
        self.absolute_pos = pos*48
        self.image = image_list[0]
        self.rect = self.image.get_rect()
        self.current_image = 0
        self.ismoving = False
        self.weapon = None
        
    def __repr__(self):
        return(self.name[0])
    
    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)