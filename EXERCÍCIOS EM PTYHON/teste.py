def matriz_3x3():
    from random import randint

    matriz = [[randint(0, 100)for _ in range(3)] for _ in range(3)]

    return matriz

def critérios():
    return coluna_maior_v, linha_menor_v

