""" 
Escreva uma fun¸ c˜ao recursiva que retorna a 
soma dos d´ ıgitos de um n´umero inteiro
positivo.
Exemplo: soma
digitos(1234) → 10
"""

def soma(n):
    if n <= 1:
        return n
    return n % 10 + soma(n // 10) 

print(soma(125))
    
    
#transformando em string 

def digitos(n):
    if len(str(n)) <= 1:
        return n
    return int(str(n)[0]) + digitos(int(str(n)[1:]))

print(digitos(1234))