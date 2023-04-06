import random

class Element:
    def __init__(self, name, abbrv=None):
        self._name = name
        if(abbrv):
            self._abbrv = abbrv
        else:
            self._abbrv = name[0]

    def __repr__(self):
        return(self._abbrv)
    
    def description(self):
        return("<"+self._name+">")
    
    def meet(self, hero):
        hero.take(self)
        return(True)
        
class Creature(Element):
    def __init__(self,name, hp, abbrv=None, strength = 1):
        super().__init__(name, abbrv)
        self._hp = hp
        self._strength = strength
    
    def description(self):
        return(super().description()+"("+str(self._hp)+")")
    
    def meet(self, other):
        self._hp -= other._strength
        return(self._hp<0)
        
class Hero(Creature):
    def __init__(self,name="Hero", hp=10, abbrv="@", strength = 2):
        super().__init__(name, hp, abbrv, strength)
        self._inventory = []
    
    def description(self):
        return(super().description()+str(self._inventory))
        
    def take(self, elem):
        self._inventory.append(elem)

class Coord:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __eq__(self,other):
        return((self.x,self.y)==(other.x,other.y))
        
    def __repr__(self):
        return("<"+str(self.x)+","+str(self.y)+">")
    
    def __add__(self,other):
        return(Coord(self.x+other.x,self.y+other.y))

class Map:
    ground="."
    wall="w"
    empty=" "
    dir={'z': Coord(0,-1), 's': Coord(0,1), 'd': Coord(1,0), 'q': Coord(-1,0)}
    
    def __init__(self,size=20, hero=None, nbrooms=7):
        self._hero=hero
        if(hero==None):
            self._hero = Hero()
        
        self._mat=[[self.empty]*size for i in range(size)]
        self._elem={}
        self._roomsToReach = []
        self._rooms = []
        self.nbrooms = nbrooms
        self.generateRooms(nbrooms)
        self.reachAllRooms()
        pos=self._rooms[0].center()
        self.put(pos,self._hero)
    
    def __repr__(self):
        return("\n".join("".join(str(j) for j in i) for i in self._mat)+"\n")
    
    def __len__(self):
        return(len(self._mat))
    
    def __contains__(self, item):
        if(type(item)==str):
            return(True in [item in i for i in self._mat])
        elif(isinstance(item,Coord)):
            return(0<=item.x<len(self._mat) and 0<=item.y<len(self._mat))
        return(False)
    
    def get(self, coord):
        self.checkCoord(coord)
        
        return(self._mat[coord.y][coord.x])
    
    def pos(self, element):
        self.checkElement(element)
        
        for i in range(len(self)):
            for j in range(len(self)):
                if(self._mat[j][i]==element):
                    return(Coord(i,j))
    
    def put(self, coord, element):
        self.checkCoord(coord)
        self.checkElement(element)
        
        if(not(self._mat[coord.y][coord.x] == Map.ground)):
            raise ValueError('Incorrect cell')
            
        if(element in self._elem.keys()):
            raise KeyError('Already placed')
            
        self._mat[coord.y][coord.x]=element
        self._elem[element]=coord
    
    def rm(self, coord):
        self.checkCoord(coord)
        self._mat[coord.y][coord.x]=self.ground
        del self._elem[list(self._elem.keys())[list(self._elem.values()).index(coord)]]
    
    def move(self,element,coord):
        pos=self.pos(element)
        if(pos+coord in self):
            if(self.get(pos+coord)==self.ground):
                self.rm(pos)
                self.put(coord+pos,element)
            
            elif(self.get(pos+coord)!=self.empty):
                if(self.get(pos+coord).meet(element)):
                    self.rm(pos+coord)
    
    def addRoom(self, room):
        self._roomsToReach.append(room)
        for i in range(room.c1.x, room.c2.x+1):
            for j in range(room.c1.y, room.c2.y+1):
                self._mat[j][i]=Map.ground
    
    def findRoom(self, coord):
        for room in self._roomsToReach:
            if(coord in room):
                return(room)
        return(False)
    
    def intersectNone(self, r):
        for room in self._roomsToReach:
            if(r.intersect(room)):
                return(False)
        return(True)
    
    def dig(self, coord):
        self._mat[coord.y][coord.x] = Map.ground
        r=self.findRoom(coord)
        if(r):
            self._rooms.append(r)
            del self._roomsToReach[self._roomsToReach.index(r)]
    
    def corridor(self, start, end):
        dir_x = 1 if(start.x < end.x) else -1
        dir_y = 1 if(start.y < end.y) else -1
        for i in range(start.y, end.y, dir_y):
            self.dig(Coord(start.x,i))
        for i in range(start.x, end.x+dir_x, dir_x):
            self.dig(Coord(i, end.y))
    
    def reach(self):
        self.corridor(random.choice(self._rooms).center(), random.choice(self._roomsToReach).center())

    def reachAllRooms(self):
        self._rooms.append(self._roomsToReach.pop(0))
        while(len(self._roomsToReach)):
            self.reach()
    
    def randRoom(self):
        taille=len(self)
        x1=random.randint(0,taille-3)
        y1=random.randint(0,taille-3)
        largeur=random.randint(3,8)
        hauteur=random.randint(3,8)
        return(Room(Coord(x1,y1), Coord(min(x1+largeur, taille-1), min(y1+hauteur, taille-1))))
        
    def generateRooms(self, n):
        for _ in range(n):
            r=self.randRoom()
            if(self.intersectNone(r)):
                self.addRoom(r)
    
    def checkCoord(self, c):
        if(not(isinstance(c, Coord))):
            raise TypeError('Not a Coord')
            
        if(not(c in self)):
            raise IndexError('Out of map coord')
            
    def checkElement(self, c):
        if(not(isinstance(c, Element))):
            raise TypeError('Not a Element')
    
    
    
class Room:
    def __init__(self, c1, c2):
        self.c1=c1
        self.c2=c2
    
    def __repr__(self):
        return(str([self.c1, self.c2]))
        
    def __contains__(self, coord):
        return(self.c1.x <= coord.x <= self.c2.x and self.c1.y <= coord.y <= self.c2.y)
    
    def center(self):
        return(Coord((self.c1.x+self.c2.x)//2, (self.c1.y + self.c2.y)//2))
    
    def intersect(self, room):
        return(room.c1 in self or room.c2 in self or Coord(room.c1.x, room.c2.y) in self or Coord(room.c2.x, room.c1.y) in self or self.c1 in room or self.c2 in room)
    
 	

#test d'appel de checkCoord/CheckElement dans les méthodes
random.seed(42)
m = Map()
m.checkCoord = lambda x : print("Check coord: " + str(x))
m.checkElement = lambda x : print("Check element: " + str(x))
m.get(Coord(0,0))
m.put(Coord(4,1), Element("."))
m.rm(Coord(4,1))
m.pos(m._hero)
