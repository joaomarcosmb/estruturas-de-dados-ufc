from acervo import Acervo


class Usuario:

  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
    self.anterior = None
    self.proximo = None

  def __str__(self):
    return f"ID: {self.id} | Nome: {self.nome}"


class Biblioteca:

  def __init__(self):
    self.users_head = None
    self.users_tail = None
    self.acervo = Acervo()
    self.inicializar_biblioteca()

  def inicializar_biblioteca(self):
    usuarios_iniciais = [("1", "Usuario 1"), ("2", "Usuario 2"),
                         ("3", "Usuario 3"), ("4", "Usuario 4"),
                         ("5", "Usuario 5"), ("6", "Usuario 6")]

    usuario_anterior = None
    for id, nome in usuarios_iniciais:
      novo_usuario = Usuario(id, nome)

      if self.users_head is None:
        self.users_head = novo_usuario
      else:
        usuario_anterior.proximo = novo_usuario
        novo_usuario.anterior = usuario_anterior

      usuario_anterior = novo_usuario

    self.users_tail = usuario_anterior

  def buscar_usuario_por_id(self, id):
    head_atual = self.users_head
    tail_atual = self.users_tail

    while head_atual and tail_atual and head_atual is not tail_atual:
      if head_atual.id == id:
        print("Usuário encontrado:")
        print(head_atual)
        return head_atual

      if tail_atual.id == id:
        print("Usuário encontrado:")
        print(tail_atual)
        return tail_atual

      head_atual = head_atual.proximo
      tail_atual = tail_atual.anterior

    print("Usuário não encontrado.")
    return

    
  def adicionar_usuario_fim(self, id, nome):
    novo_usuario = Usuario(id, nome)

    if not self.users_head:
      self.users_head = novo_usuario
      self.users_tail = novo_usuario
      return

    self.users_tail.proximo = novo_usuario
    novo_usuario.anterior = self.users_tail
    self.users_tail = novo_usuario

  def remover_usuario(self, id):
    atual = self.buscar_usuario_por_id(id)

    if atual is None:
      return

    if atual.anterior:
      atual.anterior.proximo = atual.proximo
    else:
      self.users_head = atual.proximo

    if atual.proximo:
      atual.proximo.anterior = atual.anterior
    else:
      self.users_tail = atual.anterior

    print("Usuário removido com sucesso.")

  def primeiro_usuario(self):
    return self.users_head

  def exibir_usuarios(self):
    atual = self.users_head
    while atual:
      print(atual)
      atual = atual.proximo
