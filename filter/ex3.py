from functools import reduce 

""" 
Usando map + filter + reduce, em uma linha:

Calcule a média de cada aluno

Filtre quem tem média ≥ 7

Some todas as notas dos aprovados (somando todas as notas mesmo, não as médias)

"""

alunos = [
    {"nome": "Ana", "notas": [8, 9, 10]},
    {"nome": "Bruno", "notas": [5, 6, 4]},
    {"nome": "Carlos", "notas": [7, 7, 7]},
    {"nome": "Diana", "notas": [6, 6.5, 6.9]},
    {"nome": "Eva", "notas": [9, 8.5, 9]}
]


soma = sum(reduce(lambda x, y: x + y, map(lambda item:item['notas'], filter(lambda item: sum(item['notas'])/len(item['notas']) >=7, alunos))))
print(soma)