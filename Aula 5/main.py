class Midia:
    def __init__(self, titulo: str, duracao: int):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self) -> None:
        print(f"Título: {self.titulo} \nDuração: {self.duracao} min")


class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def exibir_informacoes(self) -> None:
        super().exibir_informacoes()
        print(f"Resolução: {self.resolucao}")


class Audio(Midia):
    def __init__(self, titulo: str, duracao: int, formato: str):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibir_informacoes(self) -> None:
        super().exibir_informacoes()
        print(f"Formato: {self.formato}")


class Foto(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str, formato: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
        self.formato = formato

    def exibir_informacoes(self) -> None:
        super().exibir_informacoes()
        print(f"Resolução: {self.resolucao} \nFormato: {self.formato}")


class Playlist:
    def __init__(self, midias: list[Midia] = None):
        if midias is None:
            midias = []
        self.midias = midias

    def adicionar_midia(self, posicao: int, midia: Midia) -> None:
        self.midias.insert(posicao, midia)

    def procurar_posicao_midia(self, nome_midia: str) -> int | None:
        for i, midia in enumerate(self.midias):
            if midia.titulo == nome_midia:
                return i + 1
        return None

    def remover_midia(self, midia: Midia) -> None:
        self.midias.remove(midia)

    def exibir_informacoes(self) -> None:
        for midia in self.midias:
            midia.exibir_informacoes()
            print("-----------")

    def lista_ordenada(self):
        ordenada = sorted(self.midias, key=lambda m: m.duracao)

        for midia in ordenada:
            midia.exibir_informacoes()
            print("-----------")

    def lista_sem_duplicatas(self):
        nova_lista = list(set(self.midias))

        for midia in nova_lista:
            midia.exibir_informacoes()
            print("-----------")


class Usuario:
    def __init__(self, id: int, nome: str, playlist: Playlist):
        self.id = id
        self.nome = nome
        self.playlist = playlist

    def adicionar_midia(self, midia: Midia, posicao: int) -> None:
        self.playlist.adicionar_midia(posicao, midia)

    def procurar_posicao_midia(self, midia: str):
        return self.playlist.procurar_posicao_midia(midia)

    def lista_ordenada(self):
        self.playlist.lista_ordenada()

    def lista_sem_duplicatas(self):
        self.playlist.lista_sem_duplicatas()

    def remover_midia(self, midia: Midia) -> None:
        self.playlist.remover_midia(midia)

    def exibir_playlist_usuario(self) -> None:
        print(f"Playlist de {self.nome}:")
        self.playlist.exibir_informacoes()


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    playlist = Playlist()
    usuario = Usuario(1, nome, playlist)
    return usuario

def cadastrar_video():
    titulo = input("Digite o título do vídeo: ")
    duracao = int(input("Digite a duração do vídeo (em minutos): "))
    resolucao = input("Digite a resolução do vídeo: ")
    return Video(titulo, duracao, resolucao)


def cadastrar_audio():
    titulo = input("Digite o título do áudio: ")
    duracao = int(input("Digite a duração do áudio (em minutos): "))
    formato = input("Digite o formato do áudio: ")
    return Audio(titulo, duracao, formato)


def cadastrar_foto():
    titulo = input("Digite o título da foto: ")
    resolucao = input("Digite a resolução da foto: ")
    formato = input("Digite o formato da foto: ")
    return Foto(titulo, 0, resolucao, formato)


def exibir_menu():
    print("\n------- Gerenciador de Playlists -------\n")
    print("\nEscolha uma opção:")
    print("1 - Adicionar vídeo")
    print("2 - Adicionar áudio")
    print("3 - Adicionar foto")
    print("4 - Remover mídia")
    print("5 - Listar playlist")
    print("6 - Sair")
    return input("Escolha uma opção: ")


if __name__ == "__main__":
    print("Bem-vindo ao Gerenciador de Playlists!")

    # Cadastro do usuário
    try:
        usuario = cadastrar_usuario()
        print(f"\nUsuário {usuario.nome} cadastrado com sucesso!\n")
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        exit(1)

    while True:
        try:
            opcao = exibir_menu()

            if opcao == "1":
                video = cadastrar_video()
                usuario.adicionar_midia(video)
                print("\nVídeo adicionado à playlist com sucesso!")

            elif opcao == "2":
                audio = cadastrar_audio()
                usuario.adicionar_midia(audio)
                print("\nÁudio adicionado à playlist com sucesso!")

            elif opcao == "3":
                foto = cadastrar_foto()
                usuario.adicionar_midia(foto)
                print("\nFoto adicionada à playlist com sucesso!")

            elif opcao == "4":
                if not usuario.playlist.midias:
                    print("\nA playlist está vazia!")
                    continue
                    
                titulo = input("Digite o título da mídia que deseja remover: ")
                midia_removida = None
                
                for midia in usuario.playlist.midias:
                    if midia.titulo.lower() == titulo.lower():
                        midia_removida = midia
                        break
                
                if midia_removida:
                    usuario.playlist.midias.remove(midia_removida)
                    print(f"\nMídia '{titulo}' removida com sucesso!")
                else:
                    print(f"\nMídia '{titulo}' não encontrada na playlist!")

            elif opcao == "5":
                if not usuario.playlist.midias:
                    print("\nA playlist está vazia!")
                else:
                    print("\nMídias na playlist:")
                    for midia in usuario.playlist.midias:
                        print(f"- {midia.titulo} ({type(midia).__name__})")

            elif opcao == "6":
                print("\nObrigado por usar o Gerenciador de Playlists!")
                break

            else:
                print("\nOpção inválida! Por favor, escolha uma opção válida.")

        except Exception as e:
            print(f"\nErro: {e}")
            print("Por favor, tente novamente.")