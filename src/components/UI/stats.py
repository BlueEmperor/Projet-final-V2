import pygame

from path import ASSETS_DIR

vec = pygame.math.Vector2

class StatUI:
    STAT_IMAGE = pygame.image.load(ASSETS_DIR / "stats_bar.png").convert_alpha()
    def __init__(self, player):
        self.image = StatUI.STAT_IMAGE
        self.rect = self.image.get_rect()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 32)
        self._player = player

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, [65]*3, pygame.Rect(105,36,225,81))

        #Health
        pygame.draw.rect(SCREEN, (244,45,66), pygame.Rect(105,36,225*self._player.health/self._player.max_health,24))
        SCREEN.blit(self.font.render(f"{int(self._player.health)}/{int(self._player.max_health)}",True,(255, 255, 255)), (110, 37))

        #Mana
        pygame.draw.rect(SCREEN, (53,153,238), pygame.Rect(105,66,210*self._player.mana/self._player.max_mana,24))
        SCREEN.blit(self.font.render(f"{int(self._player.mana)}/{int(self._player.max_mana)}",True,(255, 255, 255)), (110, 67))

        #Experience
        pygame.draw.rect(SCREEN, (139,244,37), pygame.Rect(162,102,157,15))
        SCREEN.blit(self.font.render(f"LV.{int(self._player.level)}",True,(255, 255, 255)), (104, 99))

        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self._player.big_image_list[self._player.current_image], self.rect.topleft+vec(20,23))
