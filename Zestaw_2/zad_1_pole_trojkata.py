import math

def Heron(a,b,c):
    if (a +b > c and a+c >b and b+c >a):  #warunek istnienia trójkąta 
        p = (a+b+c)/2
        pole = p*(p-a)*(p-b)*(p-c)
        pierwiastek_pola = math.sqrt(pole)
        return pierwiastek_pola
    else:
        print("Trójkąt nie może istnieć")

dlugosc_a = float(input("Podaj długość boku a: "))
dlugosc_b = float(input("Podaj długość boku b: "))
dlugosc_c = float(input("Podaj długość boku c: "))

print(Heron(dlugosc_a,dlugosc_b,dlugosc_c))