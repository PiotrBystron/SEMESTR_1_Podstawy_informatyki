def srednia(Tablica):
    suma=0
    try:
        for i in range(len(Tablica)):
            suma = suma + Tablica[i]
        return suma/len(Tablica)
    except:
        print("Tablica jest pusta!")

Tablica=[]

while True:
    try:
        cyfra = float(input("Podaj liczbę lub podaj dowolny znak, aby zakończyć wprowadzanie danych: "))
        if cyfra > 0 or cyfra < 0 or cyfra == 0:
            Tablica.append(cyfra)
    except:
        break

print("Średnia", len(Tablica) ,"elementów talbicy to:", srednia(Tablica))