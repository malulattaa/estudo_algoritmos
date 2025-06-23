""" 
Dadas três listas de números, gere todas as combinações possíveis de trios (produto cartesiano).
Exemplo: [1,2], [3,4], [5,6] →

[(1,3,5), (1,3,6), (1,4,5), (1,4,6), (2,3,5), (2,3,6), (2,4,5), (2,4,6)]

"""
list1 = [1,2]
list2 = [3, 4]
list3 = [5, 6]


cartesiano = [(comb1, comb2, comb3) for comb1 in list1 for comb2 in list2 for comb3 in list3]
print(cartesiano)