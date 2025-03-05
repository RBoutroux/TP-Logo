import ply.lex as lex 
import ply.yacc as yacc
from sys import argv

# la classe Turtle est dans turtle.py et doit être complétée aussi
from tortue import Turtle

#-------------------------------------------------------------------------------
# analyse lexicale

tokens = (
    'NUMBER',
    'FORWARD',
    'BACKWARD',
    'LEFT',
    'RIGHT',
    'PEN',
    'UP',
    'DOWN',
    'COLOR',
    'COLORVALUE')
# TODO: plein de choses à compléter ici !

#-------------------------------------------------------------------------------
# grammaire
t_FORWARD = r'forward'
t_BACKWARD = r'backward'
t_LEFT = r'left'
t_RIGHT = r'right'
t_PEN = r'pen'
t_UP = r'up'
t_DOWN = r'down'
t_COLOR = r'color'

def t_NUMBER(t):
    r'-?[0-9]+' # on peut aussi écrire r'\d+'
    # initialement t.value est la chaîne de caractères correspondant à 
    # l'expression rationnelle
    t.value = int(t.value) 
    # grâce au typage faible de python c'est maintenant un entier
    # on pourrait aussi traiter l'exception ValueError pour détecter
    # un éventuel débordement de capacité.
    return t

def t_COLORVALUE(t):
    r'\#([0-9a-fA-F]{6})'
    t.value = t.value[1:]
    return t

# caractères à ignorer: ici espaces, tabulations, saut de lignes
t_ignore = " \t\n"

def t_error(t):
    print("Caractère inattendu: ", t.value[0])
    t.lexer.skip(1) # on saute ce caractère et on passe au suivant
# TODO: encore des choses à compléter ici

# ------------------------------------------------------------------------------

# on teste le nombre d'arguments donnés sur la ligne de commande
# la longueur de argv est 1 + ce nombre, la case argv[0] correspondant au nom
# du programme.
if len(argv) != 2:
    print("Utilisation: python logo.py fichier.logo")
    exit(1)

# on lit le fichier complet et on le met dans une chaîne de caractères
finput = open(argv[1], 'r')
program = finput.read()
finput.close()

# maintenant on écrit les résultats dans le fichier dont le nom consiste
# en le nom du fichier logo où l'extension logo a été remplacée par svg
foutput = open(argv[1].rsplit('.', 1)[0] + '.svg', 'w')

# une nouvelle tortue. On lui passe le fichier résultat pour qu'elle puisse
# écrire dedans
turtle = Turtle(foutput)
turtle.hello()

# entête du fichier svg
foutput.write('<?xml version="1.0" standalone="no"?>\n')
foutput.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1/1/DTD/svg11.dtd">\n')
foutput.write('<svg width="1000" height="600" version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
foutput.write('<rect width="100%" height="100%" fill="white"/>')
foutput.write(f'<title>{argv[1]}</title>\n')

# ici on crée le parseur puis on parse la chaîne de caractères program qui contient tout le programme
# logo. 
# TODO: Il faut compléter ici la création puis l'appel au parseur. Attention, on ne lit plus 
# ligne par ligne comme c'était le cas dans la calculatrice.

lexer = lex.lex()

# l'axiome: 
def p_expression(p):
    '''expression : expression expr
                | expr'''
    pass

def p_expr(p):
    '''expr : FORWARD NUMBER
            | BACKWARD NUMBER
            | LEFT NUMBER
            | RIGHT NUMBER
            | PEN UP
            | PEN DOWN
            | COLOR COLORVALUE
    '''
    pass


# gestion minimaliste des erreurs de syntaxe
def p_error(p):
    if p:
        print("Erreur de syntaxe: ", p.value)
    else:
        print("Fin de chaîne inattendue")


# instantiation de l'analyseur syntaxique
parser = yacc.yacc()

parser.parse(program)


# partie finale du fichier svg
foutput.write('</svg>')

# on n'oublie pas de fermer le fichier pour s'assurer que tout ce qui était
# potentiellement en attente d'écriture a été bien écrit.
foutput.close()
