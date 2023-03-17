
class Inventory:
    def __init__(self, player) -> None:
        self._inv=[]
        self.size=18
        self.isopen=False
        self.animation=False
        self._player=player

    def add(self, item):
        if(len(self._inv)<self.size):
            self._inv.append(item)
            return(True)
        return(False)

    def delete(self, item):
        self._inv.pop(self._inv.index(item))

    def left_click_event(self, mouse):
        if(self.isopen and not(self.animation)):
            pass
    
    def right_click_event(self, mouse):
        if(self.isopen and not(self.animation)):
            pass

    def draw(self, SCREEN):
        pass