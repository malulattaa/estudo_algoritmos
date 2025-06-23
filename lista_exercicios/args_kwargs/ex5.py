""" 
 Crie uma fun¸c˜ ao que usa **kwargs para formatar strings com placeholders perso
nalizados.
 Exemplo: formata("Ol´ a {nome}, seja bem-vindo(a) a {cidade}.", nome="Ana",
 cidade="Recife"
"""

def placeholders(**kwargs):
    print(f"Olá {kwargs['nome']}, seja bem-vindo(a) a {kwargs['cidade']}")
    
pessoa = {}

pessoa['nome'] = input("Nome: ")
pessoa['cidade'] = input("Cidade: ")

placeholders(**pessoa)

def placeholders(**kwargs):
    for c, v in kwargs.items():
        print(f"Olá {c}, seja bem-vindo(a) a {v}")
    
pessoa = {}

nome =  input("Nome: ")
cidade = input("Cidade: ")
pessoa[nome] = cidade

placeholders(**pessoa)

#correção

def placeholders(texto, **kwargs):
    print(texto.format(**kwargs))
    
nome =  input("Nome: ")
cidade = input("Cidade: ")

placeholders(f"Olá {nome} seja bem-vindo(a) a {cidade}", nome = nome, cidade = cidade)

#com o usuario digitando

def formata(texto, **kwargs):
    print(texto.format(**kwargs))
    
frase = input("Digite a frase: ")

nome =  input("Nome: ")
cidade = input("Cidade: ")

formata(frase, nome = nome, cidade = cidade)