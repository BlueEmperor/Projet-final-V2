import pygame

vec = pygame.math.Vector2

class Node:
    def __init__(self, coord, g_cost_before, end_coord, parent=None):
        self.g_cost=g_cost_before+1
        self.h_cost=vec.distance_to(end_coord,coord)
        self.total_cost=self.g_cost+self.h_cost
        self.parent=parent
        self.coord=vec(coord)
        self.end_coord=end_coord
    
    def __repr__(self) -> str:
        return(str(self.coord))
    
    def is_shortest(self, open):
        for node in open:
            if(node.coord == self.coord):
                if(node.total_cost<self.total_cost):
                    open.remove(node)
                    open.append(self)
                    return(False)
        return(True)
    
    @staticmethod
    def lowest_node(list):
        Min_Node=list[0]
        for i in list:
            if(i.total_cost<Min_Node.total_cost):
                Min_Node=i
        return(Min_Node)
    
    @staticmethod
    def voisins(current):
        list=[]
        dir=[vec(0,-1), vec(0,1), vec(1,0), vec(-1,0)]
        for i in dir:
            list.append(Node(i+current.coord,current.g_cost,current.end_coord,current))
        return(list)