def usuario():
    cadastro = []

    for _ in range(12):
        nome = input("Time: ")
        pontos = int(input("Pontos: "))
        jogos = int(input("Q° jogos: "))
        vitorias = int(input("Vitórias: "))
        empates = int(input("Empates: "))
        derrotas = int(input("Derrotas: "))

        cadastro.append([nome, pontos, jogos, vitorias, empates, derrotas])

        print("-=" * 30)

    return cadastro

def organizacao(cadastro):
    cadastro.sort(key=lambda x: x[2], reverse=True)

    posicao = [i + 1 for i in range(12)]

    tabela = [["L"] + ["Time", "P", "J", "V", "E", "D"]] + [[posicao[i]] + linha for i, linha in enumerate(cadastro)]

    return tabela

def classificacao(tabela):
    print(f"\n Resultados do brasileirão: ")
    print(f"a) Campeão do brasileiro: {tabela[1][1]}")
    print(f"b) 5 primeiros que irão para a libertadores: {', '.join([tabela[i][1] for i in range(1, 6)])}")
    print(f"c) 5 seguintes que irão para a sul-americana: {', '.join([tabela[i][1] for i in range(6, 11)])}")
    print(f"d) Os dois últimos que serão rebaixados: {', '.join([tabela[i][1] for i in range(11, 13)])}")

def main():
    cadastro = usuario()
    tabela = organizacao(cadastro)
    classificacao(tabela)

    # Exibindo a tabela
    for linha in tabela:
        print("\t".join(map(str, linha)))

if __name__ == "__main__":
    main()
