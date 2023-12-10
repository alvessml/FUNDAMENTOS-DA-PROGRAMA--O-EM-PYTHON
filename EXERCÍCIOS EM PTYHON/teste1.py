def caixa_eletronico():
    valor_saque = int(input("Digite o quanto você deseja tirar do saldo (acima de R$3,99): R$"))

    cedulas = [200, 100, 50, 20, 10, 5, 2]
    notas = []

    for nota in cedulas:
        while valor_saque >= nota:
            if valor_saque % 2 == 0 and valor_saque == 6 :
                valor_saque -= 2
                notas.append(2)
                break
            elif valor_saque % 2 == 0 and valor_saque == 8 :
                valor_saque -= 2
                notas.append(2)
                break
            elif valor_saque % 2 == 1 and 10 < valor_saque < 13:
                valor_saque -= 5
                notas.append(5)
                break
            elif valor_saque % 2 == 0:
                valor_saque -= nota
                notas.append(nota)
            elif valor_saque % 2 == 1:
                valor_saque -= nota
                notas.append(nota)
    return notas

def main():
    notas = caixa_eletronico()
    
    if notas:
        print("Notas retiradas:", notas)
    else:
        print("Valor de saque inválido. Certifique-se de que é acima de R$3,99 e um valor permitido.")

if __name__ == "__main__":
    main()

