""" 
Peça ao usuário um texto.

Monte um dicionário onde:

✅ As chaves são as palavras
✅ Os valores são o número de letras de cada palavra
"""
from collections import Counter
palavras = {}

texto = input("Digite o texto: ")

palavra = texto.split()

palavras = Counter(palavra)


print(palavras)