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
        
    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)