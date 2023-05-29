import pygame

from path import ASSETS_DIR
class Button(pygame.sprite.Sprite):
    def __init__(self, text, coord, size, function, color):
        super().__init__()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 36)
        self.text = text
        self.coord = coord
        self.size = size
        self.function = function
        self.color = color
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.coord
        self.text = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
    
    def update(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(event.button == 1):
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                        self.function()
    
    def draw(self, SCREEN):
        if(self.rect.collidepoint(pygame.mouse.get_pos())):
            color = (255, 255, 255)
        else:
            color = self.color

        self.image.fill(color)
        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.text, self.text_rect)