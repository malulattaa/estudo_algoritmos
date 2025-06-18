#usuario digita td de uma vez, separados por espaço

entrada = input("Digite os valores separados por espaço: ")
tupla_valores = tuple(map(int, entrada.split()))

print(tupla_valores)