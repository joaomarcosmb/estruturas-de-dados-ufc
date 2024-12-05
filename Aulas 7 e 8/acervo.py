from datetime import datetime, timedelta


class Livro:

    def __init__(self, id, nome, data_devolucao=None):
        self.id = id
        self.nome = nome
        self.data_devolucao = data_devolucao
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Data de devolução: {self.data_devolucao}"


class Acervo:

    def __init__(self):
        self.head = None
        self.tail = None
        self.inicializar_acervo()

    def inicializar_acervo(self):
        livros_iniciais = [("1", "Livro 1"), ("2", "Livro 2"), ("3", "Livro 3"),
                           ("4", "Livro 4"), ("5", "Livro 5"), ("6", "Livro 6"),
                           ("7", "Livro 7"), ("8", "Livro 8"), ("9", "Livro 9"),
                           ("10", "Livro 10")]

        livro_anterior = None
        for id, nome in livros_iniciais:
            novo_livro = Livro(id, nome)

            if self.head is None:
                self.head = novo_livro
            else:
                livro_anterior.proximo = novo_livro
                novo_livro.anterior = livro_anterior

            livro_anterior = novo_livro

        self.tail = livro_anterior

    def buscar_livro_por_id(self, id):
        head_atual = self.head
        tail_atual = self.tail

        while head_atual and tail_atual and head_atual is not tail_atual:
            if head_atual.id == id:
                print("Livro encontrado:")
                print(head_atual)
                return head_atual

            if tail_atual.id == id:
                print("Livro encontrado:")
                print(tail_atual)
                return tail_atual

            head_atual = head_atual.proximo
            tail_atual = tail_atual.anterior

        print("Livro não encontrado.")
        return

    def adicionar_livro_fim(self, id, nome):
        novo_livro = Livro(id, nome)

        if not self.head:
            self.head = novo_livro
            self.tail = novo_livro
            return

        self.tail.proximo = novo_livro
        novo_livro.anterior = self.tail
        self.tail = novo_livro

    def ordenar_lista_por_id(self):
        if not self.head or not self.head.proximo:
            return

        sorted = False
        while not sorted:
            sorted = True
            atual = self.head
            while atual and atual.proximo:
                if int(atual.id) > int(atual.proximo.id):
                    sorted = False
                    proximo = atual.proximo

                    if atual.anterior:
                        atual.anterior.proximo = proximo
                    else:
                        self.head = proximo

                    if proximo.proximo:
                        proximo.proximo.anterior = atual
                    else:
                        self.tail = atual

                    atual.proximo = proximo.proximo
                    proximo.anterior = atual.anterior
                    proximo.proximo = atual
                    atual.anterior = proximo
                atual = atual.proximo

    def alugar_livro(self, id, dias):
        livro = self.buscar_livro_por_id(id)
        if livro:
            livro.data_devolucao = (datetime.now() +
                                    timedelta(days=dias)).strftime("%d/%m/%Y")
            print("Livro alugado com sucesso.")
        else:
            print("Livro não encontrado.")

    def remover_livro(self, id):
        atual = self.buscar_livro_por_id(id)

        if atual is None:
            return

        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.head = atual.proximo

        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.tail = atual.anterior

        print("Livro removido com sucesso.")

    def primeiro_livro(self):
        return self.head

    def exibir_acervo(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo
