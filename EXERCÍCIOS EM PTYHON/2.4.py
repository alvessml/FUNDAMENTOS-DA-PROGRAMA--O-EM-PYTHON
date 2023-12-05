from random import randint
matriz = [[0]*7 for _ in range(12)]

cadastros = []

for _ in range(2):
    posição = int(input("Posição: "))
    nome = input("Nome: ")
    pontos = int(input("Pontos: "))
    jogos = int(input("Q° jogos: "))
    vitorias = int(input("Vitórias: "))
    empates = int(input("Empates: "))
    derrotas = int(input("Derrotas: "))
    cadastros.append([posição, nome, pontos, jogos, vitorias, empates, derrotas])
    print("-="*30)

for linha in (cadastros):
    print(linha)