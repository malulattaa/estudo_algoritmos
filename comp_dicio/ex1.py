""" 
Dada a lista de números abaixo:

numeros = [1, 2, 3, 4, 5, 6]
👉 Crie um dicionário onde:

As chaves sejam os números

Os valores sejam o quadrado de cada número.
"""

numeros = [1, 2, 3, 4, 5, 6]

dicio = {n: n**2 for n in numeros}
print(dicio)