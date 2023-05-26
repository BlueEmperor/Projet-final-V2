import pygame


class Menu:
    def __init__(self,image):
        self.image=image
        self.rect = self.image.get_rect()
        
    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)