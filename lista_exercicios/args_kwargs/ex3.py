""" 
Crie umafun¸c˜ ao saudar(**kwargs) que aceita os argumentos nome, idade e cidade,
e monta uma mensagem personalizada.
Exemplo: "Ol´ a, Jo~ ao de 30 anos, morador de S~ao Paulo!
"""

def saudacao(**kwargs):
    print(f"Olá, {kwargs['nome']} de {kwargs['idade']} anos, morador de {kwargs['cidade']}!")
        
pessoa = {}        
pessoa['nome'] = input("Nome: ")
pessoa['idade'] = int(input("Idade: "))
pessoa['cidade'] = input("Cidade: ")

saudacao(**pessoa)