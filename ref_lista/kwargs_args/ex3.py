""" 

"""

def saudar(**kwargs):
    print(f"Olá, {kwargs['nome']} de {kwargs['idade']}, morador de {kwargs['cidade']}")
    
nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")

saudar(nome = nome, idade= idade, cidade= cidade)