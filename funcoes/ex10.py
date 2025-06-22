""" 
Função que receba um dicionário de 
produtos (nome e preço) e retorne os produtos com preço acima de R$100
"""

def produtos_caros(produtos):
    acima_100 = {produto: valor for produto, valor in produtos.items() if valor >100}
    return acima_100


produtos = {
    'camisa': 50,
    'calça': 120,
    'meia': 10,
    'jaqueta': 200
}


print(produtos_caros(produtos))
