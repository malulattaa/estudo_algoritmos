"""
Some o total de todos os preços do dicionário de produtos usando reduce.
"""
from functools import reduce
produtos = {
    'camisa': 50,
    'calça': 120,
    'meia': 10,
    'jaqueta': 200
}

soma = reduce(lambda s, p: s + p[1], produtos.items(), 0) 
print(soma)