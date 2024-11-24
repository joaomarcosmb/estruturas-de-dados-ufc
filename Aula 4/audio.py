"""
Crie uma subclasse Audio que herda de Midia e adiciona um
atributo formato. Adicione um método exibir_informacoes que imprime o
título, a duração e o formato do áudio.
"""

from midia import Midia


class Audio(Midia):
    def __init__(self, titulo: str, duracao: int, formato: str):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibir_informacoes(self):
        print(f"Formato: {self.formato}")


if __name__ == "__main__":
    midia2 = Audio("Aula 1", 60, ".mp3")
    midia2.exibir_informacoes()        