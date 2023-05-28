import pygame
from math import atan2, pi

from src.components.animations.animation import Animation
from path import ASSETS_DIR
from src.config import Config
from src.components.entities.monster import Monster

vec=pygame.math.Vector2

class StairAnimation(Animation):
    def __init__(self, user, target, player):
        
        BLACK_HOLE_LIST = [pygame.image.load(ASSETS_DIR / ("animation_escalier/sprite_" + str(i) + ".png")).convert_alpha() for i in range(14)]
        
        super().__init__(images=[BLACK_HOLE_LIST],
                         speed=[0],
                         delay=[0],
                         frame_duration=[140],
                         coords=[vec(Config.WIDTH/2, Config.HEIGHT/2)],
                         directions=[vec(0, 0)],
                         framerate=10,
                         frame_until_damage=0,
                         user=Monster(*Monster.SQUELETTE, vec(0, 0)),
                         target=Monster(*Monster.SQUELETTE, vec(0, 0)))