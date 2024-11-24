from pessoa import Pessoa


class Veiculo:
    def __init__(self, marca: str, cor: str, pessoa: Pessoa):
        self.marca = marca
        self.cor = cor
        self.pessoa = pessoa

    def verificar_entrada(self):
        try:
            if self.pessoa and self.pessoa.cpf:
                print(f"Entrada permitida para o veículo {self.marca} de placa {self.placa}.")
        except AttributeError:
            print("Entrada não permitida.")

    def acelerar(self):
        print("Acelerando...")

    def parar(self):
        print("Parando...")
