from random import randint
v = [randint(0, 100) for _ in range(10)]
p = 0
i = 0
for c in range(len(v)):
    if v[c] % 2 == 0:
        p += 1
    else:
        i += 1
print(v)
print(f"O vetor gerado possui {p} pares e {i} impares!")
