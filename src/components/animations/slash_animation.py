import pygame
from math import atan2, pi

from src.components.animations.animation import Animation
from path import ASSETS_DIR
from src.config import Config

vec=pygame.math.Vector2

class SlashAnimation(Animation):
    def __init__(self, user, target, player):
        relative_target_pos = target.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)

        DAGGER_IMAGE_LIST = [pygame.image.load(ASSETS_DIR / ("slash_animation/Sprite-000" + str(i+1) + ".png")).convert_alpha() for i in range(6)]
        
        super().__init__(images=[DAGGER_IMAGE_LIST],
                         speed=[0],
                         delay=[0],
                         frame_duration=[24],
                         coords=[relative_target_pos],
                         directions=[vec(0, 0)],
                         framerate=5,
                         frame_until_damage=7,
                         function = lambda user, user_weapon, target, m, messages: target.damage(int(user_weapon.damage*user.damage_boost), m, player, messages),
                         user=user,
                         target=target)