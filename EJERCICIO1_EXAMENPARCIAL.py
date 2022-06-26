#LLASA YUCRA RUTH MARGOT
import os
global lista 
lista=list()

class Dato1:
    Distrito=""
    Provincia=""
    nro_Contagiados_Mayo=0
    nro_Contagiados_Junio=0

def RegistrarDistrito():
    print("Registrar Distrito, Provincia--->")
    a=Dato1()
    a.Provincia=input("Ingrese nombre de la Provincia: ")
    a.Distrito=input("Ingrese el nombre del distrito: ")
    a.nro_Contagiados_Mayo=int(input("Ingrese el nro de contagiados en el mes de Mayo: "))
    a.nro_Contagiados_Junio=int(input("Ingrese el nro de contagiados en el mes de junio: "))
    lista.append(a)
def ListarDistrito():
    print("LISTADO DE DISTRITOS Y CONTAGIADOS (MAYO-JUNIO)")
    for a in lista:
        print(a.Provincia,"-", a.Distrito," -", a.nro_Contagiados_Mayo,"-",a.nro_Contagiados_Junio)
def DistritosPrevncion():
    for a in lista:
        if a.nro_Contagiados_Mayo+a.nro_Contagiados_Junio<100:
            print("NO HAY DISTRITOS EN PREVENCION")
        else:
            a.nro_Contagiados_Mayo+a.nro_Contagiados_Junio>=100
            print("el distrito PARA PREVENCION ES:", a.Distrito,"-", a.Provincia)

def Salir():
    print("Gracias por utilizar la aplicacion")
def Menu():
    while True:
        print("QUE TIPO DE OPERACION DESEA REALIZAR")
        print("****************MENU*******************")
        print("1----> INGRESAR DATOS DEL DISTRITO")
        print("2----> MOSTRAR LISTADO DE DATOS")
        print("3----> MOSTRAR DISTRITOS EN PREVENCION")
        print("4----> SALIR")
        opcion=input("Ingrese la opcion de su preferencia:" )
        if opcion=='1':
            print(RegistrarDistrito())
            
        if opcion=='2':
            print(ListarDistrito())
            
        if opcion=='3':
            print(DistritosPrevncion())

        if opcion=='4':
            print(Salir())
            break
Menu()


    
    





