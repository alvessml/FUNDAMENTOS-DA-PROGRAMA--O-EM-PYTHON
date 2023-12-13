def somatório(inicio, fim):
    if inicio > fim:
        return 0
    
    if inicio % 2 == 0:
        return inicio + somatório(inicio + 2, fim)
    else:
        return somatório(inicio + 1, fim)

soma = somatório(1, 20)

print(f"O somatório dos pares de 1 a 20 é: {soma}")