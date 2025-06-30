#para quando quer selecionar apenas os itens que satisfazem uma condição

#filter(função, sequência)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

filtrando = list(filter(lambda x: x % 2 == 0, numeros)) 
print(filtrando)