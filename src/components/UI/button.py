import pygame

from path import ASSETS_DIR
class Button(pygame.sprite.Sprite):
    def __init__(self, text, coord, size, function):
        super().__init__()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 36)
        self.text = text
        self.coord = coord
        self.size = size
        self.function = function
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.function()
    
    def draw(self, SCREEN):
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.coord
        SCREEN.blit(self.image, self.rect)
        text = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        SCREEN.blit(text, text_rect)