""" 
Escreva uma fun¸c˜ ao recursiva que recebe uma string e retorna a string invertida.
Exemplo: "python" → "nohtyp"
"""

def inverter(string):
    if len(string) <= 1:
        return string
    return string[-1] + inverter(string[:-1])

print(inverter("python"))

