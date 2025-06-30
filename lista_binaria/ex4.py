""" 
Se a lista for:

[1, 2, 2, 2, 3, 4, 5]
👉 Faça a busca binária encontrar a primeira posição onde o número 2 aparece.
"""

def ocorrencia(nums, n, inicio, fim):
    if inicio > fim:
        return -1

    if nums[inicio] == n:
        return inicio
    elif nums[inicio] < n:
        return ocorrencia(nums, n, inicio + 1, fim)
    else:
        return -1
    
nums = [1, 2, 2, 2, 3, 4, 5]
n = int(input("Qual número quer achar? "))
busca = ocorrencia(nums, n, 0, len(nums)-1)
if busca != -1:
    print(f"O número {n} aparece pela primeira vez na {busca+1} posição")
else:
    print(f"O número {n} não está na lista!")