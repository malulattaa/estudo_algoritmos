""" 
Implemente a busca bin´ aria de forma 
recursiva para uma lista ordenada

"""


def busca(lista, elemento, inicio, fim):
    if inicio > fim:
        return - 1
    
    meio = (inicio + fim)// 2
    
    if lista[meio] == elemento:
        return meio
    elif elemento < lista[meio]:
        return busca(lista, elemento, inicio, meio - 1)
    else:
        return busca(lista, elemento, meio + 1, fim)

lista = [1, 3, 5, 7, 9, 11, 13, 15]
elemento = int(input("Elemento que quer buscar: "))

resultado = busca(lista, elemento, 0, len(lista) - 1)
print(f"O elemento {elemento} está na {resultado}° posição")
