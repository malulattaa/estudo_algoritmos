""" 
Dada uma lista de tuplas representando alunos e suas médias finais:


📌 Use filter() para gerar uma lista com apenas 
os alunos aprovados (média >= 7), 
e que tenham nomes com mais de 4 letras.
"""

alunos = [
    ("Ana", 8.5),
    ("Bruno", 5.9),
    ("Carlos", 7.0),
    ("Diana", 6.8),
    ("Eva", 9.2)
]

filtrando = list(filter(lambda item: len(item[0]) > 4 and item[1] >= 7, alunos))
print(filtrando)