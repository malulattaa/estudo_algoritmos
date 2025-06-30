""" 
Usando compreens˜ao de lista, inverta cada palavra de uma 
lista de strings.
Exemplo: ["casa", "gato"] → ["asac", "otag"]
"""

lista = []
while True:
    p = input("Palavra: ")
    lista.append(p)
    sair = input("Deseja continuar add? (S/N) ").upper()
    if sair == 'N':
        break
    
inverter = [x[::-1] for x in lista]
print(inverter)
