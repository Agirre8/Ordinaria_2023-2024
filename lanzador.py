#no me ha dado tiempo a que funcione ejecutar los mains en los archivos main1 y main2 en las carpetas
# from Ejercicio1.main1 import ejercicio1_main
# from Ejercicio2.main2 import ejercicio2_main
import sys
sys.path.insert(0,"/Users/smite/Documents/GitHub/Ordinaria_2023-2024/Ejercicio1")
# sys.path.insert(0,"/Users/smite/Documents/GitHub/Ordinaria_2023-2024/ORDINARIA_2023-2024/Ejercicio1/fabricas")


sys.path.insert(0,"/Users/smite/Documents/GitHub/Ordinaria_2023-2024/Ejercicio2")
from main1 import *
from main2 import *
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