def usuario():
    cadastro = []

    for x in range(12):
        nome = input("Time: ")
        pontos = int(input("Pontos: "))
        jogos = int(input("Q° jogos: "))
        vitorias = int(input("Vitórias: "))
        empates = int(input("Empates: "))
        derrotas = int(input("Derrotas: "))

        cadastro.append([nome, pontos, jogos, vitorias, empates, derrotas])
        
        print("-="*30)

    return cadastro

def organização(cadastro):
    cadastro.sort(key=lambda x: x[1], reverse=True)
    
    l = len(tabela)
    c = len(tabela[0])

    for i in range(l):
        for j in range(c):
            print(tabela[i][j], end="\t")
        print()
    return

def tabela(cadastro):
    print(f"\n Resultados do brasileirão: ")
    print(f"a) Campeão do brasileiro: {cadastro[1][1]}")
    print(f"b) 5 primeiros que irão para a libertadores: {", ".join([cadastro[i][0] for i in range(1, 2)])}")
    print(f"5 seguintes que irão para a sul-americana: {", ".join([cadastro[i][0] for i in range(2, 3)])}")
    print(f"Os dois últimos que serão rebaixados: {", ".join([cadastro[i][0] for i in range(3, 6)])}")
    return 