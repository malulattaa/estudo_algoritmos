from functools import reduce
id_aluno = 1
alunos = {}
medias = []
while True:
    notas = []
    nome = input("Nome: ")
    for n in range(3):
        nota = float(input("Nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    
    alunos[id_aluno]= {
        'nome' : nome,
        'notas' : notas,
        'media' : media,
    }
    id_aluno += 1
    
    while True:
        sair = input("Deseja continuar cadastrando [S/N]? ").upper()
        if sair in 'SN':
            break
        print("Erro")
    if sair == 'N':
        break
    
maior_media = 0
aluno_maior_media = 0
for id, dados in alunos.items():
    print(f"ID: {id}")
    media_atual = dados['media']
    if maior_media < media_atual:
        maior_media = media_atual
        aluno_maior_media = dados['nome']
    for c, v in dados.items():
        print(f"{c} : {v}")
        print("")
print(f"A maior média foi do aluno: {aluno_maior_media} com {maior_media}")
        

