""" 
 Escreva uma fun¸c˜ ao que aceita qualquer quantidade de argumentos num´ ericos e
 retorna a soma deles.

"""


def soma(*args):
    return sum(args)

n = input("Digite os números separados por espaço: ")
nums = (list(int(x)for x in n.split()))
print(soma(*nums))
