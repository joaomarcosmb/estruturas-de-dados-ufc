"""
Crie uma classe ServicoStreaming com atributos nome
e usuarios (uma lista de objetos Usuario). Adicione métodos para gerenciar
os usuários, fazer upload de mídias, e realizar streaming de mídias. Adicione
um método para exibir o relatório de uso, mostrando quantas vezes cada tipo
de mídia foi exibida por cada usuário.
"""
from midia import Midia
from playlist import Playlist
from usuario import Usuario


class ServicoStreaming:
    def __init__(self, nome: str, usuarios: list[Usuario]):
        self.nome = nome
        self.usuarios = usuarios

    def adicionar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def remover_usuario(self, usuario: Usuario) -> None:
        self.usuarios.remove(usuario)

    def upload_midia(self, usuario_id: int, midia: Midia) -> None:
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        if usuario:
            usuario.adicionar_midia(midia)
        else:
            raise Exception("Usuário não encontrado.")

    def streaming(self, usuario_id: int, midia: Midia) -> None:
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        if usuario:
            print(f"Reproduzindo {midia.titulo} para o usuário {usuario.nome}...")
            midia.reproducoes += 1
        else:
            raise Exception("Usuário não encontrado.")

    def exibir_relatorio(self) -> None:
        for usuario in self.usuarios:
            print(f"Relatório de uso de {usuario.nome}:")
            for midia in usuario.playlist.midias:
                print(f"{midia.titulo}: {midia.reproducoes} reproduções")
            print("\n ------------ \n")


if __name__ == "__main__":
    midiaA = Midia("Exemplo A", 42)
    midiaB = Midia("Exemplo B", 44)
    midiaC = Midia("Exemplo C", 45)

    lista = [midiaA, midiaB]

    playlist1 = Playlist(lista)

    user1 = Usuario(1, "João", playlist1)

    midiaD = Midia("Exemplo D", 46)
    midiaE = Midia("Exemplo E", 47)

    user2 = Usuario(2, "Maria", Playlist([midiaD, midiaE]))

    servico = ServicoStreaming("Netflix", [user1, user2])

    servico.exibir_relatorio()

    print("-----------")

    servico.upload_midia(1, midiaC)
    servico.streaming(1, midiaC)
    servico.streaming(1, midiaC)
    servico.streaming(1, midiaC)

    servico.exibir_relatorio()

    print("-----------")

    servico.upload_midia(2, midiaA)
    servico.streaming(2, midiaA)
    servico.streaming(2, midiaA)

    servico.exibir_relatorio()

    print("-----------")

    servico.remover_usuario(user1)

    servico.exibir_relatorio()