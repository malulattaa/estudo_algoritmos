""" 
Crie um programa que cadastre livros em uma biblioteca. Para cada livro, armazene:

ID automático

Título

Autor

Ano de publicação

Depois, mostre:

Todos os livros cadastrados
Apenas os livros de um autor específico (usuário informa o autor)
O livro mais antigo da coleção
"""
i = 1
livros = dict()
cadastro = int(input("Deseja cadastrar quantos livros? "))
id_livro = 1

while i <= cadastro:
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    
    livros[id_livro] = {
        'titulo' : titulo,
        'autor' : autor,
        'ano' : ano,
    }
    
    id_livro += 1
    
    i += 1

#mostra todos os livros
for id, dados in livros.items():
    print(f"ID: {id}")
    for c, v in dados.items():
        print(f"{c}:{v}")
        
buscar_autor = input("Nome do autor que deseja buscar: ")
for id, dados in livros.items():
    if dados['autor'] == buscar_autor:
        print(dados['titulo'])
        print(dados['ano'])
        print(dados['autor'])
    
antigo = min(livros.items(), key=lambda item: item[1]['ano'] )
print(f"Mais antigo: {antigo[1]['titulo']} em {antigo[1]['ano']}")