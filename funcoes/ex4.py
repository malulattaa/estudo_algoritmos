""" 
Crie uma função chamada media_lista que receba uma lista de números e retorne a média."""

def media_lista(lista):
    media = sum(lista) / len(lista)
    return media
    
print(media_lista([7, 7.5, 8, 9]))
