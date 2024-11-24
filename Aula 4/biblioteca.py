"""
Crie uma classe Biblioteca que
contenha várias instâncias de Playlist associadas a diferentes usuários.
Adicione métodos para gerenciar usuários (adicionar, remover, listar) e para
gerenciar as playlists de cada usuário. Implemente polimorfismo ao exibir
informações de diferentes tipos de mídias.
"""
from midia import Midia
from playlist import Playlist
from usuario import Usuario


class Biblioteca:

    def __init__(self):
        self.usuarios = []
        self.playlists = {}

    def adicionar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        self.playlists[usuario.id] = usuario.playlist

    def remover_usuario(self, usuario_id: int):
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        if usuario:
            self.usuarios.remove(usuario)
            del self.playlists[usuario_id]

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"ID: {usuario.id}, Nome: {usuario.nome}")

    def adicionar_midia_playlist(self, usuario_id: int, midia: Midia):
        usuario_playlist = self.playlists.get(usuario_id)
        if usuario_playlist:
            usuario_playlist.adicionar_midia(midia)
        else:
            raise Exception("Usuário não encontrado.")

    def remover_midia_playlist(self, usuario_id: int, midia: Midia):
        usuario_playlist = self.playlists.get(usuario_id)
        if usuario_playlist:
            usuario_playlist.remover_midia(midia)
        else:
            raise Exception("Usuário não encontrado.")

    def listar_midias_playlist(self, usuario_id: int):
        usuario_playlist = self.playlists.get(usuario_id)
        if usuario_playlist:
            print(f"Playlist de {self.get_usuario_nome(usuario_id)}:")
            usuario_playlist.exibir_informacoes()
        else:
            raise Exception("Usuário não encontrado.")

    def get_usuario_nome(self, usuario_id: int) -> str:
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        if usuario:
            return usuario.nome
        else:
            raise Exception("Usuário não encontrado.")


if __name__ == "__main__":
    midia2 = Midia("Exemplo 1", 32)
    midia3 = Midia("Exemplo 2", 34)
    midia4 = Midia("Exemplo 3", 35)

    usuario1 = Usuario(1, "Joao", Playlist([midia2, midia3]))
    usuario2 = Usuario(2, "Maria", Playlist([midia4]))

    biblioteca = Biblioteca()
    biblioteca.adicionar_usuario(usuario1)
    biblioteca.listar_usuarios()

    print("\n --------------- \n")

    biblioteca.adicionar_usuario(usuario2)
    biblioteca.listar_usuarios()

    print("\n --------------- \n")

    biblioteca.remover_usuario(1)
    biblioteca.listar_usuarios()

    print("\n --------------- \n")

    biblioteca.adicionar_midia_playlist(2, midia2)
    biblioteca.listar_midias_playlist(2)

    print("\n --------------- \n")

    biblioteca.remover_midia_playlist(2, midia4)
    biblioteca.listar_midias_playlist(2)
