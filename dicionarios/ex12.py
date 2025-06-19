produtos = {
    'camisa': 50,
    'calça': 120,
    'meia': 10,
    'jaqueta': 200
}

""" 
Mostre apenas os produtos com preço acima de R$100, usando filter + lambda + conversão para dict:
"""

acima_100 = list(filter(lambda x: print(f"{x[0]} - {x[1]}") if x[1] > 100 else None, produtos.items()))

acima_100 = dict(filter(lambda x: x[1] > 100, produtos.items()))
print("\nProdutos acima de R$100:")
for nome, preco in acima_100.items():
    print(f"{nome} - R${preco}")