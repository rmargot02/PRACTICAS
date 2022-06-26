import string


def CrearTriangulo(nro_filas):
    if nro_filas==0:
        return [ ]
    if nro_filas==1:
        return [[1]]
    nueva_filas=[1]
    resultado= CrearTriangulo(nro_filas-1)
    ult_fila= resultado[-1]
    for i in range(len(ult_fila)-1):
        n=ult_fila[i] +ult_fila[i+1]
        nueva_filas.append(n)
    nueva_filas.append(1)
    resultado.append(nueva_filas)

    return resultado

print(CrearTriangulo(4))