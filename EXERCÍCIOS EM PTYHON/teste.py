from datetime import date

def usuario():
    data_str = input("Digite uma data qualquer ex:(dd/mm/aaaa): ")

    # método split irá separá a data_str em cada "/", a qual foi o critério.
    dia, mes, ano = map(int, data_str.split("/"))
    return dia, mes, ano

def organização(dia, mes, ano):
    hoje = date.today()

    

    dias_faltando = map() 


    return dias_faltando