""" 
Crie uma função chamada somar_numeros que receba 
*args e some apenas os argumentos que forem numéricos
(int ou float). Ignore strings ou outros tipos.
"""

def soma_numeros(*args):
    cont = 0
    for i in args:
        if isinstance(i, float) or isinstance(i, int):
            cont += i
        else:
            cont += 0
            
    print(cont)
(soma_numeros(10, "Maria", 3.5, "texto", 7, [1,2], 4))
