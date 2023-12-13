import random
lista = list(range(1, 30 + 1))
multiplos = []
for _ in lista:
    if _ % 3 == 0:
        multiplos.append(_)

print(multiplos)
    