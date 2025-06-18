    
def analise_lista(lista):
    dicio = {}
    dicio['maior'] = max(lista)
    dicio['menor'] = min(lista)
    dicio['media'] = sum(lista) / len(lista)
    dicio['pares'] = len([p for p in lista if p % 2 == 0])
    
    return dicio
    
lista = []
while True:
    num = int(input("Digite um número ou 000 para parar: "))
    if num == 000:
        break
    lista.append(num)
    
print(analise_lista(lista))