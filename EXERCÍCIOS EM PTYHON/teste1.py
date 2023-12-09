def q_cédulas():
    valor = int(input("Digite o quanto você deseja tirar do saldo (acima de R$3,99): R$"))

    cédulas = []

    while valor > 0:
        if valor >= 200:
            valor -= 200
            cédulas.append(200)
        elif 100 <= valor < 200:
            valor -= 100
            cédulas.append(100)
        elif 50 <= valor < 100:
            valor -= 50
            cédulas.append(50)
        elif 20 <= valor < 50:
            valor -= 20
            cédulas.append(20)
        elif 10 <= valor < 20:
            valor -= 10
            cédulas.append(10)
        elif 5 <= valor < 10:
            valor -= 5
            cédulas.append(5)
        elif 2 <= valor < 5:
            valor -= 2
            cédulas.append(2)
        else:
            # Se nenhum dos casos acima for atendido, o valor é menor que 2
            # e não é possível utilizar cédulas menores que 2 reais
            print("Não é possível fornecer cédulas para o valor informado.")
            break

    return cédulas

def main():
    cédulas = q_cédulas()
    print("Cédulas fornecidas:", cédulas)

if __name__ == "__main__":
    main()
