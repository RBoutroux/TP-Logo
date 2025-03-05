from math import sin, cos, pi

#-------------------------------------------------------------------------------
# La classe représentant une tortue avec sa position, son orientation, et le
# statut du crayon (abaissé ou relevé)

# __init__ est le constructeur (par défaut) de la classe
# self joue le rôle de this en Java. Son nom est arbitraire mais standard. Il
# faut le passer explicitement en premier argument de toutes les méthodes en
# Python.

class Turtle:
    def __init__(self, out):
        self.x = 500
        self.y = 300
        self.angle = 0
        self.pendown = True
        self.color = '#1f56d2'
        # self.output représente le fichier SVG dans lequel on écrit
        self.output = out

    def hello(self):
        print(f'Bonjour, je suis une tortue, actuellement en position ({self.x}, {self.y}) !')

    # TODO compléter ici les méthodes de turtle: forward, right, set_pen et set_color
    def forward(self, dist):
        dx = dist * cos(self.angle * pi / 180)
        dy = dist * sin(self.angle * pi / 180)
        if self.pendown:
            self.output.write(f'<line x1 = "{round(self.x)}" y1 = "{round(self.y)}" x2 = "{round(self.x + dx)}" y2 = "{round(self.y + dy)}" style = "stroke:{self.color}"/>\n')
        self.x += dx
        self.y += dy
    
    def right(self, angle):
        self.angle -= angle
    # En particulier dans forward, il faudra faire le tracé si le crayon est baissé avec
    # l'instruction suivante :
    # self.output.write(f'<line x1 = "{round(self.x)}" y1 = "{round(self.y)}" x2 = "{round(self.x + dx)}" y2 = "{round(self.y + dy)}" style = "stroke:{self.color}"/>\n')
