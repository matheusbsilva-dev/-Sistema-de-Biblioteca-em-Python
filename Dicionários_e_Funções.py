bioblioteca = [{'titulo': "pequeno principe",
               'autor': 'Antoine de Saint-Exupéry',
               'ano': 1943 }]
#adiciona um livro novo
def registrar_livro (titulo,autor,ano):
    bioblioteca.append({ 'titulo':titulo,'autor':autor,'ano': ano})
registrar_livro('1984','george orwell',1949)
print(bioblioteca)
#funçao que faz exibir o livro
def exibir_livro(livro):
    print(f"titulo: {livro['titulo']}")
    print(f"autor: {livro['autor']}")
    print(f"ano: {livro['ano']}")
for livro in bioblioteca:
    exibir_livro(livro)
