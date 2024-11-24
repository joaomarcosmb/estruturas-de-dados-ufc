from veiculo import Veiculo
from pessoa import Pessoa

class Moto(Veiculo):
    def __init__(self, marca: str, placa: str, cor: str, qtd_passageiros: int, pessoa: Pessoa):
        super().__init__(marca, cor, pessoa)
        self.placa = placa
        self.qtd_passageiros = qtd_passageiros

    def verificar_entrada(self):
        if 1 <= self.qtd_passageiros <= 2:
            print(f"Entrada permitida para a moto de marca {self.marca} e placa {self.placa}.")
        else:
            print("Entrada não permitida.")

    def acelerar(self):
        print("Acelerando moto...")

    def ligar(self):
        print("Ligando moto...")

    def desligar(self):
        print("Desligando moto...")

    def parar(self):
        print("Parando moto...")


pessoa = Pessoa("000.000.000-00")
veiculo = Moto("Yamaha", "ABC6DE", "Preto", 2, pessoa)

veiculo.verificar_entrada()
veiculo.acelerar()
veiculo.parar()
veiculo.ligar()
veiculo.desligar()