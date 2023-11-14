from random import randint
primos = []
l = []
for c in range(1, 10+1):
    x = randint(1, 100)
    l.append(x)
print(f"Vetor gerado: {l}")
x = 0
while x < len(l):
    p = 0
    for z in range(1, l[x] + 1):
        if l[x] % z == 0:
            p += 1
    if p == 2:
        primos.append(l[x])
    x += 1
print(f"Primos são: {primos}")
