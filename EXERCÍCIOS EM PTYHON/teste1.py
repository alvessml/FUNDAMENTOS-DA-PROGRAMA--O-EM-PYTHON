# for _ in range(20):
#     print(_)
def somatorio():
    vetor = list(range(1, 20 + 1))
    soma = 0
    for n in vetor:
        if n % 2 == 0:
            soma += n
    return soma

def main():
    soma = somatorio()
    print(f"Soma dos pares: {soma}")