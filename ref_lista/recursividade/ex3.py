def soma(dig):
    if dig <= 1:
        return dig
    return dig % 10 + soma(dig // 10)

digito = int(input("num: "))
print(soma(digito))
