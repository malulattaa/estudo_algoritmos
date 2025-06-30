alunos = [
    {"nome": "Ana", "notas": [8, 7.5, 9]},
    {"nome": "Bruno", "notas": [5, 6, 5.5]},
    {"nome": "Carlos", "notas": [7, 7, 7]},
    {"nome": "Diana", "notas": [6, 6.5, 6.8]},
    {"nome": "Eva", "notas": [9, 9, 10]}
]


aluno = list(map(lambda item: f"{item['nome']} - Média: {sum(item['notas'])/len(item['notas'])}", filter(lambda x: sum(x['notas'])/len(x['notas'])>=7, alunos)))
print(aluno)