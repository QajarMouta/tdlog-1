class DestroyedError(Exception):
    pass

from typing import Tuple
from armes import Armes
from armes import antisurfaces,antiair,torpilles
   


class Vaisseau:
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        self.coordinates=coordinates
        self.maxhits=maxhits
        self.armes=Armes
    def go_to(self,x,y,z):
        self.coordinates = (x,y,z)
    def get_coordinates(self):
        return self.coordinates 
    def fire_at(self,x:int,y:int,z:int):
        if self.maxhits==0:
            raise DestroyedError
        self.armes.fire_at(x,y,z)
        
class Cruiser(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        super.__init__(self,coordinates,6,antiair())
    def go_to(self, x, y, z):
        if z==0:
            super().go_to(x,y,z)
class Submarine(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        super.__init__(self,coordinates,2,torpilles())
    def go_to(self, x, y, z):
        if z==0 or z==-1:
            super().go_to(x,y,z)
class Fregate(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        super.__init__(self,coordinates,5,antisurfaces())
    def go_to(self, x, y, z):
        if z==0 :
            super().go_to(x,y,z)
class Destroyer(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        super.__init__(self,coordinates,4,torpilles())
    def go_to(self, x, y, z):
        if z==0 :
            super().go_to(x,y,z)

class Airfact(Vaisseau):
    def __init__(self,coordinates:Tuple,maxhits:int,armes:Armes):
        super.__init__(self,coordinates,1,antisurfaces())
    def go_to(self, x, y, z):
        if z==1 :
            super().go_to(x,y,z)

class champ_bataille:
    def _init_(self):
        self.vaisseaux=[]
    def ajouter_vaisseau(self,vaisseau):
        joueur=vaisseau.get_coordinates()
        maxhits=vaisseau.maxhits
        for i in self.vaisseaux:
            if i.get_coordinates==joueur:
                return False 
        maxhits+=i.maxhits
        if maxhits>22:
            return False
        self.vaisseaux.append(vaisseau)
    
    def recevoir(self,x,y,z):
        joueur= (x,y,z)
        for i in self.vaisseaux:
            if i.get_coordinates() ==joueur:
                return True
        return False


    
