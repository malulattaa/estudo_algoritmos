"""Dada uma lista de strings, crie uma nova lista com o número de caracteres de cada palavra.
Exemplo: ["casa", "gato"] → [4, 4]"""

lista = ["casa", "gato", "cachorro"]
caractere = [len(c) for c in lista]
print(caractere)

