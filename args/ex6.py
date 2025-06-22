""" 
Faça uma função exibir_dados que apenas imprima 
um por um os valores recebidos via *args.
"""

def exibir_dados(*args):
    for dado in args:
        print(dado)
    
(exibir_dados(1, 2, 3, 4, 5))