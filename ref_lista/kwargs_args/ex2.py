def mult(*args):
    multiplicacao = 1
    for m in args:
        if isinstance(m, (int, float)):
            multiplicacao *= m 
    return multiplicacao

lista = []
while True:
    nums = int(input("Digite os números: "))
    lista.append(nums)
    sair = input("Deseja sair? (S/N) ").upper()
    while True:
        if sair in 'SN':
            break
        print("Digite S ou N")
    if sair == "S":
        break
print(mult(*lista))