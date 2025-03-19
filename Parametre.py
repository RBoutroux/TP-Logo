from Negated import Negated
from copy import deepcopy

class Parametre(Negated):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom

    def instantiate(self, dict):
        if self.sign == -1:
            return -dict[self.nom]
        return dict[self.nom]

    def __str__(self):
        return f"Parametre({self.nom})"