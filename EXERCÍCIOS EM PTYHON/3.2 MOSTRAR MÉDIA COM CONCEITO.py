def media_final():
    média_f = float(input("Digite sua média final (de 0 a 10): "))
    
    if 9 <= média_f <= 10:
        print(f"Você tirou um A com nota igual {média_f:.2}.")
    elif 7 <= média_f < 9:
        print(f"Você tirou um B com nota igual {média_f:.2}.")
    elif 5 <= média_f < 7:
        print(f"Você tirou um C com nota igual {média_f:.2}.")
    elif 0 <= média_f < 5:
        print(f"Você tirou um D com nota igual {média_f:.2}.")
    else:
        print("Resposta inválida, digite novamente!")

media_final()