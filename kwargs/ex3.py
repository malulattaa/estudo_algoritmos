""" 
Função que recebe vários alunos e suas notas 
(**kwargs) e retorna quem está aprovado (nota >=7).
"""

def aprovados(**kwargs):
    for nome, nota in kwargs.items():
        if nota >= 7:
            print(f"{nome} : {nota}")
            
alunos = {}

while True:
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    alunos[nome] = nota
    
    sair = input("Deseja continuar adicionando (S/N) ")
    if sair == 'N':
        break
    
aprovados(**alunos)