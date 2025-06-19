""" 
Crie um dicionário que contenha o 
salário de cada funcionário após um aumento de 15%, só para quem ganha menos que 3500.
"""

funcionarios = {
    'Ana': 3000,
    'Bruno': 2500,
    'Carlos': 4000,
    'Diana': 3500
}

aumento = {nome: salario * 1.15 for nome, salario in funcionarios.items() if salario < 3500}
print(aumento)