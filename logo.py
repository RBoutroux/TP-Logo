import ply.lex as lex 
import ply.yacc as yacc
from sys import argv

# la classe Turtle est dans turtle.py et doit être complétée aussi
from tortue import Turtle
from instruction import Instruction
from Forward import Forward
from Right import Right
from SetPen import SetPen
from PenColor import PenColor
from Heading import Heading
from Xcor import Xcor
from Ycor import Ycor
from Value import IntValue
from Parametre import Parametre
from Procedure import Procedure
from copy import deepcopy

#-------------------------------------------------------------------------------
# analyse lexicale
reserved = {
   'forward' : 'FORWARD',
   'backward' : 'BACKWARD',
   'left' : 'LEFT',
   'right' : 'RIGHT',
   'pen' : 'PEN',
   'up' : 'UP',
   'down' : 'DOWN',
   'color' : 'COLOR',
   'repeat' : 'REPEAT',
   'to' : 'TO',
   'end' : 'END',
   'xcor' : 'XCOR',
   'ycor' : 'YCOR',
   'heading' : 'HEADING'
}

tokens = [
    'NUMBER',
    'COLORVALUE',
    'NOMPROCEDURE',
    'LBRACKET',
    'RBRACKET',
    'PARAMETRE'
] + list(reserved.values())
# TODO: plein de choses à compléter ici !

#-------------------------------------------------------------------------------
# grammaire
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
t_PARAMETRE = r'\:[a-zA-Z_0-9]+'

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
    # t.value = t.value[1:] # on enlève le premier caractère
    return t

def t_NOMPROCEDURE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NOMPROCEDURE') # on regarde si c'est un mot réservé, sinon on met 'NOMPROCEDURE' à la place
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

procedures = {}
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
    '''expression : expr'''
    # une expression à calculer
    for instr in p[1]:
        print("Instruction : ")
        print(instr)
        print("")
        instr.code()

def p_expr(p):
    '''expr : expr expr_repeat
            | expr_repeat'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_expr_repeat(p):
    '''expr_repeat : REPEAT NUMBER LBRACKET expr RBRACKET
            | expr2'''
    p[0] = []
    if len(p) == 2:
        p[0] = p[1]
    else:
        for _ in range(p[2]):
            p[0] += p[4]
        

def p_expr2(p):
    '''expr2 : FORWARD terme
            | BACKWARD terme
            | LEFT terme
            | RIGHT terme
            | PEN UP
            | PEN DOWN
            | PEN COLOR COLORVALUE
            | TO NOMPROCEDURE parametres expr END
            | NOMPROCEDURE valeurs_parametres
    '''
    global procedures
    if p[1] == 'forward':
        p[0] = [Forward(turtle, p[2])]
    elif p[1] == 'backward':
        p[0] = [Forward(turtle, -p[2])]
    elif p[1] == 'left':
        p[0] = [Right(turtle, -p[2])]
    elif p[1] == 'right':
        p[0] = [Right(turtle, p[2])]
    elif p[1] == 'pen':
        if p[2] == 'up':
            p[0] = [SetPen(turtle, False)]
        elif p[2] == 'down':
            p[0] = [SetPen(turtle, True)]
        elif p[2] == 'color':
            p[0] = [PenColor(turtle, p[3])]
    elif p[1] == 'to' and p[2] not in procedures and p[2] not in reserved and p[5] == 'end':
        procedures[p[2]] = Procedure(p[2], p[3], p[4])
        p[0] = []
    elif p[1] in procedures:
        if len(procedures[p[1]].parametres) != len(p[2]):
            print("Nombre de parametres incorrect")
        else:
            dict_parametres = {}
            for i in range(len(procedures[p[1]].parametres)):
                dict_parametres[procedures[p[1]].parametres[i].nom] = p[2][i]

            p[0] = []
            for instr in procedures[p[1]].instructions:
                copied_instr = deepcopy(instr)
                copied_instr.replace_parametre(deepcopy(dict_parametres))  # Remplacement des paramètres
                p[0].append(copied_instr)
    else:
        print("Procedure inconnue")
        p[0] = []

def p_parametres(p):
    '''parametres : parametres terme
            | empty
    '''
    if p[1] == None:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_empty(p):
    'empty :'
    pass

def p_valeurs_parametres(p):
    '''valeurs_parametres : empty
                        | valeurs_parametres terme
    '''
    if p[1] == None:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_terme(p):
    '''terme : NUMBER
            | XCOR
            | YCOR
            | HEADING
            | PARAMETRE
    '''
    if p[1] == 'xcor':
        p[0] = Xcor()
    elif p[1] == 'ycor':
        p[0] = Ycor()
    elif p[1] == 'heading':
        p[0] = Heading()
    elif type(p[1]) is int:
        p[0] = IntValue(p[1])
    elif p[1][0] == ':':
        p[0] = Parametre(p[1])
        

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
