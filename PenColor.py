from instruction import Instruction
from Parametre import Parametre

class PenColor(Instruction):
    def __init__(self, turtle, color):
        super().__init__(turtle)
        self.color = color

    def code(self):
        self.turtle.set_color(self.color)
    
    def replace_parametre(self, dict):
        if isinstance(self.color, Parametre) and self.color.nom in dict:
            self.color = self.color.instantiate(dict)
    
    def __str__(self):
        return f"PenColor({self.color})"