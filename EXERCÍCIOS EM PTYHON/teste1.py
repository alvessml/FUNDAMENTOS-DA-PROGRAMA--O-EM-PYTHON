A = [[2, 7, 6], [9, 5, 1], [4, 3, 18]]

for linha in (A):
    print(linha)

def QuadradoMagico(A):
    soma_linha = []
    for i in range(3):
        soma = 0
        for j in range(3):
            soma += A[i][j]
        soma_linha.append(soma)

    soma_colunas = []
    for j in range(3):
        soma = 0
        for i in range(3):
            soma += A[i][j]
        soma_colunas.append(soma)

    soma_diagonal1 = 0
    for i in range(3):
        soma_diagonal1 += A[i][i]

    soma_diagonal2 = 0
    for i in range(3):
        soma_diagonal2 += A[i][3 - 1 - i]


    #Equiparar os valores

    for elemento in (soma_linha):
        if elemento != soma_diagonal2:
            return False

    for elemento in (soma_colunas):
        if elemento != soma_diagonal2:
            return False
    
    if soma_diagonal1 != soma_diagonal2:
        return False
    
    return True



if (QuadradoMagico(A)):
    print("É um QUADRADO MÁGICO")
else:
    print("NÃO é um QUADRADO MÁGICO")
    

    
