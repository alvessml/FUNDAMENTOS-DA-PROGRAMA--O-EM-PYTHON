def calcular_cedulas(valor):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    quantidades = []

    for cedula in cedulas:
        qtd_cedulas = valor // cedula
        quantidades.append(qtd_cedulas)
        valor %= cedula

    return quantidades

def main():
    valor_saque = int(input("Digite o valor que você deseja sacar (a partir de R$4): R$"))

    if valor_saque < 4:
        print("Valor inválido. O saque mínimo é R$4.")
    else:
        quantidades = calcular_cedulas(valor_saque)

        print(f"Para sacar R${valor_saque}, você precisará de:")
        for cedula, quantidade in zip([200, 100, 50, 20, 10, 5, 2], quantidades):
            if quantidade > 0:
                print(f"{quantidade} cédula(s) de R${cedula}")

if __name__ == "__main__":
    main()
