from veiculo import Veiculo
from pessoa import Pessoa

class Carro(Veiculo):
    def __init__(self, marca: str, placa: str, cor: str, qtd_passageiros: int, pessoa: Pessoa):
        super().__init__(marca, cor, pessoa)
        self.placa = placa
        self.qtd_passageiros = qtd_passageiros

    def verificar_entrada(self):
        if 1 <= self.qtd_passageiros <= 4:
            print(f"Entrada permitida para o carro de marca {self.marca} e placa {self.placa}.")
        else:
            print("Entrada não permitida.")

    def acelerar(self):
        print("Acelerando carro...")

    def ligar(self):
        print("Ligando carro...")

    def desligar(self):
        print("Desligando carro...")

    def parar(self):
        print("Parando carro...")


pessoa = Pessoa("000.000.000-00")
veiculo = Carro("Volkswagen", "ABC6DE", "Preto", 4, pessoa)

veiculo.verificar_entrada()
veiculo.acelerar()
veiculo.parar()
veiculo.ligar()
veiculo.desligar()