def usuário():
    peso = float(input("Digite seu peso (em quilos): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = peso / (altura)**2
        
    return imc

def calculo(imc):
    
    return classificação

def main():
    imc = usuário()
    classificação = calculo(imc)