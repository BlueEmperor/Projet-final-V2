import pygame
from math import atan2, pi

from src.components.animations.animation import Animation
from path import ASSETS_DIR
from src.config import Config

vec=pygame.math.Vector2

class BowAnimation(Animation):
    def __init__(self, user, target, player):
        coord = target.absolute_pos-user.absolute_pos
        distance = (coord[0]**2+coord[1]**2)**0.5
        direction = coord/distance
        dagger_speed = 10
        duration = int(distance/dagger_speed-2) if(int(distance/dagger_speed-2) >= 0) else 0
        relative_user_pos = user.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)
        
        DAGGER_IMAGE_LIST = [pygame.transform.rotate(pygame.image.load(ASSETS_DIR / ("arrow.png")).convert_alpha(), (pi/2-atan2(direction[1], direction[0]))*180/pi)]
        
        super().__init__(images=[DAGGER_IMAGE_LIST],
                         speed=[dagger_speed],
                         delay=[0],
                         frame_duration=[duration],
                         coords=[relative_user_pos],
                         directions=[direction],
                         framerate=10,
                         frame_until_damage=duration,
                         user=user,
                         target=target)