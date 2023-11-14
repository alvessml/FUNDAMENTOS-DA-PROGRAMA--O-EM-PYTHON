from random import randint

# Étapa 1 -> iremos criar um vetor que receberá 10 valores aleatórios.
vetor = [randint(0, 100) for _ in range(10)]

# Étapa 2 -> iremos análisar quantas vezes o meu elemento está repetindo.
contador = {}
elementos_repetido = []

for valor in vetor:
    if valor in contador:
        contador[valor] += 1
    else:
        contador[valor] = 1

# Étapa 3 -> iremos colocar no vetor elemento_repetido os valores repetidos e imprimir.
print(f"Vetor gerado: {vetor}")
repetição = False
for valor, quantidade in contador.items():
    if quantidade > 1:
        elementos_repetido.append(valor)
        repetição = True
if repetição == True:
    print(f"Valores repetidos: {elementos_repetido}")
else:
    print("Não há valores repetidos!")
