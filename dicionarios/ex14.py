""" 
Fazer um dicionário com nomes de alunos e notas, depois aplicar map para calcular se estão aprovados ou reprovados.
"""

id_aluno = 1 
alunos = {}
while True:
    notas = []
    aluno = input("Nome: ")
    for n in range(1, 5):
        nota = float(input(f"Digite a {n}° nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
        
    alunos[id_aluno] = {
        'nome' : aluno,
        'notas' : notas,
        'media' : media,
    }
    id_aluno += 1
    
    while True:
        continuar = input("Deseja continuar? (S/N)").upper()
        if continuar in "SN":
            break
        print("Erro")
    if continuar == 'N':
        break
    
for id, dados in alunos.items():
    print(f"ID: {id}")
    for c, v in dados.items():
        print(f"{c} : {v}")
        
aprovados = dict(map(lambda x: (x[1]['nome'], "Aprovado" if x[1]['media'] > 7 else "Reprovado"), alunos.items()))
for n, a in aprovados.items():
    print(f"{n} - {a}")