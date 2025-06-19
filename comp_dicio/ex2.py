""" 
As chaves sejam os nomes

Os valores sejam a quantidade de letras de cada nome

Mas apenas para os nomes que começam com a letra "A"
"""


nomes = ['Ana', 'Bruno', 'Carlos', 'Amanda', 'Beatriz', 'Caio']

pessoas = {nome: len(nome) for nome in nomes if nome[0] == 'A'}

print(pessoas)