""" 
Peça ao usuário para digitar uma frase e crie um dicionário que armazene:

Cada caractere como chave

Quantas vezes ele apareceu como valor
"""

from collections import Counter

frase = input("Digite uma frase: ")
dicio = {}
count = Counter(frase)

dicio = count

for letra, qtde in dicio.items():
    print(f"A letra {letra} aparece {qtde} vezes")
    