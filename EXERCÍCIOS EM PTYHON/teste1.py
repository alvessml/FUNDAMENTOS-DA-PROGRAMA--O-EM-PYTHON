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
        
        print("-="*30)

    return cadastro

def organização(cadastro):
    cadastro.sort(key=lambda x: x[1], reverse=True)

    posição = [i + 1 for i in range(12)]

    tabela = [["L", "Time       ", "P", "J", "V", "E", "D"]] + [[posição[i]] + linha for i, linha in enumerate(cadastro)]

    return tabela

def classificação(tabela):
    print(f"\n Resultados do brasileirão: ")
    print(f"\na) Campeão do brasileiro: {tabela[1][1]}")
    print(f"\nb) 5 primeiros que irão para a libertadores: {", ".join([tabela[i][1] for i in range(1, 6)])}")
    print(f"\nc) 5 seguintes que irão para a sul-americana: {", ".join([tabela[i][1] for i in range(6, 11)])}")
    print(f"\nd)Os dois últimos que serão rebaixados: {", ".join([tabela[i][1] for i in range(11, 13)])}")


# Conduzindo o programa com a sequência abaixo:
def main():
    cadastro = usuario()
    tabela = organização(cadastro)

    #Exibir na tela:
    for linha in (tabela):
        print("\t".join(map(str, linha)))
        # map(str, linha): Converte cada elemento da linha para uma string, # pois join espera strings como argumentos.

    classificação(tabela)

main()