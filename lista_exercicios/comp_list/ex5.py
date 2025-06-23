""" 
Dadas duas listas de numeros, gere todos os pares possiveis 
entre elementos de uma e de outra.
 Exemplo: [1,2] e [3,4] → [(1,3), (1,4), (2,3), (2,4)]

"""
lista1 = [1,2]
lista2 = [3,4]
produto_cartesiano = [(x,y) for x in lista1 for y in lista2]
print(produto_cartesiano)