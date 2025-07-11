"""Monte um cadastro de alunos com:

Nome

Lista de notas

Depois mostre:

✅ A média de cada aluno
✅ Apenas os alunos com média acima de 7
✅ O aluno com a menor média"""

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

for maior in alunos.values():
    if maior['media'] >= 7:
        print(f"Media maior que 7: {maior['nome']}")

menor = min(alunos.items(), key = lambda x: x[1]['media'])
print(f"{menor[1]['nome']}, media {menor[1]['media']}")

