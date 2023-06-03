import pygame
from math import atan2, pi

from src.components.animations.animation import Animation
from path import WEAPON_DIR
from src.config import Config

vec=pygame.math.Vector2

class FireShotAnimation(Animation):
    def __init__(self, user, target, player):
        coord = target.absolute_pos-user.absolute_pos
        distance = (coord[0]**2+coord[1]**2)**0.5
        direction = coord/distance
        speed = 0
        #duration = int(distance/fireball_speed-165/2/fireball_speed) if(int(distance/fireball_speed-165/2/fireball_speed) >= 0) else 0
        relative_user_pos = user.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)
        relative_target_pos = target.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)
        IMAGE = [pygame.transform.rotate(pygame.image.load(WEAPON_DIR / "coup_de_feu.png").convert_alpha(), (pi/2-atan2(direction[1], direction[0]))*180/pi)]

        
        super().__init__(images=[IMAGE],
                         speed=[speed],
                         delay=[0],
                         frame_duration=[10],
                         coords=[relative_user_pos+48*direction],
                         directions=[direction],
                         framerate=4,
                         frame_until_damage=0,
                         function = lambda user, user_weapon, target, m, messages: target.damage(int(user_weapon.damage*user.damage_boost), m, player, messages),
                         user=user,
                         target=target)