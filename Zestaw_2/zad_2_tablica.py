def srednia(T):
    suma=0
    for i in range(len(T)):
        suma = suma + T[i]
    return suma/len(T)

T=[2, 4, 7, 9, 12, 16, 31, 51, 21, 17]

print("Średnia", len(T) ,"elementów talbicy to:", srednia(T))