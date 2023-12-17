from random import randint

vetor = [randint(1, 100) for _ in range(10)]

print(f"Vetor gerado: {vetor}")

def maior_(n):
    maior = 0
    if  vetor[n] > maior:
        maior = vetor[n]
    
    return maior

res = 0
for i in range(10):
    res = maior_(i)

print(f"Maior número do meu vetor é {res}.")