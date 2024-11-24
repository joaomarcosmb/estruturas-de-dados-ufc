from veiculo import Veiculo
from pessoa import Pessoa

class Bicicleta(Veiculo):
    def __init__(self, marca: str, cor: str, pessoa: Pessoa):
        super().__init__(marca, cor, pessoa)

    def verificar_entrada(self):
        try:
            if self.pessoa and self.pessoa.cpf:
                print("Entrada permitida para a bicicleta.")
        except AttributeError:
            print("Entrada não permitida.")

    def acelerar(self):
        print("Acelerando bicicleta...")

    def parar(self):
        print("Parando bicicleta...")


pessoa = Pessoa("000.000.000-00")
veiculo = Bicicleta("Colli", "Preto", pessoa)

veiculo.verificar_entrada()
veiculo.acelerar()
veiculo.parar()