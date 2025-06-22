""" 
Função que calcule o fatorial de um número (usando loop simples por enquanto)
"""
def fatorial(num):
    add = num
    for fat in range(num, 1, -1):
        result = add * (fat - 1)
        add = result
        
    return add

print(fatorial(6))