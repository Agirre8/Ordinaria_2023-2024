from Ejercicio1 import ejercicio1_main

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
            # Importa y ejecuta otro ejercicio si lo tienes
            print("Otro ejercicio aún no implementado.")
        elif opcion == "0":
            print("Saliendo del lanzador.")
            break
        else:
            print("Opción no válida. Introduce un número válido.")