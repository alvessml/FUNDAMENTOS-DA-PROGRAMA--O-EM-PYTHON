def fibonacci(n):
    if n == 1:
        return 0 
    elif n == 2:
        return 1
    else:
                #termo anterior + termo antes do anterior
        return fibonacci(n - 1) + fibonacci(n - 2)

def série_fibonacci(n):
    if n <= 0:
        print("Erro! Digite um número maior que 0!")
    else:
        print(f"Serié fibonacci do {n}° termo é: ")

        for i in range(1, 12+1):
            print(fibonacci(i), end=" ")

série_fibonacci(12)