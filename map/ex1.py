""" 
Dado um dicionário com nomes de produtos e preços em reais, crie uma nova lista com os 
preços convertidos para dólares (cotação: R$ 5,00).
"""

produtos = {
    "arroz": 20.0,
    "feijão": 10.0,
    "macarrão": 8.5,
    "óleo": 6.0
}

mapeando = list(map(lambda item: f"{item[0]}: $ {item[1]/5} USD", produtos.items()))
print(mapeando)



