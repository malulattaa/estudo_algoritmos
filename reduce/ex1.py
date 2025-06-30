""" 
use reduce() para calcular o total de itens vendidos.
"""
from functools import reduce

vendas = {
    "arroz": 10,
    "feijão": 7,
    "óleo": 5,
    "macarrão": 3
}

vendidos = reduce(lambda x,y: x + y, vendas.values())
print(vendidos)
