import pygame

class Animation:
    def __init__(self, image_list, frame_per_image, direction, speed, delay, frame_duration, start_coord):
        self.image_list = image_list
        self.image = self.image_list[0]
        self.frame_per_image = frame_per_image
        self.direction = direction
        self.speed = speed
        self.max_frame_duration = frame_duration
        self.actual_frame = 0
        self.coord = start_coord
        self.frame_image = 0
        self.frame = 0
        self.delay = delay

    def update(self):
        if(self.delay != 0):
            self.delay -= 1
            return
        self.actual_frame += 1
        if(self.actual_frame == self.max_frame_duration):
            return
        self.frame += 1
        if(self.frame == self.frame_per_image):
            self.frame = 0
            self.frame_image += 1
            if(self.frame_image == len(self.image_list)):
                self.frame_image = 0
            self.image = self.image_list[self.frame_image]

        self.coord += self.direction*self.speed

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.coord)