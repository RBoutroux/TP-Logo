from instruction import Instruction
from Parametre import Parametre
from copy import deepcopy

class SetPen(Instruction):
    def __init__(self, turtle, pen):
        super().__init__(turtle)
        self.pen = pen

    def code(self):
        self.turtle.set_pen(self.pen)

    def replace_parametre(self, dict):
        if isinstance(self.pen, Parametre) and self.pen.nom in dict:
            self.pen = self.pen.instantiate(dict)

    def __str__(self):
        return f"SetPen({self.pen})"
    
    # def __deepcopy__(self, memo):
    #     new_instance = super().__deepcopy__(memo)
    #     new_instance.pen = deepcopy(self.pen)
    #     return new_instance