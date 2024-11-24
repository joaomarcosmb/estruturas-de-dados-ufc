"""
Crie uma classe Usuario com atributos nome, id e playlist
(que será uma instância da classe Playlist). Adicione métodos para adicionar
e remover mídias da playlist do usuário, e um método para exibir a playlist
do usuário.

"""
from midia import Midia
from playlist import Playlist


class Usuario:
    def __init__(self, id: int, nome: str, playlist: Playlist):
        self.id = id
        self.nome = nome
        self.playlist = playlist

    def adicionar_midia(self, midia: Midia):
        self.playlist.adicionar_midia(midia)

    def remover_midia(self, midia: Midia):
        self.playlist.remover_midia(midia)

    def exibir_playlist_usuario(self):
        print(f"Playlist de {self.nome}:")
        self.playlist.exibir_informacoes()

if __name__ == "__main__":
    midiaA = Midia("Exemplo A", 42)
    midiaB = Midia("Exemplo B", 44)
    midiaC = Midia("Exemplo C", 45)
    
    lista = [midiaA, midiaB]
    
    playlist1 = Playlist(lista)
    
    user1 = Usuario(1, "João", playlist1)
    user1.exibir_playlist_usuario()
    
    print("-----------")
    
    user1.adicionar_midia(midiaC)
    user1.exibir_playlist_usuario()
    
    print("-----------")
    
    user1.remover_midia(midiaA)
    user1.exibir_playlist_usuario()