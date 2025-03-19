from Negated import Negated
from copy import deepcopy

class Heading(Negated):
    def __init__(self):
        super().__init__()
        self.direction = 0
    
    def value(self, turtle):
        self.direction = turtle.angle
        return self.sign*self.direction
    
    def __str__(self):
        return f"Heading({self.sign})"