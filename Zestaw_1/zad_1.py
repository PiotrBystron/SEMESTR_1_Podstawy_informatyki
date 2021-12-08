# sumowanie liczb 10^3, 10^6, 10^9, 10^12 przy pomocy 1 pętli
# złożoność O(n)

def wolne(n):
    wynik = 0
    for i in range (3,12+1,3):
        wynik = wynik + n ** i
    return wynik

print(wolne(10)) 
