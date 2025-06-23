""" 
Dada uma lista de numeros, retorne uma nova lista com os 
quadrados apenas dos numeros pares.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [x for x in lista if x % 2 == 0]
print(pares)