""" 
Com o mesmo dicionário acima, use map para criar um novo dicionário com todos os preços com 20% de desconto.
"""

produtos = {
    'camisa': 50,
    'calça': 120,
    'meia': 10,
    'jaqueta': 200
}


desconto = dict(map(lambda x: (x[0], x[1] * 0.8), produtos.items()))
for p, i in desconto.items():
    print(f"{p} - {i}")
