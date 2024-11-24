"""
Crie uma subclasse Podcast que herda de Audio e adiciona
um atributo episodio. Adicione um método exibir_informacoes que imprime
o título, a duração, o formato e o número do episódio do podcast.
"""
from audio import Audio


class Podcast(Audio):
    def __init__(self, episodio: str, titulo: str, duracao: int, formato: str):
        super().__init__(titulo, duracao, formato)
        self.episodio = episodio

    def exibir_informacoes(self):
        print(f"Episódio: {self.episodio}")


if __name__ == "__main__":
    podcast1 = Podcast("Ep1", "Título", 34, ".mp4")
    podcast1.exibir_informacoes()