"""
Você tem uma lista de dicionários, onde cada item representa um produto com:
- nome
- preço
- quantidade em estoque

"""
from functools import reduce 

lista = []
produtos = {}

while True:
    nome = input("Produto: ")
    qtde = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    produtos = {
        'produto' : nome,
        'quantidade' : qtde,
        'preco' : preco,
    }
    lista.append(produtos)
    
    while True:
        add = input("Deseja continuar adicionando? (S/N) ").upper()
        if add in "SN":
            break
    if add == "N":
        break
    
print(lista)
""" 
Usar filter + map + reduce em uma única linha para calcular o valor total 
em reais dos produtos disponíveis no estoque (ou seja, com quantidade > 0).
"""
estoque = reduce(lambda x, y: x + y, map(lambda item: item['quantidade'] * item['preco'], filter(lambda q: q['quantidade'] > 0, lista)))
print(estoque)
print(f"Valor total do estoque: {estoque}")

