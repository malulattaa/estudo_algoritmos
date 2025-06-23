""" 
Crie uma função que receba qualquer quantidade de argumentos via *args e retorne apenas os que forem do tipo str.
"""

def string(*args):
    lista = []
    for palavra in args:
        if isinstance(palavra, str):
            lista.append(palavra)
    return lista
        
print(string("maria", 10, 95.5, "oi", 8, "dmndkmkdm"))