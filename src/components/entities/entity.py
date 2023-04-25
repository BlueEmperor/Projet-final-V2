import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,name,pos, image_list, hover_list, health=0):
        super().__init__()
        self.name = name
        self.map_pos = pos
        self.absolute_pos = pos*48
        self.image = image_list[0]
        self.image_list = image_list
        self.hover_list = hover_list
        self.rect = self.image.get_rect()
        self.current_image = 0
        self.ismoving = False
        self.moving_tick=0
        self.health = health
        
    def __repr__(self):
        return(self.name[0])
    
    def draw(self,SCREEN):
        SCREEN.blit(self.image, self.rect)

    def meet(self,other, m):
        if isinstance(other,Entity):
            if (other.health > self.weapon.damage):
                other.health-= self.weapon.damage
            else:
                other.health = 0
                other.kill()
                m.rm(other)
    
    def can_attack(self,entity, m):
        dist=(entity.map_pos-self.map_pos)
        if(self.weapon.attack_type == "linear"):
            return((dist[0]==0 or dist[1]==0) and abs(dist[0]+dist[1]) in range(int(self.weapon.range[0]), int(self.weapon.range[1])+1))
        
        elif(self.weapon.attack_type == "zone"):
            return(abs(dist[0]+dist[1]) in range(int(self.weapon.range[0]), int(self.weapon.range[1])+1))
        return True