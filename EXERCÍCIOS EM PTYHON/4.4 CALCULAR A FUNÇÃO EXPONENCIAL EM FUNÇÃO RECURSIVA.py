from random import randint

def função_exp(valor, x = 0, resultado = 1):
    if x < valor:
        resultado = resultado * 2
        return função_exp(valor, x + 1, resultado)
    else:
        return resultado
valor = randint(1, 10)
y = função_exp(valor)
print(f"O valor da explonecial de 2^{valor} = {y}")