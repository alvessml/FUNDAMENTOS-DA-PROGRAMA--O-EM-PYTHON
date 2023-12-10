def q_cédulas():
    valor = int(input("Digite o quantos você deseja tira do saldo (acima de R$3,99): R$"))

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
             if valor % 2 == 1:
                valor -= 5
                cédulas.append(5)
            elif valor % 2 == 0:
                valor -= 2
                cédulas.append(2)
            else:
                if 2 <= valor < 10:
                    if valor % 2 == 1:
                        valor -= 5
                        cédulas.append(5)
                    elif valor % 2 == 0:
                        valor -= 2
                        cédulas.append(2)
                    else:
                        print("Não é possível fornecer cédula!")
                        break
    return cédulas
def main():
    cédulas = q_cédulas()
    cédulas_unicas = set(cédulas)
    print("Você receberá", end="")
    for elemento in cédulas_unicas:
        quantidade = cédulas.count(elemento)
        print(f", {quantidade} cédulas de {elemento} reais", end="")
    print(".")
main()
