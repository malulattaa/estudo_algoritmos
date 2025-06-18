""" 
Monte um dicionário onde cada produto seja uma chave e o valor seja outro dicionário com:

Quantidade vendida

Preço unitário

O total de vendas (quantidade × preço) por produto
O valor total de todas as vendas
O produto que gerou mais receita

"""
produtos = {}

while True:
    produto = input("Produto: ")
    qtde = int(input("Quantidade vendida: "))
    preco = float(input("Preço unitário: "))
    total = qtde * preco

    
    produtos[produto] = {
        'qtde' : qtde,
        'preco' : preco,
        'total' : total,
    }
    
    while True:
        sair = input("Deseja adicionar outro produto? (S/N) ").upper()
        if sair in "SN":
            break
        print("Erro.")
    if sair == 'N':
        break
    print("")
    print("")
    
    
for nome, dados in produtos.items():
    print(f"Produto: {nome}")
    for c, v in dados.items():
        print(f"{c} : {v}")

    print("")

"""total_vendas = sum(produtos.items(), key = lambda p: p[1]['total'])
print(f"Total de todas as vendas: {total_vendas}")"""
total_vendas = sum(dados['total'] for dados in produtos.values())
print(f"Total de todas as vendas: {total_vendas}")

print("")

receita = max(produtos.items(), key = lambda r: r[1]['total'])

print(f"Mais receita: {receita[0]} - Total: R${receita[1]['total']}")