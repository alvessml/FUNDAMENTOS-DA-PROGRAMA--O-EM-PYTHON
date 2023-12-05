def criar_tabela():
    # Cria uma matriz vazia (12 x 7)
    tabela = [[0] * 7 for _ in range(12)]

    # Preenche a matriz com as informações fornecidas pelo usuário
    for i in range(12):
        print(f"Informe os dados para o time {i + 1}:")
        tabela[i][0] = int(input("Posição: "))
        tabela[i][1] = input("Time: ")
        tabela[i][2] = int(input("Pontos: "))
        tabela[i][3] = int(input("Jogos: "))
        tabela[i][4] = int(input("Vitórias: "))
        tabela[i][5] = int(input("Empates: "))
        tabela[i][6] = int(input("Derrotas: "))
        print()

    return tabela

def imprimir_tabela(tabela):
    # Imprime a tabela formatada
    print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<8} {:<8}".format(
        "Pos", "Time", "Pontos", "Jogos", "Vitórias", "Empates", "Derrotas"))
    
    for linha in tabela:
        print("{:<5} {:<20} {:<10} {:<8} {:<8} {:<8} {:<8}".format(*linha))

def calcular_resultados(tabela):
    # Ordena a tabela pela pontuação em ordem decrescente
    tabela.sort(key=lambda x: x[2], reverse=True)

    # a) Campeão brasileiro
    campeao = tabela[0][1]

    # b) 5 primeiros colocados para a Libertadores
    libertadores = [tabela[i][1] for i in range(5)]

    # c) 5 seguintes para a Copa Sul-Americana
    sul_americana = [tabela[i][1] for i in range(5, 10)]

    # d) 2 últimos rebaixados para a Série B
    rebaixados = [tabela[i][1] for i in range(10, 12)]

    return campeao, libertadores, sul_americana, rebaixados

# Criar a tabela
tabela = criar_tabela()

# Imprimir a tabela
imprimir_tabela(tabela)

# Calcular e imprimir os resultados
campeao, libertadores, sul_americana, rebaixados = calcular_resultados(tabela)

print("\nResultados:")
print(f"a) Campeão brasileiro: {campeao}")
print(f"b) 5 primeiros colocados (Libertadores): {', '.join(libertadores)}")
print(f"c) 5 seguintes (Copa Sul-Americana): {', '.join(sul_americana)}")
print(f"d) 2 últimos rebaixados para a Série B: {', '.join(rebaixados)}")
