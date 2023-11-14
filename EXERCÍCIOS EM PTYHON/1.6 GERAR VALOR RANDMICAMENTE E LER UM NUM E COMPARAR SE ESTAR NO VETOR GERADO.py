from random import randint
v = []
for c in range(10):
    n = randint(0, 100)
    v.append(n)
p = int(input("Digite um valor para comparar com o vetor gerado: "))

encontrado = False
for o in range(len(v)):
    if p == v[o]:
        print(f"{p} está no vetor gerado! Na posição {o}.")
        encontrado = True
        break
if not encontrado:
    print(f"{p} não está no vetor gerado.")
print(f"Vetor gerado: {v}")
