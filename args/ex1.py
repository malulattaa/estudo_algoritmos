""" 
Crie uma função chamada soma_total que aceite uma 
quantidade indefinida de números e retorne a soma total.

"""

def soma_total(*args):
    soma = sum(args)
    return soma

print(soma_total(1, 6, 9, 8))