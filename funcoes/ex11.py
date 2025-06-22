"""Função que receba um número e retorne se ele é primo

Primeiro, verifica se o número é menor ou igual a 1 → Se for, não é primo.

Depois, faz um loop de 2 até o número-1 (ou até a raiz quadrada, se quiser otimizar).
Vai testando: "Esse número é divisível por algum número entre 2 e ele-1?"

Se encontrar alguma divisão exata, significa que o número não é primo.

Se o loop terminar sem achar divisor, então o número é primo.

"""

def eh_primo(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

print(eh_primo(8))