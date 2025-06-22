""" 
Função que imprime chave e 
valor de qualquer dicionário passado via **kwargs.
"""

def imprimir(**kwargs):
    for c, v in kwargs.items():
        print(f"{c} : {v}")
        
pessoa = {}

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pessoa[nome] = idade
    
    sair = input("Deseja continuar adicionando (S/N) ")
    if sair == 'N':
        break
    
imprimir(**pessoa)