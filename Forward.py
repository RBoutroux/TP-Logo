from instruction import Instruction
from Parametre import Parametre

class Forward(Instruction):
    def __init__(self, turtle, distance):
        super().__init__(turtle)
        self.distance = distance
    
    def code(self):
        self.turtle.forward(self.distance.value(self.turtle))

    def replace_parametre(self, dict):
        if isinstance(self.distance, Parametre) and self.distance.nom in dict:
            self.distance = self.distance.instantiate(dict)

    def __str__(self):
        return f"Forward({self.distance})"
