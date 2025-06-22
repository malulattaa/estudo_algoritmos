""" 
Função que receba uma lista de nomes e retorne só os nomes com mais de 5 letras
Nome: filtrar_nomes

"""


def filtrar_nome(nomes):
    filtro = list(filter(lambda x: x if len(x) > 5 else None, nomes))
    return filtro


print(filtrar_nome(["Ana", "Bruno", "Carla", "Alexandre"]))