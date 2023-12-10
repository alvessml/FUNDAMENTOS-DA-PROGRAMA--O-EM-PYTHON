def calcular_cedulas(valor):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    quantidades = []
    
    for cedula in  cedulas:
        # Irá calcular quantas vezes a cedula cabe no meu valor
        qtd_cedulas = valor // cedula
        quantidades.append(qtd_cedulas)
        valor %= cedula
    
    return quantidades

def main():
    valor_saque = int(input("Digite o valor que voce deseja sacar (a partir de R$4): R$"))

    if valor_saque < 4:
        print("Inválido! Digite novamente um valor acima de R$4 para sacar!")
    else:
        quantidades = calcular_cedulas(valor_saque)

        print(f"Você receberá: ")
        for cedula, quantidade in zip([200, 100, 50, 20, 10, 5, 2], quantidades):
            if quantidade > 0:
                print(f"{quantidade} cédula(s) de R${cedula}")
                
main()