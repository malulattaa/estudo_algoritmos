#para aplicar uma função a cada item da sequência e desenvolver outra sequencia com o mesmo tamanho

#map(função, sequeência)

numeros = [1, 2, 3, 4, 5, 6]

mapeando = list(map(lambda x: x**2, numeros))
print(mapeando)