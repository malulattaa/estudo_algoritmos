""" 
Crie uma função que apenas retorne quantos 
argumentos foram passados via *args.
"""

def qtde(*args):
    return len(args)

print(qtde(1, 9, 4, 7, 6))