"""
Usar filter, map, reduce para:

Somar as idades das pessoas cujo nome tem mais de 5 letras

Esperado: Carolina (27) + Eduardo (35) → resultado 62
"""
from functools import reduce
pessoas = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carolina", "idade": 27},
    {"nome": "Eduardo", "idade": 35}
]

#ter mais de 5 letras: filter
#map so pega a idade e o outro soma?

idades = reduce(lambda x, y: x + y, map(lambda item: item['idade'], filter(lambda item: len(item['nome']) > 5, pessoas)))
print(idades)