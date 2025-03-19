from instruction import Instruction
from Parametre import Parametre
from copy import deepcopy

class Right(Instruction):
    def __init__(self, turtle, angle):
        super().__init__(turtle)
        self.angle = angle

    def code(self):
        self.turtle.right(self.angle.value(self.turtle))

    def replace_parametre(self, dict):
        if isinstance(self.angle, Parametre) and self.angle.nom in dict:
            self.angle = self.angle.instantiate(dict)

    def __str__(self):
        return f"Right({self.angle})"
    
    # def __deepcopy__(self, memo):
    #     new_instance = super().__deepcopy__(memo)
    #     new_instance.angle = deepcopy(self.angle)
    #     return new_instance