""" 
Peça ao usuário um texto (uma frase grande).
Conte quantas vezes cada palavra apareceu, usando um dicionário com a palavra como chave e a quantidade como valor.

"""
from collections import Counter
texto = input("Digite um texto: ")
palavras = texto.split()

dicio = {}


for palavra in palavras:
    if palavra in dicio:
        dicio[palavra] += 1 
    else:
        dicio[palavra] = 1
    
print(dicio)
print("")
contagem = Counter(palavras)
print(contagem)
print("")

dicio_dicio = {palavra: palavras.count(palavra) for palavra in set(palavras)}
print(dicio_dicio)