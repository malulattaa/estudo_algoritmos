"""Crie uma função chamada dados_aluno que receba o nome do aluno e uma lista com 3 notas.
Ela deve calcular a média e retornar o nome e a média"""

def dados_alunos(nome, lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    return nome, media

print(dados_alunos("Maria", [9, 8, 7.5, 7]))