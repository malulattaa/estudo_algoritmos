""" 
Gere um novo dicionário apenas com os alunos aprovados (média ≥ 7), contendo id, nome e média.
"""

alunos = {
    1: {'nome': 'Ana', 'media': 6.5},
    2: {'nome': 'Bruno', 'media': 7.8},
    3: {'nome': 'Carla', 'media': 9.0},
    4: {'nome': 'Diego', 'media': 5.9},
}

aprovados = {id: dados for id, dados in alunos.items() if dados['media'] >= 7}

print(aprovados)