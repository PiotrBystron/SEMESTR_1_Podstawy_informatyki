def ilosc_znakow(ciag_znakow):
    licznik = 0    
    for i in ciag_znakow:
        licznik += 1    
    return licznik
  
ciag_znakow = str(input("Podaj imię: "))
aaa = ciag_znakow.split(' ')

for i in aaa:
    print(ilosc_znakow(i))