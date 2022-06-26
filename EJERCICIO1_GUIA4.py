# ************* MÓDULOS ***************
def CalcularPromedios(N):
    if (N > 0):
        CalcularPromedios(N-1)#2
        print('Ingresar notas del alumno ',N)
        Nota1 = int(input('Nota 1: '))
        Nota2 = int(input('Nota 2: '))
        Nota3 = int(input('Nota 3: '))
        Promedio = (Nota1 + Nota2 + Nota3)/3
        print('Promedio: ',Promedio)
N=int(input("Ingrese N: "))
CalcularPromedios(N)