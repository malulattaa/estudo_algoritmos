def placeholders(texto, **kwargs):
    return texto.format(**kwargs)
    
texto = input("Digite um texto com placeholders: ")

nome = input("Digite o nome: ")
cidade = input("Digite a cidade: ")

print(placeholders(texto, nome = nome, cidade = cidade))