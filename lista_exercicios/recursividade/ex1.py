""" 
 Implemente uma fun¸c˜ ao recursiva contagem
 regressiva(n) que imprime uma con
tagem de n at´ e 0. Ao chegar a 0, deve imprimir "Boom!".
 (Opcional: usar time.sleep(1) para simular contagem real.)
"""

def contagem_regressiva(n):
    if n == 0:
        print("Boom!")
        return
    print(n)
    return n, contagem_regressiva(n-1)


(contagem_regressiva(5))