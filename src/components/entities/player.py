import pygame

from src.components.entities.entity import Entity
from path import ASSETS_DIR
from src.config import Config

vec = pygame.math.Vector2

class Player(Entity):
    def __init__(self):
        self.image_list = [pygame.image.load(ASSETS_DIR / "player" / ("player" + str(i+1) + ".png")).convert_alpha() for i in range(4)]
        super().__init__("player", vec(2,2), self.image_list)
        self.rect.center=vec(Config.WIDTH/2, Config.HEIGHT/2)
