""" 
Crie um novo dicionário chamado aprovados, usando compreensão de dicionário, 
contendo apenas os alunos com média maior ou igual a 7, no formato:

{
    id: {'nome': nome, 'media': media}
}

"""

alunos = {
    1: {'nome': 'Maria', 'media': 8.5},
    2: {'nome': 'João', 'media': 6.0},
    3: {'nome': 'Ana', 'media': 9.0},
    4: {'nome': 'Pedro', 'media': 7.3},
}

aprovados = {id: dados for id, dados in alunos.items() if dados['media'] > 7}

print(aprovados)