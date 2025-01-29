class Client:
    def __init__(self, account_number, balance, name, credit):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.credit = credit


class AVLNode:
    def __init__(self, client):
        self.client = client
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left_child) - self.height(node.right_child)

    def is_left_child_heavy(self, node):
        return self.balance_factor(node) > 1

    def is_right_child_heavy(self, node):
        return self.balance_factor(node) < -1

    def set_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left_child), self.height(node.right_child)) + 1

    def rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        new_root.left_child = node

        self.set_height(node)
        self.set_height(new_root)

        return new_root

    def rotate_right(self, node):
        new_root = node.left_child
        node.left_child = new_root.right_child
        new_root.right_child = node

        self.set_height(node)
        self.set_height(new_root)

        return new_root

    def balance_node(self, node):
        if not node:
            return node

        if self.is_left_child_heavy(node):
            if (self.balance_factor(node.left_child) < 0):
                node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        elif self.is_right_child_heavy(node):
            if (self.balance_factor(node.right_child) > 0):
                node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def insert(self, client):
        def _insert(node, client):
            if not node:
                return AVLNode(client)

            if client.account_number < node.client.account_number:
                node.left_child = _insert(node.left_child, client)
            else:
                node.right_child = _insert(node.right_child, client)

            self.set_height(node)
            return self.balance_node(node)

        self.root = _insert(self.root, client)

    def search_by_account_number(self, account_number):
        def _search(node, account_number):
            if not node:
                return None
            if account_number == node.client.account_number:
                return node.client
            if account_number < node.client.account_number:
                return _search(node.left_child, account_number)
            return _search(node.right_child, account_number)

        return _search(self.root, account_number)

    def min(self, node):
        current = node
        while current.left_child:
            current = current.left_child
        return current

    def remove_by_account_number(self, account_number):
        def _remove_by_account_number(node, account_number):
            if not node:
                return node

            if account_number < node.client.account_number:
                node.left_child = _remove_by_account_number(node.left_child, account_number)
            elif account_number > node.client.account_number:
                node.right_child = _remove_by_account_number(node.right_child, account_number)
            else:
                if not node.left_child:
                    return node.right_child
                elif not node.right_child:
                    return node.left_child

                temp = self.min(node.right_child)
                node.client = temp.client
                node.right_child = _remove_by_account_number(node.right_child, temp.client.account_number)

            return self.balance_node(node)

        self.root = _remove_by_account_number(self.root, account_number)

    def print_pre_order(self, node):
        if not node:
            return
        print(node.client)
        self.print_pre_order(node.left_child)
        self.print_pre_order(node.right_child)

    def print_in_order(self, node):
        if not node:
            return
        self.print_in_order(node.left_child)
        print(node.client)
        self.print_in_order(node.right_child)

    def print_post_order(self, node):
        if not node:
            return
        self.print_post_order(node.left_child)
        self.print_post_order(node.right_child)
        print(node.client)

    def print_tree(self):
        def _print_tree(node, level=0, prefix="Root: "):
            if not node:
                return
            print("  " * level + prefix + f"[Account: {node.client.account_number}, Name: {node.client.name}]")
            if node.left_child:
                _print_tree(node.left_child, level + 1, "L--- ")
            if node.right_child:
                _print_tree(node.right_child, level + 1, "R--- ")

        _print_tree(self.root)


def main():
    tree = AVLTree()

    clients_iniciais = [
        Client(1001, 5000.0, "Ana Silva", 2000.0),
        Client(1002, 3500.0, "Bruno Santos", 1500.0),
        Client(1003, 7000.0, "Carla Oliveira", 3000.0),
        Client(1004, 2500.0, "Daniel Lima", 1000.0),
        Client(1005, 10000.0, "Elena Costa", 5000.0),
        Client(1006, 4500.0, "Fernando Pereira", 2500.0),
        Client(1007, 6000.0, "Gabriela Souza", 2800.0),
        Client(1008, 8500.0, "Hugo Martins", 4000.0)
    ]

    for client in clients_iniciais:
        tree.insert(client)

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Cadastrar novo cliente")
        print("2. Remover cliente")
        print("3. Pesquisar cliente pelo número da conta")
        print("4. Visualizar árvore AVL")
        print("5. Sair")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            account = int(input("Número da conta corrente: "))
            balance = float(input("Saldo inicial: "))
            name = input("Nome do cliente: ")
            credit = float(input("Valor do crédito: "))

            novo_client = Client(account, balance, name, credit)
            tree.insert(novo_client)
            print("\nCliente inserido com sucesso!")

        elif option == "2":
            account_number = int(input("Número da conta corrente a ser removida: "))
            client = tree.search_by_account_number(account_number)
            if client:
                tree.remove_by_account_number(account_number)
                print("\nCliente removido com sucesso!")
            else:
                print("\nCliente não encontrado!")

        elif option == "3":
            account_number = int(input("Número da conta corrente a ser buscado: "))
            client = tree.search_by_account_number(account_number)
            if client:
                print("\nInformações do cliente:")
                print(f"Nome: {client.name}")
                print(f"Conta Corrente: {client.account_number}")
                print(f"Saldo: R$ {client.balance:.2f}")
                print(f"Crédito: R$ {client.credit:.2f}")
            else:
                print("\nCliente não encontrado!")

        elif option == "4":
            print("\nÁrvore AVL:")
            tree.print_tree()

        elif option == "5":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
