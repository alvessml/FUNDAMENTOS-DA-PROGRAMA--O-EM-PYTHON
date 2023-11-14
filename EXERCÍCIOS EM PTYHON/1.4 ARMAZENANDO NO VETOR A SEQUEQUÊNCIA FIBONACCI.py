v = []
n1 = -1
n2 = 1
x = 0
while len(v) < 20:
    n3 = n2 + n1
    v.append(n3)
    n1 = n2
    n2 = n3
    x += 1
print(f"Sequência Fibonacci até 20° posição é {v}")
