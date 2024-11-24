"""
Crie uma subclasse Video que herda de Midia e adiciona um
atributo resolucao. Adicione um método exibir_informacoes que imprime o
título, a duração e a resolução do vídeo.
"""

from midia import Midia


class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def exibir_informacoes(self):
        print(f"Resolução: {self.resolucao}")


if __name__ == "__main__":
    midia2 = Video("Aula 1", 60, "1080p")
    midia2.exibir_informacoes()        