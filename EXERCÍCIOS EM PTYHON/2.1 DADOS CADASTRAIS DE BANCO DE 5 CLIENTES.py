# Matriz 5x5
matriz = [[0]*5 for _ in range(5)]

# Cadastrar clientes
print("-=" * 30)
clientes = []
for _ in range(5):
    num_conta = int(input("Digite o número da conta: "))
    nome = str(input("Digite seu nome: "))
    saldo = float(input("Digite seu saldo: R$"))
    op = input("Digite a operação (C para crédito e D para débito): ")
    clientes.append([num_conta, nome, saldo, op])
    print("-" * 60)
print(clientes)
