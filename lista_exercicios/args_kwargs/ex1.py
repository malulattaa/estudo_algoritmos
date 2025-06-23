""" 
Soma com *args
Escreva uma fun¸c˜ ao que aceita qualquer 
quantidade de argumentos num´ ericos e
retorna a soma deles.
"""

def soma(*args):
    return sum(args)

print(soma(1, 6, 9, 4, 2))