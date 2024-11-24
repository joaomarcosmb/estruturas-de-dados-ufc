"""
Crie uma classe Playlist que contenha uma lista de objetos
Midia. Adicione métodos para adicionar e remover mídias, e um método para
exibir as informações de todas as mídias na playlist.
"""

from midia import Midia

class Playlist:
    def __init__(self, midias: list[Midia]):
        self.midias = midias

    def adicionar_midia(self, midia: Midia) -> None:
        self.midias.append(midia)

    def remover_midia(self, midia: Midia) -> None:
        self.midias.remove(midia)

    def exibir_informacoes(self) -> None:
        for midia in self.midias:
            midia.exibir_informacoes()


if __name__ == "__main__":
    midia2 = Midia("Exemplo 1", 32)
    midia3 = Midia("Exemplo 2", 34)
    midia4 = Midia("Exemplo 3", 35)
    
    lista = [midia2, midia3]
    
    playlist1 = Playlist(lista)
    playlist1.exibir_informacoes()
    
    print("-----------")
    
    playlist1.adicionar_midia(midia4)
    playlist1.exibir_informacoes()
    
    print("-----------")
    
    playlist1.remover_midia(midia2)
    playlist1.exibir_informacoes()