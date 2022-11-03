from Armes import Weapon
from weapon import LMAR, LMAS, LT


class Vessel:
    def __init__(self,coordinates,maxhits,weapon):
        self.coordinates=coordinates
        self.maxhits=maxhits
        self.weapon=weapon
    def go_to(x,y,z):