import random as rd
import matplotlib.pyplot as plt



class Random:
    def __init__(self):
        pass


#exercice 1:

nbr = rd.randint(0, 1)

def gen_congruenciel_lineaire(a, c, m, y0, n):

    for i in range(y0, n):   
        yn = (a * y0 + c) % m
    return yn


def valeurs(a, c, m, y0, n):
    liste = []
    liste.append(y0)
    y = y0

    for i in range(n-1):
        y = (a * y + c) % m
        #y = y / m   #la suite n'est plus aléatoire /!\
        liste.append(y)
    return liste

res  = valeurs(25, 16, 256, 11, 10)
#res_2 = valeurs(843314861, 453816693, 2**31, 1, 10)
print(res)


