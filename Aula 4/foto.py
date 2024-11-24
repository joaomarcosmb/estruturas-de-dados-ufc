"""
Crie uma subclasse Foto que herda de Midia e adiciona
atributos resolucao e formato. Adicione um método exibir_informacoes que
imprime o título, a duração, a resolução e o formato da foto.
"""

from midia import Midia

class Foto(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str, formato: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
        self.formato = formato

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Resolução: {self.resolucao} \nFormato: {self.formato}")


if __name__ == "__main__":
    midia2 = Foto("Aula 1", 0, "1080p", "JPEG")
    midia2.exibir_informacoes()        