""" 
Função que calcule a soma de vários números usando *args
(A gente já vai começar a introduzir *args aqui 😄)

"""

def soma(*args):
    somando = sum(args)
    return somando

print(soma(1, 2, 3, 4, 5, 5))  