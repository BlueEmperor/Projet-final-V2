import pygame
#from src.components.entities.monster import Monster
#from src.components.entities.coffre import Coffre
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
        self.ismoving = False
        self.moving_tick=0
        self.health = health
        self.max_health = health
        self.weapon = None
        
    def __repr__(self):
        return(self.name[0])
    
    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)

    def meet(self, target, m, animation):
        if(self.weapon.animation != None):
            animation.append(self.weapon.animation(self, target, m._player))
    
    def damage(self, damage, m):
        self.health -= damage
        if(self.health <= 0):
            self.remove(m.monster_group)
            m.rm(self)

    def can_attack(self,entity, m):
        dist=(entity.map_pos-self.map_pos)
        if(self.weapon.attack_type == "linear"):
            m.line_of_sight(entity.map_pos,self.map_pos)
            return((dist[0]==0 or dist[1]==0) and abs(dist[0]+dist[1]) in range(int(self.weapon.range[0]), int(self.weapon.range[1])+1))
        
        elif(self.weapon.attack_type == "zone"):
            m.line_of_sight(entity.map_pos,self.map_pos)
            return(abs(dist[0]+dist[1]) in range(int(self.weapon.range[0]), int(self.weapon.range[1])+1))

        elif (self.weapon.attack_type == "continuous"):

            return True
        
    
    def teleport(self, coord):
        self.map_pos = coord
        self.absolute_pos = coord*48

    
    def heal(self, number):
        if(self.health + number > self.max_health):
            self.health = self.max_health
        else:
            self.health += number