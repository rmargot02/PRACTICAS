def factorial(num):
    if num > 0:
     
        return int(num*factorial(num-1))
    else:
        return 1

def combinatoria(num1, num2):
    return int(factorial(num1) / (factorial(num2)*factorial(num1-num2)))

def CrearTriangulo(nro_filas):
    if nro_filas==0:
        return "1"
    else: 
        nueva_fila=CrearTriangulo(nro_filas-1)
        for fila in range(nro_filas):
            for j in range(nro_filas-fila+1):
                print(" ", end="")
                for j in range(fila+2):
                    print(combinatoria(fila+1, j), end=" ")
                print()
CrearTriangulo(2)