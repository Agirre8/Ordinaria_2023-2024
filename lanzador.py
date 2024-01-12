
#no me ha dado tiempo a que funcione ejecutar los mains en los archivos main1 y main2 en las carpetas

from Ejercicio1.main import ejercicio1_main
from Ejercicio2.main import ejercicio1_main

def lanzador():
    while True:
        print("Selecciona el ejercicio que deseas ejecutar:")
        print("1. Ejercicio 1 (Ciudad con Estilos Arquitectónicos)")
        print("2. Otro Ejercicio...")
        print("0. Salir")

        opcion = input("Ingresa el número del ejercicio (o 0 para salir): ")

        if opcion == "1":
            ejercicio1_main()
        elif opcion == "2":
            ejercicio2_main()
        elif opcion == "0":
            print("Saliendo del lanzador.")
            break
        else:
            print("Opción no válida. Introduce un número válido.")

if __name__ == "__main__":
    lanzador()