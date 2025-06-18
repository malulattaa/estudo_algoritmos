id_funcionario = 1
dados = {}
while True:
    dados[id_funcionario] = {
        'nome' : input("Nome: "),
        'cargo' : input("Cargo: "),
        'salario' : int(input("Salário: ")) 
    }
    id_funcionario += 1
    continuar = input("Deseja continuar? S/N ").upper()
    if continuar == 'N':
        break

for id, func in dados.items():
    print(f"ID: {id}")
    for chave, valor in func.items():
        print(f"{chave} : {valor}")
        