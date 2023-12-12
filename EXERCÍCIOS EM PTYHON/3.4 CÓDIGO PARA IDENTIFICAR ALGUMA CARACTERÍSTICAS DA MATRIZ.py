def matriz_3x3():
    from random import randint

    matriz = [[randint(0, 100)for _ in range(3)] for _ in range(3)]

    return matriz

def critérios(matriz):

    # Código para saber qual coluna tem o maior número e qual é esse número.
    maior_c = 0
    for c in range(3):
        for l in range(3):
            if matriz[l][c] > maior_c:
                maior_c = matriz[l][c]
                coluna_maior = c

    # Código para saber qual linha tem o menor número e qual é esse número.
    menor_l = 111
    for l in range(3):
         for c in range(3):
              if matriz[l][c] < menor_l:
                   menor_l = matriz[l][c]
                   linha_menor = l

    return coluna_maior, maior_c, linha_menor, menor_l

def main():
    matriz = matriz_3x3()
    coluna_maior, maior_c, linha_menor, menor_l = critérios(matriz)

    print("Matriz gerada: ")
    for linha in matriz:
         print("{:<3} {:<3} {:<3}".format(*linha))

    print("-="*30)

    print(f"O maior número da coluna da matriz acima é o {maior_c} e está na coluna {coluna_maior}:\n")

    soma = 0
    for linha in matriz:
            print(linha[coluna_maior])
            soma += linha[coluna_maior]

    print(f"\nSoma destes valores é {soma}.")

    print("-="*30)

    print(f"O menor número da linha da matriz acima é o {menor_l} e está na linha {linha_menor}:\n")

    print("{:<3} {:<3} {:<3}".format(*matriz[linha_menor]))
    soma = 0
    for elemento in matriz[linha_menor]:
         soma += elemento
    print(f"\nSoma desdes valores é {soma}.")


main()