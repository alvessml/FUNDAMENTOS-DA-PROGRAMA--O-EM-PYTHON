from random import randint


def tabela():
        
    tabela = []

    tabela.append(["L", "Time       ", "P", "V", "E", "D"])

    for _ in range(2, 4):
        posição = int(input("Posição: "))
        nome = input("Nome: ")
        pontos = int(input("Pontos: "))
        jogos = int(input("Q° jogos: "))
        vitorias = int(input("Vitórias: "))
        empates = int(input("Empates: "))
        derrotas = int(input("Derrotas: "))

        tabela.append([posição, nome, pontos, jogos, vitorias, empates, derrotas])
        print("-="*30)

    tabela.sort(key=lambda x: x[2], reverse=True)

    l = len(tabela)
    c = len(tabela[0])

    for i in range(l):
        for j in range(c):
            print(tabela[i][j], end="\t")
        print()

        
    return tabela

def ordenar_resultados(tabela):
    #Irá organizar a tabela por meio dos pontos!
    tabela.sort(key=lambda x: x[2], reverse=True)
    return tabela



tabela()