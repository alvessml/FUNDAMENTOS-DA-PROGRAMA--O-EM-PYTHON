def q_cédulas():
    valor = int(input("Digite o quantos você deseja tira do saldo (acima de R$3,99): R$"))

    cédulas = []
    if valor >= 4:
        while valor > 0:
            if valor >= 200:
                if valor % 2 == 1:
                    valor -= 100
                    cédulas.append(100)
                elif valor % 2 == 0:
                    valor -= 200
                    cédulas.append(200)
            elif 100 <= valor < 200:
                if valor % 2 == 1:
                    valor -= 50
                    cédulas.append(50)
                elif valor % 2 == 0:
                    valor -= 100
                    cédulas.append(100)
            elif 50 <= valor < 100:        
                if valor % 2 == 1:
                    valor -= 20
                    cédulas.append(20)
                elif valor % 2 == 0:
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
                    valor -= 10
                    cédulas.append(10)
            elif 5 <= valor < 10:
                if valor % 2 == 1:
                    valor -= 5
                    cédulas.append(5)
                elif valor % 2 == 0:
                    valor -= 2
                    cédulas.append(2)
            elif 2 <= valor < 5:
                valor -= 2
                cédulas.append(2)
    else:
        print("Inválido! Avalie se o seu valor é acima de R$4 !")
        
    return cédulas, valor
def main():
    cédulas, valor = q_cédulas()
    if valor >= 4:
        cédulas_unicas = set(cédulas)
        print("Você receberá", end="")
        for elemento in cédulas_unicas:
            quantidade = cédulas.count(elemento)
            print(f", {quantidade} cédulas de {elemento} reais", end="")
        print(".")
    elif valor < 4:
        False
main()
