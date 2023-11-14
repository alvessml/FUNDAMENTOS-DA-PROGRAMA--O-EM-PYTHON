v = []
p = []
for c in range(10, 20 + 1):
    v.append(c)
    if c % 2 == 0:
        p.append(c)
print(f"Vetor gerado: {v}")
print(f"Pares: {sorted(p, reverse= True)}")
