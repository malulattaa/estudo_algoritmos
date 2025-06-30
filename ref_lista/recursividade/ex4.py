def pot(base, expoente):
    if expoente <= 0:
        return 1
    return base * pot(base, expoente - 1)

base = int(input("Base: "))
expoente = int(input("Expoente: "))

print(pot(base, expoente))