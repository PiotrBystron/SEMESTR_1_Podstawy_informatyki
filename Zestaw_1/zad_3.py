# sumowanie liczb 10^3, 10^6, 10^9, 10^12 przy pomocy 2 pętli
# złożoność O(n^2)

def brutalne(n):
    wynik = 0
    for i in range (3,12+1,3):
        wynik2 = 1
        for j in range (1,i+1):
            wynik2 = wynik2 * n
        wynik = wynik + wynik2
    return wynik

print(brutalne(10)) 