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
        if isinstance(self.distance, Parametre) and self.distance.nom in dict:
            self.distance = self.distance.instantiate(dict)

    def __str__(self):
        return f"Forward({self.distance})"
    
    # def __deepcopy__(self, memo):
    #     new_instance = super().__deepcopy__(memo)
    #     new_instance.distance = deepcopy(self.distance)
    #     return new_instance
