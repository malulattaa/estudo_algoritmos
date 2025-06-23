""" 
Crie uma função que receba informações de um cadastro usando **kwargs e imprima assim:
"""

def cadastro(**kwargs):
    for c, v in kwargs.items():
        print(f"Campo: {c} -> Valor: {v}")
        
while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")
    
    continuar = input("Deseja continuar add pessoas? (S/N) ").upper()
    while True:
        if continuar in 'SN':
            break
        print("Digite S para sim ou N para não.")
    if continuar == 'N':
        break
    
cadastro(nome = nome, idade = idade, cidade = cidade)

def cadastro(**kwargs):
    for c, v in kwargs.items():
        print(f"Campo: {c} -> Valor: {v}")
        
while True:
    pessoa = {
    'nome' : input("Nome: "),
    'idade' : int(input("Idade: ")),
    'cidade' : input("Cidade: ")}
    
    continuar = input("Deseja continuar add pessoas? (S/N) ").upper()
    while True:
        if continuar in 'SN':
            break
        print("Digite S para sim ou N para não.")
    if continuar == 'N':
        break
    
cadastro(**pessoa)