from functools import reduce

""" 
Usar map, filter e reduce em uma linha para:

Somar o total em reais das vendas com quantidade maior que 0.
"""

vendas = [
    {"produto": "arroz", "quantidade": 2, "preco": 20.0},
    {"produto": "feijão", "quantidade": 0, "preco": 10.0},
    {"produto": "óleo", "quantidade": 3, "preco": 6.5},
    {"produto": "macarrão", "quantidade": 1, "preco": 8.5},
]


#map pra multiplicar
#reduce pra somar
#filter filtrar

total = reduce(lambda x,y: x+y, map(lambda item: item['quantidade'] * item['preco'], filter(lambda item: item['quantidade'] > 0, vendas)))
print(total)