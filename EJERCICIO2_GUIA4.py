def CalcularPromedios(N):
    if (N == 0):
        return 0, 0
    else:
        A, D = CalcularPromedios(N-1)
        print('Ingresar notas del alumno ',N)
        Nota1 = int(input('Nota 1: '))
        Nota2 = int(input('Nota 2: '))
        Nota3 = int(input('Nota 3: '))
        Promedio = (Nota1 + Nota2 + Nota3)/3
        print('Promedio: ',Promedio)
        if Promedio >= 14:
            A += 1
        else:
            D += 1
        return A, D
N=int(input("Ingrese N: "))
CalcularPromedios(N)
    