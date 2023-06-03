import pygame

from path import ASSETS_DIR
from src.components.entities.entity import Entity
from src.components.items.sword import Sword
from src.components.items.wand import Wand


vec=pygame.math.Vector2

class Monster(Entity):
    SQUELETTE = ("Squelette",
                 8,
                 1,
                 Sword(*Sword.SKELETON_SWORD),
                 [[pygame.image.load(ASSETS_DIR / ("entities/squelette/idle/squelette_" + str(i) + ".png")).convert_alpha() for i in range(4)],
                  [pygame.image.load(ASSETS_DIR / ("entities/squelette/idle/squelette_hover_" + str(i) + ".png")).convert_alpha() for i in range(4)]],
                  8,
                  3)
    
    VAMPIRE = ("Vampire",
               15,
               1,
               Wand(*Wand.VAMPIRE_WAND),
               [[pygame.image.load(ASSETS_DIR / ("entities/vampire/idle/vampire_" + str(i) + ".png")).convert_alpha() for i in range(4)],
                [pygame.image.load(ASSETS_DIR / ("entities/vampire/idle/vampire_hover_" + str(i) + ".png")).convert_alpha() for i in range(4)]],
               12,
               10)
    
    SNAKE = ("Snake",
             12,
             1,
             Sword(*Sword.RARE_SWORD),
             [[pygame.image.load(ASSETS_DIR / ("entities/snake/face_snake_"+str(i+1)+".png")).convert_alpha() for i in range (4)],
              [pygame.image.load(ASSETS_DIR / ("entities/snake/face_snake_hover_"+str(i+1)+".png")).convert_alpha() for i in range (4)]],
             15,
             20)
    
    BIG_GUY = ("Big boy",
               50,
               1,
               Sword(*Sword.EPIC_SWORD),
               [[pygame.image.load(ASSETS_DIR/("entities/Big guy/face_big_guy_"+ str(i+1)+ ".png")).convert_alpha() for i in range(4)],
                [pygame.image.load(ASSETS_DIR/("entities/Big guy/face_big_guy_"+ str(i+1)+ ".png")).convert_alpha() for i in range(4)]],
               50,
               50)
    MONSTER_LIST = [SQUELETTE, VAMPIRE,SNAKE, BIG_GUY]
    
    def __init__(self,name,health,speed, weapon, image_list, xp, gold, pos):
        super().__init__(name, pos,image_list[0], health)
        self.hover_list = image_list[1]
        self.speed = speed
        self.weapon = weapon
        self.aggro = False
        self.xp = xp
        self.gold = gold

    def update(self, player):
        if(self.actual_frame == 0):
            self.actual_frame = 15
            self.current_image += 1
            if(self.current_image >= len(self.image_list)):
                self.current_image = 0
            self.image = self.image_list[self.current_image]

        self.actual_frame -= 1

        self.rect.topleft = vec(player.rect.topleft)-player.absolute_pos+self.absolute_pos
        if self.ismoving != False:
            self.absolute_pos += self.ismoving
            self.moving_tick-=1
            if(self.moving_tick==0):
                self.ismoving=False
    
    def move(self,m):
        coord = (self.map_pos-m._player.map_pos)
        if((coord[0]**2+coord[1]**2)**0.5>8 and not(m.line_of_sight(self.map_pos, m._player.map_pos))):
            return
        
        chemin=m.A_star(self.map_pos, m._player.map_pos)
        if(len(chemin) == 0):
            return
        
        m.move(self.map_pos,chemin[-1])
        self.ismoving=(chemin[-1]-self.map_pos)*4
        self.map_pos=chemin[-1]
        self.moving_tick = 12
       
    
    def turn_action(self, m, animation):
        if(self.aggro):
            if self.can_attack(m._player, m):
                self.meet(m._player, m, animation)
            else:
                self.move(m)
