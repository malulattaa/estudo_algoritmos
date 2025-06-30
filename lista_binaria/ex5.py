""" 
Contar quantas vezes um número aparece 
(usando binária):
Exemplo:

[1, 2, 2, 2, 3, 4, 5]
👉 Se o número for 2, a resposta deve ser 3 ocorrências.

Aqui a ideia é fazer uma busca binária para achar a primeira posição e a última posição de 2 e calcular a quantidade.
"""

def ocorrencia(nums, n, inicio, fim):
    cont = 0
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    
    if nums[meio] == n:
        
        return cont
    elif nums[meio] < n:
        procurando = ocorrencia(nums, n, meio +1, fim)
        if procurando == n:
            posicao = procurando[meio]
        return cont
        
nums = [1, 2, 2, 2, 3, 4, 5]
n = int(input("numero: "))
busca = ocorrencia(nums, n, 0, len(nums)-1)
print(f"o numero {n} aparece {busca} vezes")