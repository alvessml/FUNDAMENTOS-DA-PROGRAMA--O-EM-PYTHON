from random import randint

matriz = [[randint(1, 100) for _ in range(3)]for _ in range(3)]

print("Matriz gerada: ")
for _ in matriz:
    print("{:<3} {:<3} {:<3}".format(*_))


def soma_diagonais(matriz):
    
    soma_diagonal_1 = 0
    for i in range(3):
        soma_diagonal_1 += matriz[i][i]

    soma_diagonal_2 = 0
    for i in range(3):
        soma_diagonal_2 += matriz[i][3 - 1 - i]

    return soma_diagonal_1, soma_diagonal_2

def main():
    soma_diagonal_1, soma_diagonal_2 = soma_diagonais(matriz)
    
    print(f"A soma da diagonal 1 é {soma_diagonal_1} e a diagonal 2 é {soma_diagonal_2}.")

main()