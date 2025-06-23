""" 
Dada uma lista de números, crie uma nova lista com o cubo de cada número.
Exemplo: [1, 2, 3] → [1, 8, 27]
"""

lista = [1, 2, 3]
cubo = [x **3 for x in lista]
print(cubo)

