""" 
A partir de uma lista de palavras, retorne apenas as que começam com vogal.
Exemplo: ["uva", "cachorro", "elefante"] → ["uva", "elefante"]


"""

lista = ["uva", "cachorro", "elefante"]

vogal = [string for string in lista if string[0] in 'aeiouAEIOU']
print(vogal)