from instruction import Instruction
from Parametre import Parametre
from copy import deepcopy

class Forward(Instruction):
    def __init__(self, turtle, distance):
        super().__init__(turtle)
        self.distance = distance
    
    def code(self):
        self.turtle.forward(self.distance.value(self.turtle))

    def replace_parametre(self, dict):
        print(f"Avant remplacement : {self.distance}")
        if isinstance(self.distance, Parametre) and self.distance.nom in dict:
            self.distance = self.distance.instantiate(dict)
        print(f"Après remplacement : {self.distance}")

    def __str__(self):
        return f"Forward({self.distance})"
