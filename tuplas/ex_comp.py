numeros = input("Digite números separador por espaço: ")

#1 

conversao = tuple(map(int, numeros.split()))
print(conversao)


#2

dobro = list(map(lambda x: x*2, conversao))
print(dobro)