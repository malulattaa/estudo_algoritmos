""" 
A partir de uma lista de listas, crie uma lista plana.
Exemplo: [[1,2], [3,4], [5]] → [1,2,3,4,5
"""
lista =  [[1,2], [3,4], [5]]
plana = [x for sub in lista for x in sub] 
print(plana)