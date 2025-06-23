""" 
Implemente uma função recursiva que calcule o fatorial de um número positivo.
Exemplo: fatorial(5) → 120
"""
def fatorial(n):
    if n <= 1:
        return n
    return n * fatorial(n-1)

print(fatorial(5))