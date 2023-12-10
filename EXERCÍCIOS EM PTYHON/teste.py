def caixa_eletronico():
    valor_saque = int(input("Digite o quantos você deseja tira do saldo (acima de R$3,99): R$"))

    cédulas = [200, 100, 50, 20, 10, 5, 2]
    notas = []
    for nota in cédulas:
        while True:
                if valor_saque >= nota:
                    if valor_saque % 2 == 0: 
                        valor_saque -= nota
                        notas.append(nota)
                        break
                elif cédulas[nota + 1] <= valor_saque < cédulas[nota - 1]: 
                    valor_saque -= nota
                    notas.append(nota)
                    break
                else:
                    break
                
    return notas

def main():
    notas = caixa_eletronico()
    print(notas)

main()