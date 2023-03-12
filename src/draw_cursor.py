import pygame
from path import ASSETS_DIR

cursor = pygame.image.load(ASSETS_DIR / "cursor.png").convert_alpha()
cursor_rect = cursor.get_rect()

def DrawCursor(SCREEN):
    cursor_rect.center = pygame.mouse.get_pos()  # update position 
    SCREEN.blit(cursor, cursor_rect)