import pygame

from src.config import Config
from path import ASSETS_DIR

vec = pygame.math.Vector2

class Animation:
    def __init__(self, images, speed, delay, frame_duration, coords, directions, framerate, frame_until_damage, user, target):
        self.images = images
        self.images_rect = [i[0].get_rect() for i in self.images]
        for i in range(len(self.images_rect)):
            self.images_rect[i].center = coords[i]

        self.speed = speed
        self.delay = delay
        self.frame_duration = frame_duration
        self.directions = directions
        self.framerate = framerate
        self.actual_frame = [0]*len(self.images)
        self.frame_until_damage = frame_until_damage
        self.user = user
        self.target = target

    def update(self):
        i = 0
        while(i < len(self.images)):
            if(self.actual_frame[i] == self.frame_duration[i]):
                self.images.pop(i)
                self.images_rect.pop(i)
                self.speed.pop(i)
                self.delay.pop(i)
                self.frame_duration.pop(i)
                self.directions.pop(i)
                self.actual_frame.pop(i)
            i += 1
            
        for i in range(len(self.delay)):
            if(self.delay[i] != 0):
                self.delay[i] -= 1
            else:
                self.actual_frame[i] += 1
                self.images_rect[i].center += self.directions[i]*self.speed[i]
        
        if(len(self.images) == 0):
            return(True)
        
        return(False)

    def draw(self, SCREEN):
        for i in range(len(self.images)):
            if(self.delay[i] == 0):
                SCREEN.blit(self.images[i][self.actual_frame[i]//self.framerate%len(self.images[i])], self.images_rect[i])