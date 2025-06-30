def binaria(lista, n, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if n == lista[meio]:
        return lista[meio]
    
    if lista[meio] < n:
        return binaria(lista, n, meio + 1, fim)
    else:
        return binaria(lista, n, inicio, meio - 1)
lista = []
while True:
    nums = int(input("Digite números ordenados: "))
    lista.append(nums)
    sair = input("Quer sair? ").upper()
    while True:
        if sair in "SN":
            break
        print("Digite S ou N")
    if sair == "S":
        break
inicio = int(input("Digite o número de inicio: (padrão 0)"))
fim = int(input("Digite o fim: "))
n = int(input("Número procurado: "))
print(binaria(lista, n, inicio, fim-1))
    
        