"""
Crie um sistema de gerenciamento de biblioteca que permita adicionar
livros, verificar a disponibilidade e realizar empréstimos. A classe Livro deve ter
atributos como titulo, autor e disponibilidade. A classe Biblioteca deve gerenciar
uma coleção de livros e permitir adicionar novos livros, emprestar livros (mudando
sua disponibilidade) e exibir os livros disponíveis.
"""


class Livro:
    def __init__(self, titulo: str, autor: str, disponibilidade: bool):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade


class Biblioteca:
    def __init__(self, livros: list[Livro]):
        self.livros = livros

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo: str):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponibilidade:
                    livro.disponibilidade = False
                    return f"{livro.titulo} emprestado com sucesso."
                else:
                    return f"{livro.titulo} não está disponível no momento."
        return "Livro não encontrado."

    def exibir_livros_disponiveis(self):
        print("---------------------")
        print("Disponibilidade dos livros:\n")
        for livro in self.livros:
            if livro.disponibilidade:
                print(f"Título: {livro.titulo} \nAutor: {livro.autor} \nDisponibilidade: Disponível\n")
            else:
                print(f"Título: {livro.titulo} \nAutor: {livro.autor} \nDisponibilidade: Indisponível\n")


livro1 = Livro("Crônicas de Fogo e Gelo Vol. 1", "George R. R. Martin", False)
livro2 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", True)
livro3 = Livro("O Hobbit", "J. R. R. Tolkien", True)

biblioteca = Biblioteca([livro1, livro2, livro3])
livro4 = Livro("Crônicas de Fogo e Gelo Vol. 2", "George R. R. Martin", True)
biblioteca.adicionar_livro(livro4)

print("\n")

print(biblioteca.emprestar_livro("Crônicas de Fogo e Gelo Vol. 1"))
print(biblioteca.emprestar_livro("O Senhor dos Anéis"))

print("\n")

biblioteca.exibir_livros_disponiveis()