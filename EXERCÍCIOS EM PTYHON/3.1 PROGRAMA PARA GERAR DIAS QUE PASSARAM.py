from datetime import date

def usuario():
    data_str = input("Digite uma data qualquer ex:(dd/mm/aaaa): ")

    # método split irá separá a data_str em cada "/", a qual foi o critério.
    dia, mes, ano = map(int, data_str.split("/"))
    return dia, mes, ano, data_str

def organização(dia, mes, ano):
    data_atual = date.today()

    day = data_atual.day
    month = data_atual.month
    year = data_atual.year
    
    if dia >= day:
        dia_f = dia - day
    else:
        dia_f = day - dia
    
    if mes >= month:
        mes_f = mes - month
    else:
        mes_f = month - mes

    if ano >= year:
        ano_f = ano - year
    else:
        ano_f = year - ano

    dia_totais_f = dia_f + (mes_f * 30) + (ano_f * 365)

    return dia_totais_f
  
def main():
    dia, mes, ano, data_str = usuario()
    dia_totais_f = organização(dia, mes, ano)
    print(f"Já se passaram {dia_totais_f} dias, deste dessa data.")

main()
