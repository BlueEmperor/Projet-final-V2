import pygame
import random

from src.message_display import MessageDisplay
from path import ASSETS_DIR

#from src.components.entities.monster import Monster
#from src.components.entities.coffre import Coffre

vec = pygame.math.Vector2

class Entity(pygame.sprite.Sprite):
    def __init__(self,name,pos, image_list, health=0):
        super().__init__()
        self.name = name
        self.map_pos = pos
        self.absolute_pos = pos*48
        self.image = image_list[0]
        self.image_list = image_list
        self.rect = self.image.get_rect()
        self.current_image = 0
        self.actual_frame = random.randint(0,15)
        self.ismoving = False
        self.moving_tick=0
        self.health = health
        self.max_health = health
        self.weapon = None
        self.defense_boost = 1
        self.damage_boost = 1
        self.mana_boost = 1
        self.health_boost = 1
        self.defense = 0

    def __repr__(self):
        return(self.name[0])
    
    def draw(self,SCREEN, m):
        if(m.see_map[int(self.map_pos[1])][int(self.map_pos[0])] == m.GROUND):
            SCREEN.blit(self.image, self.rect)

    def meet(self, target, m, animation):
        if(self.weapon.animation != None):
            animation.append(self.weapon.animation(self, target, m._player))
        #else:
        #    target.health-=self.weapon.damage
    
    def damage(self, damage, m, player, messages):
        X = 100
        damage = int(damage*X/(X + self.defense*self.defense_boost))
        messages.append(MessageDisplay(text = str(damage),
                                       color = (255, 0, 0),
                                       font = pygame.font.Font(ASSETS_DIR / "font.ttf", 48),
                                       top_left_pos = self.rect.center-vec(len(str(damage))*9,0),
                                       start_alpha = 255,
                                       start_speed = vec(random.random()*4-2, 3),
                                       lambda_alpha = lambda alpha: alpha - 4,
                                       lambda_speed = lambda speed: speed - vec(0,0.1),
                                       timer = 60))
        self.health -= damage
        if(self.health <= 0):
            self.remove(m.monster_group)
            m.rm(self)
            player.add_experience(self.xp)

    def can_attack(self,entity, m):
        dist=(entity.map_pos-self.map_pos)
        if(self.weapon.attack_type == "linear"):
            if(m.line_of_sight(entity.map_pos,self.map_pos)):
                return((dist[0]==0 or dist[1]==0) and abs(dist[0]+dist[1]) in range(int(self.weapon.range[0]), int(self.weapon.range[1])+1))
        
        elif(self.weapon.attack_type == "zone"):
            if(m.line_of_sight(entity.map_pos,self.map_pos)):
                return(abs(dist[0]+dist[1]) in range(int(self.weapon.range[0]), int(self.weapon.range[1])+1))

        elif (self.weapon.attack_type == "continuous"):

            return True
        return(False)
        
    
    def teleport(self, coord):
        self.map_pos = coord
        self.absolute_pos = coord*48

    
    def heal(self, number):
        if(self.health + number > self.max_health):
            self.health = self.max_health
        else:
            self.health += number
    
    def damage_area(self, damage, m, player, messages, radius):
        for monster in m.monster_group:
            if((monster.map_pos - self.map_pos).length() <= radius):
                monster.damage(damage, m, player, messages)