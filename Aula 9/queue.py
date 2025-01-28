class Usuario:

    def __init__(self, nome, conta, saldo, credito):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        self.credito = credito

        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"Nome: {self.nome} | Conta: {self.conta} | Saldo: {self.saldo} | Crédito: {self.credito}"


class Banco:

    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0
        self.inicializar_clientes()

    def inicializar_clientes(self):
        clientes_iniciais = [("João", "123", 1000, 500),
                             ("Giovana", "101", 2000, 1000),
                             ("Vitor", "721", 3000, 1500)]

        cliente_anterior = None
        for nome, conta, saldo, credito in clientes_iniciais:
            novo_cliente = Usuario(nome, conta, saldo, credito)

            if self.head is None:
                self.head = novo_cliente
            else:
                cliente_anterior.proximo = novo_cliente
                novo_cliente.anterior = cliente_anterior

            cliente_anterior = novo_cliente
            self.tamanho += 1

        self.tail = cliente_anterior

    def exibir_clientes(self):
        if not self.head:
            print("Nenhum cliente cadastrado.")
            return

        atual = self.head
        print(f"\nListagem de clientes ({self.tamanho_lista()}):")
        while atual:
            print(atual)
            atual = atual.proximo

    def buscar_cliente_por_conta(self, conta):
        if not self.head:
            return None

        atual = self.head
        while atual:
            if atual.conta == conta:
                print("Cliente encontrado:")
                print(atual)
                return atual
            atual = atual.proximo

        return

    def cadastrar_cliente(self, nome, conta, saldo, credito):
        novo_cliente = self.buscar_cliente_por_conta(conta)

        if novo_cliente:
            print("Cliente já cadastrado.")
            return

        novo_cliente = Usuario(nome, conta, saldo, credito)

        if self.head is None:
            self.head = novo_cliente
        else:
            self.tail.proximo = novo_cliente
            novo_cliente.anterior = self.tail

        self.tail = novo_cliente
        self.tamanho += 1

        print("Cliente cadastrado com sucesso.")

    def ordernar_clientes_por_credito(self, asc=False):
        if not self.head or not self.head.proximo:
            return

        trocado = True
        while trocado:
            trocado = False
            atual = self.head

            while atual and atual.proximo:
                deve_trocar = (asc and float(atual.credito) > float(
                    atual.proximo.credito)) or (not asc and float(
                        atual.credito) < float(atual.proximo.credito))

                if deve_trocar:
                    proximo = atual.proximo
                    anterior = atual.anterior
                    proximo_proximo = proximo.proximo

                    if anterior:
                        anterior.proximo = proximo
                    else:
                        self.head = proximo

                    if proximo_proximo:
                        proximo_proximo.anterior = atual
                    else:
                        self.tail = atual

                    atual.proximo = proximo_proximo
                    proximo.anterior = anterior
                    proximo.proximo = atual
                    atual.anterior = proximo

                    atual = proximo
                    trocado = True
                else:
                    atual = atual.proximo

        self.exibir_clientes()

    def excluir_cliente(self):
        if self.head:
            cliente_excluido = self.head
            self.head = self.head.proximo

            if self.head:
                self.head.anterior = None
            else:
                self.tail = None

            self.tamanho -= 1
            print(f"Cliente {cliente_excluido.nome} excluído.")

    def tamanho_lista(self):
        return self.tamanho


def menu():
    print("\nMenu:")
    print("1 - Listar clientes")
    print("2 - Ordenar clientes por crédito")
    print("3 - Cadastrar cliente")
    print("4 - Excluir cliente")
    print("5 - Exibir quantidade de clientes")
    print("6 - Sair")
    return int(input("\nDigite a opção desejada: "))


def main():
    banco = Banco()

    print("\n-------- Seja bem-vindo(a) ao Banco Brasil! --------")

    while True:
        opcao = menu()

        if opcao == 1:
            banco.exibir_clientes()
        elif opcao == 2:
            ordem = input("Deseja ordenar em ordem crescente? (S/N): ")
            banco.ordernar_clientes_por_credito(ordem.lower() == "s")
        elif opcao == 3:
            nome = input("Digite o nome do cliente: ")
            conta = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo do cliente: "))
            credito = float(input("Digite o crédito do cliente: "))
            banco.cadastrar_cliente(nome, conta, saldo, credito)
        elif opcao == 4:
            banco.excluir_cliente()
        elif opcao == 5:
            print(f"Há {banco.tamanho_lista()} cliente(s) cadastrado(s).")
        elif opcao == 6:
            print("Obrigado por utilizar o Banco Brasil!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
