from acervo import Acervo
from biblioteca import Biblioteca


def menu():
  print("\nMenu:")
  print("1. Exibir acervo")
  print("2. Buscar livro por ID")
  print("3. Adicionar livro ao acervo")
  print("4. Alugar livro")
  print("5. Remover livro do acervo")
  print("6. Exibir usuários")
  print("7. Buscar usuário por ID")
  print("8. Cadastrar usuário")
  print("9. Remover usuário")
  print("10. Sair")
  return int(input("Sua escolha: "))


def main():
  while True:
    opcao = menu()

    if opcao == 1:
      acervo = Acervo()
      acervo.exibir_acervo()
    elif opcao == 2:
      id = input("Digite o ID do livro: ")
      acervo = Acervo()
      acervo.buscar_livro_por_id(id)
    elif opcao == 3:
      id = input("Digite o ID do livro: ")
      nome = input("Digite o nome do livro: ")
      acervo = Acervo()
      acervo.adicionar_livro_fim(id, nome)
    elif opcao == 4:
      id = input("Digite o ID do livro: ")
      dias = int(input("Digite a quantidade de dias para alugar: "))
      acervo = Acervo()
      acervo.alugar_livro(id, dias)
    elif opcao == 5:
      id = input("Digite o ID do livro: ")
      acervo = Acervo()
      acervo.remover_livro(id)
    elif opcao == 6:
      biblioteca = Biblioteca()
      biblioteca.exibir_usuarios()
    elif opcao == 7:
      id = input("Digite o ID do usuário: ")
      biblioteca = Biblioteca()
      biblioteca.buscar_usuario_por_id(id)
    elif opcao == 8:
      id = input("Digite o ID do usuário: ")
      nome = input("Digite o nome do usuário: ")
      biblioteca = Biblioteca()
      biblioteca.adicionar_usuario_fim(id, nome)
    elif opcao == 9:
      id = input("Digite o ID do usuário: ")
      biblioteca = Biblioteca()
      biblioteca.remover_usuario(id)
    elif opcao == 10:
      print("Saindo...")
      break


if __name__ == "__main__":
  main()
