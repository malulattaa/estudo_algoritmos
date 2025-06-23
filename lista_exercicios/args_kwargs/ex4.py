""" 
Fun¸c˜ ao de filtro com *args e **kwargs
Escreva uma fun¸c˜ ao que aceita uma lista de n´ umeros via *args e usa **kwargs para
aplicar filtros, como min=10, max=50.
"""

def filtro(*args, **kwargs):
    filtrados = []
    minimo = kwargs.get('min')
    maximo = kwargs.get('max')
    
    for num in args:
        if num >= minimo and num <= maximo:
            filtrados.append(num)
    return filtrados

numeros_args = input("Digite os numeros, utilizando espaço para separá-los: ")
args = tuple(int(x) for x in numeros_args.split())


kwargs = {}
minimo = int(input("Digite o valor minimo: "))
kwargs['min'] = minimo

maximo = int(input("Digite o valor máximo: "))
kwargs['max'] = maximo


print(filtro(*args, **kwargs))

#.get('min', float('-inf')) → Se o filtro min não for informado, assume sem limite inferior.