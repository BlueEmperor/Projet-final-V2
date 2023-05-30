import pygame

from path import ASSETS_DIR
from src.components.UI.button import Button
from src.config import Config
from src.global_state import GlobalState
from src.status import GameStatus
from src.components.map.map import Map
from src.components.entities.player import Player
from src.components.UI.inventory import InventoryUI
from src.components.UI.stats import StatUI
from src.components.UI.minimap import MiniMap
from src.components.UI.hover import Hover

vec = pygame.math.Vector2

class DeathMenu:
    def __init__(self, m, player, animations, messages, inventory_ui, stat_ui, minimap, hover):
        self.image = pygame.image.load(ASSETS_DIR / "menu/death_menu.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Config.WIDTH, Config.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.active = True
        self.buttons = []
        self.buttons.append(Button("Retry", vec(Config.WIDTH/2, Config.HEIGHT/2-50), vec(200, 50), self.retry, (255, 100, 0)))
        self.buttons.append(Button("Quitter", vec(Config.WIDTH/2, Config.HEIGHT/2+50), vec(200, 50), self.quit, (10, 150, 255)))
        self.m = m
        self.player = player
        self.animations = animations
        self.messages = messages
        self.inventory_ui = inventory_ui
        self.stat_ui = stat_ui
        self.minimap = minimap
        self.hover = hover

    
    def retry(self):
        self.player.__init__()
        self.m.__init__(self.player)
        self.inventory_ui.__init__(self.player)
        self.stat_ui.__init__(self.player)
        self.minimap.__init__(self.m)
        self.hover.__init__(self.m)
        self.messages.clear()
        self.animations.clear()

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
    