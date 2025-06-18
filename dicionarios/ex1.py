produtos = []

for _ in range(3):
    produto = {
        'Produto': input("Digite o nome: "),
        'preco' : float(input("Digite o preço: ")),
        'quantidade' : int(input("Estoque: ")),
        
    }
    produtos.append(produto)
    
for p in produtos:
    for c, v in p.items():
        print(f"{c}: {v}")
    total = p['preco'] * p['quantidade']
    print(f"Total: {total} ")