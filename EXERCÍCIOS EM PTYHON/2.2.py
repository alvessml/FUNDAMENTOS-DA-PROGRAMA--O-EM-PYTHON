matriz = [[0]*5 for _ in range(5)]

## Adicionando os dados dos funcionários como lista
funcionarios = [] 
maior = 0
menor = 9999999999999
for _ in range(4):
    matricula = int(input("Digite a sua matrícula: "))
    nome = input("Digite seu nome: ")
    função = input("Digite sua função: ")
    salario = int(input("Digite seu salário: R$"))
    funcionarios.append([matricula, nome, função, salario])
    if salario > maior:
        maior = salario
    else: 
        menor = salario
    print("-=" * 30)
for i in range(4):
    for j in range(4):
        matriz[i][j] = funcionarios[i][j]
#for linha in (matriz):
#    print(matriz[i][j])
#print("-="*30)
#print(f"O maior salário foi R${maior} e menor R${menor}.")