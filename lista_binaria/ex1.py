""" 
Dada uma lista ordenada de nomes:

nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fernanda", "Gustavo"]

Peça ao usuário um nome e use a busca binária para verificar se ele está na lista.
"""

def binaria(nomes, nome, inicio, fim):

    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    
    if nomes[meio] == nome:
        return meio
    elif nome < nomes[meio]:
        #percorre pro lado esquerdo nomes[meio - 1]
        return binaria(nomes, nome, inicio, meio - 1)
    else:
        return binaria(nomes, nome, meio + 1, fim)

nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fernanda", "Gustavo"]
nome = input("Nome: ")
busca = binaria(nomes, nome, 0, len(nomes) - 1)
if busca != -1:
    print(f"O nome {nome} está na lista, na {busca+1} posição")
else:
    print(f"O nome {nome} não está na lista")

