

def NumeroPrimo(n):
    div=1
    res=0
    suma=0
    if n<2:
        div = n+1
    while div<=n:
        res=n%div
        div=div+1
        if res==0:
            suma=suma+1
    if suma==2:
        print (n,"es primo")
    else:
        print (n,"no es primo")

NumeroPrimo(1)

