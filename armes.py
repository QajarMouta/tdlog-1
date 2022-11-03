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