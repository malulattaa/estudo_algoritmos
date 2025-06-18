

#media = 29,5

def estatisticas_tupla(tupla):
    qtde = len(tupla)
    media = sum(tupla) / len(tupla)
    maior = max(tupla)
    menor = min(tupla)
    
    return qtde, media, maior, menor


print(estatisticas_tupla((20, 50, 5, 75, 15, 12)))