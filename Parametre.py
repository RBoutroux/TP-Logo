class Parametre:
    def __init__(self, nom):
        self.nom = nom

    def instantiate(self, dict):
        return dict[self.nom]