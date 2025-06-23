""" 
Exercício 3 - Buscar maior valor menor que um dado número:
Exemplo:
Se a lista for:
[10, 20, 30, 40, 50]
E o usuário buscar o número 35, a função deve retornar 30 (o maior menor que 35).
👉 Use uma modificação da lógica da busca binária.

"""

def binaria(lista, num, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    
    if lista[meio] < num:
        candidato = lista[meio]
        buscando = binaria(lista, num, meio + 1, fim)
        if buscando != -1:
            return buscando
        else:
            return candidato
    else:

        return binaria(lista, num, inicio, meio - 1)
    
lista = [10, 20, 30, 40, 50]

num = int(input("Qual número deseja procurar? "))
busca = binaria(lista, num, 0, len(lista)-1)
print(busca)