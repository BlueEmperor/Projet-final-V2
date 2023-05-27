import pygame

from src.config import Config

class MessageDisplay:
    def __init__(self, text, color, font, top_left_pos, start_alpha, start_speed, lambda_alpha, lambda_speed, timer):
        self.text = text
        self.color = color
        self.font = font
        self.top_left_pos = top_left_pos
        self.alpha = start_alpha
        self.speed = start_speed
        self.lambda_alpha = lambda_alpha
        self.lambda_speed = lambda_speed
        self.timer = timer
        self.text_render = self.font.render(self.text,True,(*self.color,255))
        self.text_rect = self.text_render.get_rect()
        self.surface = pygame.Surface(self.text_rect.size, pygame.SRCALPHA)

    def update(self):
        self.top_left_pos += self.speed
        self.alpha = self.lambda_alpha(self.alpha)
        self.speed = self.lambda_speed(self.speed)
        self.timer -= 1
        if(self.alpha < 0):
            self.alpha = 0
        elif(self.alpha > 255):
            self.alpha = 255

    def draw(self, SCREEN):
        self.surface.fill((0,0,0,0))
        self.surface.blit(self.text_render, (0, 0))
        self.surface.set_alpha(self.alpha)
        SCREEN.blit(self.surface, self.top_left_pos)