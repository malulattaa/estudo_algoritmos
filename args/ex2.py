""" 
Crie uma função chamada media que receba qualquer quantidade de notas e retorne a média.
"""

def media(*args):
    media_nota = sum(args) / len(args)
    return media_nota

print(media(1, 8, 5.5))

#correção (possivel divisao por 0)

def media2(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(media2())
