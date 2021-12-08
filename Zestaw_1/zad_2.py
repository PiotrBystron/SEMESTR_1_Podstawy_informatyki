# sumowanie liczb 10^3, 10^6, 10^9, 10^12 
# złożoność O(1)

def szybkie(n):
    wynik = n*(n*(n*(n*(n*(n*(n*(n*(n*(n*(n*(n+0)+0)+1)+0)+0)+1)+0)+0)+1)+0)+0)+0
    return wynik

print(szybkie(10)) 