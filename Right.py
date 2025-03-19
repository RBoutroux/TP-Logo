from instruction import Instruction
from Parametre import Parametre

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