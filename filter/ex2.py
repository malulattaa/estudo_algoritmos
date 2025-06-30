nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eva"]
notas = [8.5, 5.9, 7.0, 6.8, 9.2]

filtro = list(map(lambda item: f"{item[0]} - {item[1]}",filter(lambda item: item[1] > 7, zip(nomes, notas))))
for f in filtro:
    print (f)

""" 
Junte os nomes e notas usando zip().

Filtre os alunos com nota maior ou igual a 7.

Formate usando map() para gerar strings como:
"Ana - 8.5"


"""

