from Negated import Negated
class IntValue(Negated): 
    def __init__(self, coord):
        super().__init__()
        self.coord = coord
    
    def value(self, turtle):
        return self.sign*self.coord