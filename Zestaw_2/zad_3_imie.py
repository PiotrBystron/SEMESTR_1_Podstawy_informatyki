def ilosc_znakow(dane):
    licznik = 0    
    for j in dane:
        licznik += 1    
    return licznik
  
ciag_znakow = str(input("Podaj imię i nazwisko: "))
podzielony = ciag_znakow.split(" ")

for i in podzielony:
    print(ilosc_znakow(i))