def contagem(n):
    if n < 1:
        print("Boom!")
        return 0
    print(n)
    return n, contagem(n-1)

n = int(input("Digite um n: "))

contagem(n)
