"""
Crie uma classe chamada Pessoa com os atributos nome e idade. Em
seguida, crie uma subclasse chamada Funcionário que tenha um atributo
adicional chamado salário. A subclasse deve ter um metodo para aumentar o
salário em uma porcentagem fornecida.
"""


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, salario: float):
        super().__init__(nome, idade)
        self.salario = salario

    def dar_aumento(self, porcentagem: float) -> float:
        return self.salario * (1 + porcentagem)


funcionario1 = Funcionario("João", 19, 10_000.00)
print(f"Novo salário de {funcionario1.nome}: R${funcionario1.dar_aumento(0.2):.2f}.")
