tabela = []

for x in range(6):
    posição = []
    nome = input("Nome: ")
    pontos = int(input("Pontos: "))
    jogos = int(input("Q° jogos: "))
    vitorias = int(input("Vitórias: "))
    empates = int(input("Empates: "))
    derrotas = int(input("Derrotas: "))

    tabela.append([posição, nome, pontos, jogos, vitorias, empates, derrotas])

    #maior = pontos

    #if pontos > maior
    print("-="*30)

#-----------------------------------------------------------#
tabela.sort(key=lambda x: x[2], reverse=True)

tabela_topo = ["L", "Time       ", "P", "V", "E", "D"]

tabela.insert(0, tabela_topo)

l = len(tabela)
c = len(tabela[0])

for i in range(l):
    for j in range(c):
        print(tabela[i][j], end="\t")
    print()

#-----------------------------------------------------------#
print(f"\n Resultados do brasileirão: ")
print(f"a) Campeão do brasileiro: {tabela[1][1]}")
print(f"b) 5 primeiros que irão para a libertadores: {", ".join([tabela[i][0] for i in range(1, 2)])}")
print(f"5 seguintes que irão para a sul-americana: {", ".join([tabela[i][0] for i in range(2, 3)])}")
print(f"Os dois últimos que serão rebaixados: {", ".join([tabela[i][0] for i in range(3, 6)])}")