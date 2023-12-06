from random import randint


def tabela_classicação():

    tabela = []

    #tabela.append(["L", "Time       ", "P", "V", "E", "D"])

    for _ in range(12):
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
        
    return tabela_classicação

def ordenar_resultados(tabela):
    #Irá organizar a tabela por meio dos pontos!
    tabela.sort(key=lambda x: x[2], reverse=True)

    # a) campeão do brasileirão 
    campeao = tabela[0][0]

    # b) 5 primeiros colocados para a libertadores
    libertadores = [tabela[i][0] for i in range(5)]

    # c) 5 seguintes para a copa sul-americano
    sul_americana = [tabela[i][0] for i in range(5, 10)]

    # d) 2 últimos que serão rebaixados
    rebaixados = [tabela[i][0] for i in range(10, 12)]

    return campeao, libertadores, sul_americana, rebaixados

def barra(tabela):
     tabela.append(["L", "Time       ", "P", "V", "E", "D"])


tabela_classicação()

campeao, libertadores, sul_americana, rebaixados = ordenar_resultados

print("\n Resultados do brasileirão: ")
print(f"a) Campeão do brasileiro: {campeao}")
print(f"b) 5 primeiros que irão para a libertadores: {", ".join(libertadores)}")
print(f"5 seguintes que irão para a sul-americana: {", ".join(sul_americana)}")
print(f"Os dois últimos que serão rebaixados: {", ".join(rebaixados)}")