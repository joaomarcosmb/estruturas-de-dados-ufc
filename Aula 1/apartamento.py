def calc_entrada(valor_apt: float) -> float:
    return valor_apt * 0.1


def pode_comprar(valor_apt: float) -> bool:
    soma_rendas = 0

    while True:
        try:
            outra_renda = float(input("Insira uma renda: "))
        except ValueError:
            print("Insira um valor numérico ou digite 0 para parar.")
            continue

        if outra_renda == 0.0:
            print("Você não pode comprar o apartamento.")
            return False

        soma_rendas += outra_renda
        print(f"Soma das rendas: {soma_rendas}")

        credito = soma_rendas * 65  # É o mesmo que soma_rendas / 1_000 * 65_000
        print(f"Crédito: {credito}\n")

        valor = valor_apt - calc_entrada(valor_apt)
        if credito >= valor:
            print("Parabéns, você pode comprar o apartamento!")
            return True
        else:
            continue


print(pode_comprar(131_000))
