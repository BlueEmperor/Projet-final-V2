import pygame

from path import ASSETS_DIR

vec = pygame.math.Vector2

class StatUI:
    STAT_IMAGE = pygame.image.load(ASSETS_DIR / "stats_bar.png").convert_alpha()
    EFFECTS_IMAGE = pygame.image.load(ASSETS_DIR / "effects_bar.png").convert_alpha()
    OPEN_EFFECTS_IMAGE = pygame.image.load(ASSETS_DIR / "open_effects_bar.png").convert_alpha()
    CLOCK_ICON = pygame.image.load(ASSETS_DIR / "clock_icon.png").convert_alpha()
    def __init__(self, player):
        self.image = StatUI.STAT_IMAGE
        self.image2 = StatUI.EFFECTS_IMAGE
        self.effects_image = StatUI.EFFECTS_IMAGE
        self.open_effects_image = StatUI.OPEN_EFFECTS_IMAGE
        self.rect = self.image.get_rect()
        self.effects_rect = self.effects_image.get_rect()
        self.open_effects_rect = self.open_effects_image.get_rect()
        self.font = pygame.font.Font(ASSETS_DIR / "font.ttf", 32)
        self._player = player
        self.isopen = False
        self.image2_rect = self.image2.get_rect()

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, [55]*3, pygame.Rect(105,36,225,87))

        #Health
        pygame.draw.rect(SCREEN, (244,45,66), pygame.Rect(105,36,225*self._player.health/self._player.max_health,24))
        
        #Mana
        pygame.draw.rect(SCREEN, (53,153,238), pygame.Rect(105,66,210*self._player.mana/self._player.max_mana,24))
        
        #Experience
        pygame.draw.rect(SCREEN, (139,244,37), pygame.Rect(162,102,157*self._player.experience/self._player.experience_to_level_up(),21))

        #Effects 
        #pygame.draw.rect(SCREEN, ()

        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self._player.big_image_list[self._player.current_image], self.rect.topleft+vec(20,20))
        
        #Health
        SCREEN.blit(self.font.render(f"{int(self._player.health)}/{int(self._player.max_health)}",True,(255, 255, 255)), (110, 37))
        
        #Mana
        SCREEN.blit(self.font.render(f"{int(self._player.mana)}/{int(self._player.max_mana)}",True,(255, 255, 255)), (110, 67))
        
        #Experience
        SCREEN.blit(self.font.render(f"LV.{int(self._player.level)}",True,(255, 255, 255)), (104, 102))
        SCREEN.blit(self.font.render(f"{int(self._player.experience)}/{int(self._player.experience_to_level_up())}",True,(255, 255, 255)), (170,102))

        #Effects
        if self.isopen:
            SCREEN.blit(self.image2, vec(self.effects_rect.topleft) + vec(1008,416) )

            SCREEN.blit(self.font.render("EFFECTS:",True,(255, 255, 255)), (1054, 436))
            for i in range (len(self._player.effects)):
                #SCREEN.blit(self.font.render(str(self._player.effects[i][2]),True,(255, 255, 255)), (1000, 500+64*i))
                SCREEN.blit(self.font.render(str(self._player.effects[i][1]) + " tour(s)",True,(255, 255, 255)),(1087, 500+64*i)) #(1150, 500+64*i))
                SCREEN.blit((self.CLOCK_ICON), vec(1047,495+64*i))# 495+64*i))
                SCREEN.blit((self._player.effects[i][3]), vec(1012, 495+64*i))

        else:
            SCREEN.blit(self.image2, vec(self.effects_rect.topleft) + vec(1008,748) )
            for i in range(len(self._player.effects)):
                 SCREEN.blit(self._player.effects[i][3], vec(1020+40*i, 760))
                 
             

    def open_effects(self,player,SCREEN):
        self.isopen = not(self.isopen)



    def get_self(self):
        if vec(1200,800)[0]<=self.image2_rect.bottomright[0]+pygame.mouse.get_pos()[0]:
                if vec(1200,800)[1]<= self.image2_rect.bottomright[1]+pygame.mouse.get_pos()[1]:
                    return self
                return
        return None
    
    def update(self):
        if self.isopen!= True:
              self.image2 = self.effects_image
        else:
             self.image2 = self.open_effects_image
        self.image2_rect = self.image2.get_rect()