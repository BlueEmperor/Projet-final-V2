import pygame
from math import atan2, pi

from src.components.animations.animation import Animation
from path import ASSETS_DIR, AUDIO_DIR
from src.config import Config

vec=pygame.math.Vector2

class FireballAnimation(Animation):
    def __init__(self, user, target, player):
        coord = target.absolute_pos-user.absolute_pos
        distance = (coord[0]**2+coord[1]**2)**0.5
        direction = coord/distance
        fireball_speed = 5
        duration = int(distance/fireball_speed-165/2/fireball_speed) if(int(distance/fireball_speed-165/2/fireball_speed) >= 0) else 0
        relative_user_pos = user.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)
        relative_target_pos = target.absolute_pos - player.absolute_pos + vec(Config.WIDTH//2, Config.HEIGHT//2)

        
        FIREBALL_IMAGE_LIST = [pygame.transform.rotate(pygame.image.load(ASSETS_DIR / ("Fireball/Sprite-000"+str(i+1)+".png")).convert_alpha(), (pi/2-atan2(direction[1], direction[0]))*180/pi) for i in range(7)]
        EXPLOSION_IMAGE_LIST = [pygame.image.load(ASSETS_DIR / ("Explosion/Sprite-000"+str(i+1)+".png")).convert_alpha() for i in range(10)]
        SOUND = pygame.mixer.Sound(AUDIO_DIR /"sounds/tiim.mp3")
        SOUND.set_volume(0.1)
        SOUND.play()
        
        super().__init__(images=[FIREBALL_IMAGE_LIST, EXPLOSION_IMAGE_LIST],
                         speed=[fireball_speed, 0],
                         delay=[0, duration],
                         frame_duration=[duration, 40],
                         coords=[relative_user_pos, relative_target_pos],
                         directions=[direction, vec(0,0)],
                         framerate=4,
                         frame_until_damage=duration,
                         function = lambda user, user_weapon, target, m, messages: target.damage(int(user_weapon.damage*user.damage_boost), m, player, messages),
                         user=user,
                         target=target,
                         sound=SOUND)