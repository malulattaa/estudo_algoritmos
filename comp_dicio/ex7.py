""" 
Conte quantos clientes há em cada cidade e mostre o resultado em um dicionário.
"""
from collections import Counter

clientes = {
    1: {'nome': 'João', 'cidade': 'São Paulo'},
    2: {'nome': 'Maria', 'cidade': 'Rio de Janeiro'},
    3: {'nome': 'José', 'cidade': 'São Paulo'},
    4: {'nome': 'Ana', 'cidade': 'Curitiba'},
    5: {'nome': 'Paulo', 'cidade': 'Rio de Janeiro'},
}

cidades = [dados['cidade'] for dados in clientes.values()]
print(cidades)

contagem = Counter(cidades)
print(contagem)