""" 
Função que recebe informações 
de um produto (**kwargs) e imprime os detalhes.
"""

def produto(**kwargs):
    for c, v in kwargs.items():
        print(f"{c} : {v}")
        
(produto(nome = input("Nome"), qtde = int(input("Qtde: ")), preco = float(input("Preço: "))))