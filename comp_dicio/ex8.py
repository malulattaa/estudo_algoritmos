""" 
Atualize o dicionário alunos para substituir a média dos alunos com as novas notas.
"""

alunos = {
    1: {'nome': 'Ana', 'media': 6.5},
    2: {'nome': 'Bruno', 'media': 7.8},
    3: {'nome': 'Carla', 'media': 9.0}
}

novas_notas = {
    1: 7.5,
    3: 8.5
}



for id, nova_media in novas_notas.items():
    if id in alunos:
        alunos[id]['media'] = nova_media
        

for id, dados in alunos.items():
    print(f"ID: {id}")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    print()
