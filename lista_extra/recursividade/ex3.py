""" 
Implemente uma função recursiva que retorne o n-ésimo número da sequência de Fibonacci.
"""

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(6))