def convertirABaseDiez(n,b):
    return aux_x_b10(n,b,0,0)

def aux_x_b10(n,b,p,c):
    if n>0:
        return aux_x_b10(n//10,b,p+1,((b**p)*(n%10))+c)
    else:
        return c
