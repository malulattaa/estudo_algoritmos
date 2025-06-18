numeros = (10, 20, 30, 40 ,50, 15)

print(f"Soma: ", sum(numeros))

if 30 in numeros:
    print("30 pertence a lista números")
    
nova = tuple(p for p in numeros if p % 2 == 0)
print(nova)

