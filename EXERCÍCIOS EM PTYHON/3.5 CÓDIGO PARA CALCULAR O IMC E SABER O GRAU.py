def usuário():
    peso = float(input("Digite seu peso (em quilos): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = peso / (altura)**2
        
    return imc

def calculo(imc):

    if imc < 18.5:
        classificação = "magreza"
        grau_de_obesidade = 0
    elif 18.5 <= imc < 25:
        classificação = "normal"
        grau_de_obesidade = 0
    elif 25 <= imc < 30:
        classificação = "sobrepeso"
        grau_de_obesidade = 1    
    elif 30 <= imc < 40:
        classificação = "obesidade"
        grau_de_obesidade = 2
    else:
        classificação = "obesidade grave"
        grau_de_obesidade = 3
    return classificação, grau_de_obesidade

def main():
    imc = usuário()
    classificação, grau_de_obesidade = calculo(imc)

    print(f"Seu imc é {imc:.2f}, você está {classificação} e com grau {grau_de_obesidade}!")

main()