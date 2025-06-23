""" 
Dada uma lista de números, crie uma nova lista de tuplas onde cada tupla contenha o número original e o seu quadrado.
Exemplo: [1, 2, 3] → [(1, 1), (2, 4), (3, 9)]
"""

lista = [1, 2, 3]
quadrado = [(n, n**2) for n in lista]
print(quadrado)