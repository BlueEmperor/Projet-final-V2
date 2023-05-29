import pygame

from path import ASSETS_DIR
from src.components.UI.button import Button
from src.config import Config
from src.global_state import GlobalState
from src.status import GameStatus

vec = pygame.math.Vector2

class MainMenu:
    def __init__(self):
        self.image = pygame.image.load(ASSETS_DIR / "menu/bugatti_chiron.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Config.WIDTH, Config.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.active = True
        self.buttons = []
        self.buttons.append(Button("Jouer", vec(Config.WIDTH/2, Config.HEIGHT/2-50), vec(200, 50), self.play, (255, 100, 0)))
        self.buttons.append(Button("Quitter", vec(Config.WIDTH/2, Config.HEIGHT/2+50), vec(200, 50), self.quit, (10, 150, 255)))
    
    def play(self):
        GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    def quit(self):
        pygame.quit()
        exit()

    def update(self, events):
        for button in self.buttons:
            button.update(events)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for button in self.buttons:
            button.draw(screen)
    