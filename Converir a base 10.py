def convertirABaseDiez(n,b):
    return aux_x_b10(n,b,0,0)

def aux_x_b10(n,b,p,c):
    if n>0:
        return aux_x_b10(n//10,b,p+1,((b**p)*(n%10))+c)
    else:
        return c
def convertirDeBaseDiez(n,b):
    return aux1(n,b,0,0)
def aux1(n,b,p,c):
    if (n//b)>b:
        return aux1(n%b,b,p+1,((n%b)*(10**p))+c)
    else:
        return (((n%b)*(10**p))+(n%b)*(10**(p+1))+c)
