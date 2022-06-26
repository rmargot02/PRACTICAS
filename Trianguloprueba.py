# Doing the Pascal's Triangle using Python
def factorial(num):
    if num > 0:
        # Doing the factorial using recursion
        return int(num*factorial(num-1))
    else:
        return 1

def combinatoria(num1, num2):
    return int(factorial(num1) / (factorial(num2)*factorial(num1-num2)))

def crearTriangulo(n_filas):
    for fila in range(n_filas):
        for j in range(n_filas-fila+1):
            print(" ", end="")
        if fila == 0:
            print("1 1")
        else:
            for j in range(fila+2):
                print(combinatoria(fila+1, j), end=" ")
            print()

crearTriangulo(int(input("Indica el número de filas que desee: ")))