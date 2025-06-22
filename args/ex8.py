""" 
Crie uma função chamada filtrar_palavras_grandes
que receba *args e retorne uma lista apenas 
com as strings que tenham mais de 5 caracteres.


"""
# def filtrar_palavras_grandes(*args):
#     palavras = [i for i in args if len(i) > 5]
#     return palavras

def filtrar_palavras_grandes(*args):
    return list(filter(lambda x: len(x) > 5, args))

print(filtrar_palavras_grandes("Ana", "Mariana", "Sol", "Computador", "Chá", "Amor"))

