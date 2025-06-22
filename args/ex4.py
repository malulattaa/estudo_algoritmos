""" 
Crie uma função maior_numero que receba vários 
valores e retorne o maior deles 
(sem usar o max, faça na lógica).
"""

def maior_numero(*args):
    comp = args[0]
    for i in args:
        if i >= comp:
            indice = i
            comp = i
    return indice

print(maior_numero(1, 9, 158,  5, 81, 91, 58, 36, 0,56,2))