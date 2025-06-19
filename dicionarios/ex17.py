""" 
Crie um cadastro de clientes de uma loja. Cada cliente terá:

ID

Nome

Cidade

Estado

Depois permita que o usuário:

✅ Liste todos os clientes
✅ Filtre apenas os clientes de um estado informado
✅ Conte quantos clientes há por cidade (exemplo: {'São Paulo': 3, 'Rio de Janeiro': 2})

"""
from collections import Counter
id_cliente = 1
clientes = {}

while True:
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    
    clientes[id_cliente] = {
        'nome' : nome,
        'cidade' : cidade,
        'estado' : estado,
    }
    
    id_cliente += 1
    
    while True:
        continuar = input("Deseja adicionar mais clientes? (S/N)").upper()
        if continuar in "SN":
            break
    if continuar == "N":
        break
    
for id, dados in clientes.items():
    print("ID: ", {id})
    for c, v in dados.items():
        print(f"{c} = {v}")
    print("")
    
filtrar = input("Deseja filtrar qual estado? ")
filtro = list(filter(lambda e: e[1]['estado'] == filtrar, clientes.items()))
if filtro: 
    for id_c, info in filtro:
        print(f"{id_c}: {info['nome']} - {info['estado']}")
else:
    print("Não há.")
    
cidades = [dados['cidade'] for dados in clientes.values()]
cont_cidade = Counter(cidades)

for n, qtde in cont_cidade.items():
    print(f"{n} = {qtde}")