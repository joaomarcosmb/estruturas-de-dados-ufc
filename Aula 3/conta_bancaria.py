"""
Pergunta: Crie uma classe chamada Conta_Bancaria que tenha os atributos
titular, saldo e numero. A classe deve ter os métodos depositar e sacar. O metodo
depositar deve adicionar um valor ao saldo, e o metodo sacar deve subtrair um
valor do saldo apenas se houver fundos suficientes.
"""


class ContaBancaria:
    def __init__(self, titular: str, saldo: float, numero: str):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self, valor: float) -> str:
        self.saldo += valor
        return f"Depósito de R${valor:.2f} feito com sucesso. Saldo atual: R${self.saldo:.2f}."

    def sacar(self, valor: float) -> str:
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} feito com success. Saldo atual: R${self.saldo:.2f}."
        else:
            return "Saldo insuficiente."


conta1 = ContaBancaria("João Marcos", 1_000_000.00, "1234-0")
print(conta1.depositar(200))
print(conta1.sacar(100))
