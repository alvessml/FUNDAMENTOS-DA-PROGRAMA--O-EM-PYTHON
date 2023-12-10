def q_cédulas():
    valor = int(input("Digite o quantos você deseja tira do saldo (acima de R$3,99): R$"))

    cédulas = []
    total = valor
    céd_disponíveis = 200
    tot_ced = 0   
    while True:
        if total > céd_disponíveis:
            total -= céd_disponíveis
            cédulas.append(céd_disponíveis)
            tot_ced += 1    
        else:
            if tot_ced > 0:
                print(f"Total de {tot_ced} cédulas de R{céd_disponíveis}")
            if céd_disponíveis == 100:
                céd_disponíveis = 50
            if céd_disponíveis == 50:
                céd_disponíveis = 20
            elif céd_disponíveis == 20:
                céd_disponíveis = 10
            elif céd_disponíveis == 10:
                céd_disponíveis = 5
            elif céd_disponíveis == 5:
                céd_disponíveis = 2
            tot_ced = 0
            if total == 0:
                break
    return cédulas
def main():
    cédulas = q_cédulas()
    cédulas_unicas = set(cédulas)
    print("Você reberá", end="")
    for elemento in cédulas_unicas:
        quantidade = cédulas.count(elemento)
        print(f", {quantidade} cédulas de {elemento} reais", end="")
    print(".")

main()
