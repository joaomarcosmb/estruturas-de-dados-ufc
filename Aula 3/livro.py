"""
Crie uma classe Livro com os atributos título, autor e ano. A classe deve
ter um metodo descrever que exiba uma descrição do livro. Em seguida, crie uma
subclasse Ebook que tenha um atributo adicional tamanho_arquivo e sobrescreva
o metodo descrever para incluir o tamanho do arquivo.
"""


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descrever(self):
        return f"Título: {self.titulo} \nAutor: {self.autor} \nAno: {self.ano}"


class Ebook(Livro):
    def __init__(self, titulo: str, autor: str, ano: int, tamanho_arquivo: int):
        super().__init__(titulo, autor, ano)
        self.tamanho_arquivo = tamanho_arquivo

    def descrever(self):
        return f"Título: {self.titulo} \nAutor: {self.autor} \nAno: {self.ano} \nTamanho do arquivo: {self.tamanho_arquivo} MBs"


livro1 = Livro("Crônicas de Fogo e Gelo Vol. 1", "George R. R. Martin", 1996)
print(livro1.descrever())

print("\n")

livro2 = Ebook("O Senhor dos Anéis", "J. R. R. Tolkien", 1954, 10)
print(livro2.descrever())
