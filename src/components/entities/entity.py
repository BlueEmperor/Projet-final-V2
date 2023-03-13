import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,name,coord,absolute_coord, image_list):
        super().__init__()
        self.name = name
        self.map_coord = coord
        self.absolute_coord = absolute_coord
        self.image = image_list[0]
        self.rect = self.image.get_rect()
        self.current_image = 0
        