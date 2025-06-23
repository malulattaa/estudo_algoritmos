""" 
Implemente uma fun¸c˜ ao recursiva que calcula base^expoente, onde ambos s˜ao in
teiros positivos.
"""

def potencia(base, expoente):
    if expoente <= 0:
        return 1
    return base * potencia(base, expoente - 1)

print(potencia(2, 5))