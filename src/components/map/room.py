import pygame

vec = pygame.math.Vector2

class Room:
    def __init__(self, c1, c2):
        self.c1=c1
        self.c2=c2
    
    def __repr__(self):
        return(str([self.c1, self.c2]))
        
    def __contains__(self, coord):
        return(self.c1.x <= coord.x <= self.c2.x and self.c1.y <= coord.y <= self.c2.y)

    def center(self):
        return(vec((self.c1.x+self.c2.x)//2, (self.c1.y + self.c2.y)//2))
    
    def intersect(self, room):
        return(room.c1 in self or room.c2 in self or vec(room.c1.x, room.c2.y) in self or vec(room.c2.x, room.c1.y) in self or self.c1 in room or self.c2 in room)