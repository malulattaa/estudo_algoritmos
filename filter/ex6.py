""" 
Usar zip, map, reduce, e filter para:

Calcular a média ponderada de cada aluno

Retornar apenas os alunos com média ≥ 7

Mostrar como: "Carlos - média: 7.33"

"""
from functools import reduce

alunos = [
    {"nome": "Ana", "notas": [7, 8, 9], "pesos": [2, 3, 5]},
    {"nome": "Bruno", "notas": [5, 5, 5], "pesos": [1, 1, 1]},
    {"nome": "Carlos", "notas": [6, 7, 8], "pesos": [1, 2, 3]},
]


