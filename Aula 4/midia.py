"""
Crie uma classe chamada Midia com atributos titulo e
duracao. Adicione um método exibir_informacoes que imprime o título e a
duração da mídia.
"""

class Midia:
    def __init__(self, titulo: str, duracao: int, reproducoes: int = 0):
        self.titulo = titulo
        self.duracao = duracao
        self.reproducoes = reproducoes

    def exibir_informacoes(self):
        print(f"Título: {self.titulo} \nDuração: {self.duracao} min")

if __name__ == "__main__":
    midia1 = Midia("Aula 1", 60)
    midia1.exibir_informacoes()