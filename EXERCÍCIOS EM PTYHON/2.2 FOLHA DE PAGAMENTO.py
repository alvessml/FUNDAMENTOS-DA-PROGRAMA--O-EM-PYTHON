folha_de_pagamento = []

## Adicionando os dados dos funcionários como lista para a lista folha_de_pagamento!     
x = 0
while x < 4:
    matricula = int(input("Digite a sua matrícula: "))
    nome = input("Digite seu nome: ")
    função = input("Digite sua função: ")
    salario = int(input("Digite seu salário: R$"))
    folha_de_pagamento.append([matricula, nome, função, salario])
    print("-=" * 30)
    x += 1

## Analizando quem tem o maior salário e o menor salário!
maior_salario = folha_de_pagamento[0][3]
menor_salario = folha_de_pagamento[0][3]

for funcionário in folha_de_pagamento:
    salario = funcionário[3]
    if salario > maior_salario:
        maior_salario = salario
    elif salario < menor_salario:
        menor_salario = salario

##Exibindo a matriz 4x4 e maior e menor sálario!
    
print("Folha de pagamento: ")
for funcionário in folha_de_pagamento:
    print(funcionário)

print("\nFuncionário com MAIOR salário: ")
for funcionário in folha_de_pagamento:
    if funcionário[3] == maior_salario:
        print(funcionário)

print("\nFuncionário com MENOR salário: ")
for funcionário in folha_de_pagamento:
    if funcionário[3] == menor_salario:
        print(funcionário)