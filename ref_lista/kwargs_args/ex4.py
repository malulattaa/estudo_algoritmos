def filtro(*args, **kwargs):
    filtrados = []
    minimo = kwargs['min']
    maximo = kwargs['max']
    
    for nums in args:
        if nums >= minimo and nums <= maximo:
            filtrados.append(nums)
    return filtrados



kwargs = {}
kwargs['min'] = int(input("Digte o valor mínimo: "))
kwargs['max'] = int(input("Digte o valor máximo: "))

filtrando = input("digite os valores a serem filtrados separados por espaço: ")
arg = tuple(int(x) for x in filtrando.split())
print(filtro(*arg, **kwargs))