def vagas_disponiveis(estacionamento: dict) -> int:
    return estacionamento["total_vagas"] - estacionamento["vagas_ocupadas"]


class EstacionamentoIguatemi:
    def __init__(self, estacionamentos: list[dict]):
        self.estacionamentos = []
        for estacionamento in estacionamentos:
            self.estacionamentos.append({
                "codigo": estacionamento["codigo"],
                "total_vagas": estacionamento["total_vagas"],
                "vagas_ocupadas": estacionamento["vagas_ocupadas"]
            })

    def listar_estacionamentos(self):
        for estacionamento in self.estacionamentos:
            print(
                f'Estacionamento {estacionamento["codigo"]}: {estacionamento["vagas_ocupadas"]}/{estacionamento["total_vagas"]} vagas ocupadas.')

    def contar_lotados(self) -> int:
        """
        Conta quantos estacionamentos estão lotados.
        Para cada iteração do laço, verifica se a quantidade de vagas ocupadas é maior ou igual ao total de vagas. Se for, incrementa o contador.
        :return: Número de estacionamentos lotados.
        """
        return sum([estacionamento["vagas_ocupadas"] >= estacionamento["total_vagas"] for estacionamento in self.estacionamentos])

    def adicionar_carros(self, carros_entrada: int) -> int:
        """
        Adiciona carros aos estacionamentos. Inicia-se assumindo que nenhum carro consegue estacionar.
        Itera-se sobre cada estacionamento e verifica-se se a quantidade de carros que não conseguiram estacionar é maior que a quantidade de vagas disponíveis no estacionamento. Se for, o estacionamento é lotado e a quantidade de carros que não conseguiram estacionar é decrementada. Caso contrário, a quantidade de carros que não conseguiram estacionar é zerada e o laço é interrompido.
        :param carros_entrada: Número de carros que estão tentando estacionar.
        :return: Número de carros que não conseguiram estacionar.
        """
        carros_fora = carros_entrada
        for est in self.estacionamentos:
            vagas_restantes = vagas_disponiveis(est)
            if carros_fora > vagas_restantes:
                est["vagas_ocupadas"] = est["total_vagas"]
                carros_fora -= vagas_restantes
            else:
                est["vagas_ocupadas"] += carros_fora
                carros_fora = 0
                break

        return carros_fora

    def exibir_lotacao(self, carros_entrada: int):
        carros_fora = self.adicionar_carros(carros_entrada)
        total_lotados = self.contar_lotados()

        print(f"Estacionamentos lotados: {total_lotados} de {len(self.estacionamentos)}.")

        if carros_fora > 0:
            print(f"Carros que não conseguiram estacionar: {carros_fora}.")
        else:
            print("Todos os carros estacionaram com sucesso.")


estacionamentos_info = [
    {"codigo": "A", "total_vagas": 500, "vagas_ocupadas": 500},
    {"codigo": "B", "total_vagas": 500, "vagas_ocupadas": 450},
    {"codigo": "C", "total_vagas": 500, "vagas_ocupadas": 500},
    {"codigo": "D", "total_vagas": 500, "vagas_ocupadas": 400},
]

estacionamento_iguatemi = EstacionamentoIguatemi(estacionamentos_info)

estacionamento_iguatemi.exibir_lotacao(300)