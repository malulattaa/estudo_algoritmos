""" 
Use sorted() com key=lambda

Percorra o resultado com enumerate() pra mostrar a posição

Não use for aninhado

Não use lista auxiliar desnecessária

Tudo direto com o dicionário que já tem
"""

alunos = {
    1: {'nome': 'Maria', 'media': 8.5},
    2: {'nome': 'João', 'media': 6.0},
    3: {'nome': 'Ana', 'media': 9.0},
    4: {'nome': 'Pedro', 'media': 7.3},
}

ranking = sorted(alunos.items(), key = lambda item: item[1]['media'], reverse=True)
print(ranking)
for posicao, (id_aluno, dados_aluno) in enumerate(ranking, start = 1):
    print(f"{posicao}° lugar: {dados_aluno['nome']} com média {dados_aluno['media']}")

