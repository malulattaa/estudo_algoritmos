""" 
Crie um novo dicionário com os mesmos produtos, mas aplicando um aumento de 10% no preço.
"""

vendas = {
    'camisa': 120,
    'calça': 80,
    'meia': 50,
    'jaqueta': 200
}

aumento = {produto: valor * 1.1 for produto, valor in vendas.items()}
print(aumento)
