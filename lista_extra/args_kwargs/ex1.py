""" 
Crie uma função que receba qualquer quantidade de números via *args e retorne a média.
"""
def media(*args):
    return sum(args) / len(args)


num = input("digites os numeros  e de espaço para separa-los: ")
numeros = tuple(int(x) for x in num.split())
print(media(*numeros))