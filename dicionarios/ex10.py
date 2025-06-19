""" 
Monte um dicionário com funcionários (nome como chave) e salário como valor.

Depois, crie uma função que:

✅ Aumente o salário de todos em 10%
✅ Mostre apenas os funcionários que ganham acima de um certo valor informado pelo usuário


"""
funcionarios = {}

while True:
    nome = input("Nome: ")
    salario = int(input("Salário: "))
    
    funcionarios[nome] = salario
    
    while True: 
        add = input("Continuar adicionando? (S/N) ").upper()
        if add in "SN":
            break
    if add == "N":
        break

for nome, salario in funcionarios.items():
    print(f"{nome} - R${salario}")
    print("")
    
aumento = list(map(lambda item: print(f"{item[0]} - R${item[1] * 1.1}"), funcionarios.items()))

buscar = int(input("Informe o valor que deseja buscar: "))

filtrar = list(filter(lambda item: print(f"{item[0]} - {item[1]}") if item[1] >= buscar else None, funcionarios.items()))

