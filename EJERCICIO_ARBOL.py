def Mostrar(nroEspacios,nroAsteriscos):
    print(' '*nroEspacios+'*'*nroAsteriscos)

def CopaArbol(nroEspacios,n):
    if n>0:
        CopaArbol(nroEspacios+1,n-1)
        Mostrar(nroEspacios, 2*n-1)
def Tronco(nroEspacios,n):
    if n>0:
        Tronco(nroEspacios, n-1)
        Mostrar(nroEspacios,3)
def Base(nroEspacios,n):
    if n>0:
        Base(nroEspacios,n-1)
        Mostrar(nroEspacios,9)

CopaArbol(0,5)
Tronco(3,3)
Base(0,1)