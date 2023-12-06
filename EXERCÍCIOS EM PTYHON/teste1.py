from random import randint

def tabela_classificacao():
    tabela = []

    for _ in range(3):
        posição = int(input("Posição: "))
        nome = input("Nome: ")
        pontos = int(input("Pontos: "))
        jogos = int(input("Q° jogos: "))
        vitorias = int(input("Vitórias: "))
        empates = int(input("Empates: "))
        derrotas = int(input("Derrotas: "))

        tabela.append([posição, nome, pontos, jogos, vitorias, empates, derrotas])
        print("-=" * 30)

    tabela.sort(key=lambda x: x[2], reverse=True)

    l = len(tabela)
    c = len(tabela[0])

    for i in range(l):
        for j in range(c):
            print(tabela[i][j], end="\t")
        print()

    return tabela

def ordenar_resultados(tabela):
    tabela_topo = ["L", "Time", "P", "V", "E", "D"]
    tabela.insert(0, tabela_topo)

    campeao = tabela[1][1]
    libertadores = [tabela[i][1] for i in range(1, 6)]
    sul_americana = [tabela[i][1] for i in range(6, 11)]
    rebaixados = [tabela[i][1] for i in range(11, 13)]

    return campeao, libertadores, sul_americana, rebaixados

tabela = tabela_classificacao()

# Corrected the function call by adding parentheses
campeao, libertadores, sul_americana, rebaixados = ordenar_resultados(tabela)

print("\nResultados do brasileirão:")
print(f"a) Campeão do brasileiro: {campeao}")
print(f"b) 5 primeiros que irão para a libertadores: {', '.join(libertadores)}")
print(f"c) 5 seguintes que irão para a sul-americana: {', '.join(sul_americana)}")
print(f"d) Os dois últimos que serão rebaixados: {', '.join(rebaixados)}")
