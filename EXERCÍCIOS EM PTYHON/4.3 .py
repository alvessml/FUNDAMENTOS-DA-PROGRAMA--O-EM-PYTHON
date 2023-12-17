from random import randint

def main(vetor, x = 0, maior=None):
    if x == len(vetor):
        return maior
    else:
        num_atual = vetor[x]
        if maior is None or num_atual > maior:
            maior = num_atual
            return main(vetor, x + 1, maior)

vetor = [randint(1, 100) for _ in range(10)]
maior_valor = main(vetor)
print(f"Vetor gerado: {vetor}")
print(f"\nMaior valor gerado foi {maior_valor}.")