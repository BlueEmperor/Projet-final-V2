import pygame
from math import atan2, pi

from src.components.animations.animation import Animation
from path import ASSETS_DIR
from src.config import Config

vec=pygame.math.Vector2

class RpgAnimation(Animation):
    def __init__(self, user, target, player):
        coord = target.absolute_pos-user.absolute_pos
        distance = (coord[0]**2+coord[1]**2)**0.5
        direction = coord/distance
        fireball_speed = 10
        duration = int(distance/fireball_speed-1) if(int(distance/fireball_speed-1) >= 0) else 0
        relative_user_pos = user.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)
        relative_target_pos = target.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)
        
        FIREBALL_IMAGE_LIST = [pygame.transform.rotate(pygame.image.load(ASSETS_DIR / ("missile.png")).convert_alpha(), (pi/2-atan2(direction[1], direction[0]))*180/pi)]
        EXPLOSION_IMAGE_LIST = [pygame.image.load(ASSETS_DIR / ("Explosion/Sprite-000"+str(i+1)+".png")).convert_alpha() for i in range(10)]
        
        super().__init__(images=[FIREBALL_IMAGE_LIST, EXPLOSION_IMAGE_LIST],
                         speed=[fireball_speed, 0],
                         delay=[0, duration],
                         frame_duration=[duration, 40],
                         coords=[relative_user_pos, relative_target_pos],
                         directions=[direction, vec(0,0)],
                         framerate=4,
                         frame_until_damage=duration,
                         function = lambda user, user_weapon, target, m, messages: target.damage_area(int(user_weapon.damage*user.damage_boost), m, player, messages, 2),
                         user=user,
                         target=target)