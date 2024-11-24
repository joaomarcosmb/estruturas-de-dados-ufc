"""
Crie uma classe chamada Cachorro que tenha dois atributos: nome e
idade. A classe deve ter um metodo chamado latir que imprime uma mensagem
com o nome do cachorro.
"""


class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f'{self.nome} está latindo!')


tobby = Cachorro("Tobby", 3)
tobby.latir()
