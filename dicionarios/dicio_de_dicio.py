alunos = {
    1: {'nome': 'Maria', 'idade': 20, 'nota': 8.5},
    2: {'nome': 'João', 'idade': 22, 'nota': 7.0},
    3: {'nome': 'Ana', 'idade': 21, 'nota': 9.2}
}


for id_aluno, dados_aluno in alunos.items():
    print(f"ID: {id_aluno}")
    for chave, valor in dados_aluno.items():
        print(f"{chave} : {valor}")