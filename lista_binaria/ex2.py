""" 
Dada uma lista de números ordenados:

numeros = [2, 4, 6, 8, 10, 12, 14, 16]
👉 Faça uma busca binária para retornar o índice onde o número está.
"""
def binaria(numeros, num, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if numeros[meio] == num:
        return meio
    elif numeros[meio] > num:
        return binaria(numeros, num, inicio, meio - 1)
    else:
        return binaria(numeros, num, meio + 1, fim)
    

numeros = [2, 4, 6, 8, 10, 12, 14, 16]
num = int(input("Qual número deseja procurar? "))
busca = binaria(numeros, num, 0, len(numeros)-1)
if busca != -1:
    print(f"o número {num} está na {busca+1} posição")
else:
    print("Esse número não está na lista")