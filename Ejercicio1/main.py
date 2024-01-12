from fabricas import FabricaEdificiosConcretos, FabricaEdificiosConcretosAmpliada

def ejercicio1_main():
    # Fabrica original
    fabrica = FabricaEdificiosConcretos()

    edificio = fabrica.crear_edificio()
    estilo = fabrica.crear_estilo_arquitectonico()

    edificio_clon = edificio.duplica()
    estilo_clon = estilo.duplica()

    print("Fábrica original:")
    print(f"Edificio original: {edificio}")
    print(f"Edificio clonado: {edificio_clon}")
    print(f"Estilo original: {estilo}")
    print(f"Estilo clonado: {estilo_clon}")

    print("\n------------------------\n")

    # Implementación de la fábrica ampliada
    fabrica_ampliada = FabricaEdificiosConcretosAmpliada()

    edificio_ampliado = fabrica_ampliada.crear_edificio()
    estilo_ampliado = fabrica_ampliada.crear_estilo_arquitectonico()

    edificio_ampliado_clon = edificio_ampliado.duplica()
    estilo_ampliado_clon = estilo_ampliado.duplica()

    print("Fábrica ampliada:")
    print(f"Edificio ampliado original: {edificio_ampliado}")
    print(f"Edificio ampliado clonado: {edificio_ampliado_clon}")
    print(f"Estilo ampliado original: {estilo_ampliado}")
    print(f"Estilo ampliado clonado: {estilo_ampliado_clon}")

    print("\n------------------------\n")

    # Crear ciudad con la fábrica ampliada
    ciudad_fabrica_ampliada = fabrica_ampliada.crear_ciudad(cantidad_edificios=5)

    print("Ciudad fabricada con Fábrica ampliada:")
    for edificio, estilo in ciudad_fabrica_ampliada:
        print(f"Edificio: {edificio}, Estilo: {estilo}")

if __name__ == "__main__":
    ejercicio1_main()
