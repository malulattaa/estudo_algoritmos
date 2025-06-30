#acumula ou reduz todos os itens de uma sequência a um único valor

#from functools import reduce
#reduce(função, sequência)
from functools import reduce
numeros = [1, 2, 3, 4, 5]

reduzindo = reduce(lambda x,y: x + y, numeros)
print(reduzindo)
