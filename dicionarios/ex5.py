""" 
Crie um dicionário que armazene informações de alunos, onde cada aluno é uma chave (um id), e o valor é outro dicionário com:

nome

lista de notas (exemplo: [7.5, 8.0, 6.0])

média das notas

Depois, faça um loop que imprima os dados dos alunos formatados.
"""
id_aluno = 1
alunos = {}

while True:
    notas = []
    nome = input("Digite o nome do aluno: ")
    for n in range(4):
        nota = float(input(f"Nota {n}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    
    alunos[id_aluno] = {
        'nome' : nome,
        'nota' : notas,
        'media' : media,
    }
    id_aluno += 1
    while True:
        continuar = input("Deseja sair? S/N ").upper()
        if continuar in "SN":
            break
        print("Digite S ou N")
    if continuar == "S":
        break
    
for id, dados in alunos.items():
    print(f"ID: {id}")
    for c, v in dados.items():
        print(f"{c} : {v}")
    