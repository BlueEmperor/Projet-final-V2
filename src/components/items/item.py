import pygame

vec = pygame.math.Vector2

class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.slot = None
        self.location = None

    def update(self, inventory_topleft, hotbar_topleft):
        if(self.location == "h"):
            self.rect.topleft = vec(88,16)+vec(hotbar_topleft)+self.slot*72
        elif(self.location == "i"):
            self.rect.topleft = vec(322,34)+vec(inventory_topleft)+self.slot*72
    
    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)