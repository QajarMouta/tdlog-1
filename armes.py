class NoAmmunitionError(Exception):
    pass
class OutOfRangeError(Exception):
    pass

class Armes:
    def __init__(self,ammunitions, range):
        self.ammunitions=ammunitions
        self.range=range
    def fire_at(self,x,y,z):
         if self.ammunations == 0:
            raise NoAmmunitionError
         self.ammunitions -=1   

class antisurfaces(Armes):
    def __init__(self,rayon,munitions):
       def __init__(self) -> None:
        super().__init__(40, 30)
        def fire_at(self,x,y,z):
            super().fire_at(x,y,z)
            if z!=0:
                raise OutOfRangeError
                
            
class antiair(Armes):
    def __init__(self,rayon,munitions):
        def __init__(self) -> None:
          super().__init__(50, 40)
        
    def fire_at(self,x,y,z):
            super().fire_at(x,y,z)
            if not z>=0:
                raise OutOfRangeError
             
class torpilles(Armes):
    def __init__(self,rayon,munitions):
        def __init__(self) -> None:
          super().__init__(50, 40)

    def fire_at(self,x,y,z):
            super().fire_at(x,y,z)
            if not z<=0:
                raise OutOfRangeError
                
"""test unitaire"""
if __name__ == "__main__":
    antisurfaces= antisurfaces()
    antiair = antiair()
    torpilles= torpilles()
    antisurfaces.fire_at(0,0,0)
    assert antisurfaces.ammunations == 35
    try:
        antisurfaces.fire_at(2,0,1)
    except:
        assert antisurfaces.ammunations == 34
    antiair.fire_at(1,3,5)
    assert antiair.ammunations == 49
    try:
        antiair.fire_at(0,0,0)
    except:
        assert LMAR.ammunations == 48
    torpilles.fire_at(0,0,0)
    assert torpilles.ammunations == 14
    torpilles.fire_at(0,0,-1)
    assert torpilles.ammunations == 13
    try:
        torpilles.fire_at(0,0,1)
    except:
        assert torpilles.ammunations == 12
