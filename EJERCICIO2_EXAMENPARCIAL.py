def DesponerDigitos(N1,N2):
    A=1
    result1=[]
    B=1
    result2=[]
    Interseccion=[]
    for i in range(0, len(N1), A):
            result1.append(int(N1[i : i + A]))
    print("La lista de digitos descompuestos de N1 es :" + str(result1))
    
    for i in range(0, len(N2), B):
            result2.append(int(N2[i : i + B]))
    print("La lista de digitos descompuestos de N2 es : " + str(result2))
    
    for n1 in result1:
        for n2 in result2:
            if n1==n2 and n1 not in Interseccion:
                Interseccion.append(n1)
    print('Los numeros que se repiten en ambos numeros son: ',Interseccion)
    print('El numero de numeros repetidos es:',len(Interseccion))
    if len(Interseccion)>=1:
        print("*******Los numeros NO SON ENEMIGOS**********")
    else:
        print("*********Los numeros SON ENEMIGOS***********")
    

#********PROGRAMA PRINCIPAL*********
N1=input('INGRESE EL PRIMER NUMERO ENTERO :')
N2=input('INGRESE EL SEGUNDO NUMERO ENTERO :')
print(DesponerDigitos(N1, N2))