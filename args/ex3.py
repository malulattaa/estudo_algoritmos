""" 
Crie uma função chamada filtrar_pares que aceite 
vários números via *args e retorne apenas os pares 
(use list comprehension ou filter).
"""

def filtrar_pares(*args):
    return list(filter(lambda item: item if item % 2 == 0 else None, args))
    
print(filtrar_pares(1, 2, 3, 4, 5, 6, 7, 8, 12))