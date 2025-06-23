""" 
Faça uma função recursiva que conte quantas vogais existem em uma string.
Exemplo: "recursividade" → 6
"""

def recursividade(string):
    if len(string) <= 1:
        return 1
    if string[0] in 'aeiouAEIOU':
        return 1 + recursividade(string[1:])
    else:
        return recursividade(string[1:])

print(recursividade("recursividade"))