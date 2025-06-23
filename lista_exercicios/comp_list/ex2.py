""" 
A partir de uma lista de palavras, 
retorne apenas as que tˆem mais de 5 caracteres
"""
lista = []
while True:
    p = input("Palavra: ")
    lista.append(p)
    sair = input("Deseja continuar add? (S/N) ")
    if sair == 'S':
        break
    
palavras = [c for c in lista if len(c) > 5]
print(palavras)