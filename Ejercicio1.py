from abc import ABC, abstractmethod
import copy

# Interfaz para los productos (edificios)
class Edificio(ABC):
    @abstractmethod
    def duplica(self):
        pass

# Clases concretas para diferentes tipos de edificios
class EdificioResidencial(Edificio):
    def duplica(self):
        return copy.deepcopy(self)

class EdificioComercial(Edificio):
    def duplica(self):
        return copy.deepcopy(self)

class EdificioIndustrial(Edificio):
    def duplica(self):
        return copy.deepcopy(self)

# Interfaz para los productos (estilos arquitectónicos)
class EstiloArquitectonico(ABC):
    @abstractmethod
    def duplica(self):
        pass

# Clases concretas para diferentes estilos arquitectónicos
class EstiloModerno(EstiloArquitectonico):
    def duplica(self):
        return copy.deepcopy(self)

class EstiloClasico(EstiloArquitectonico):
    def duplica(self):
        return copy.deepcopy(self)

class EstiloFuturista(EstiloArquitectonico):
    def duplica(self):
        return copy.deepcopy(self)

class EstiloContemporaneo(EstiloArquitectonico):
    def duplica(self):
        return copy.deepcopy(self)

class EstiloColonial(EstiloArquitectonico):
    def duplica(self):
        return copy.deepcopy(self)

# Abstract Factory para crear edificios con diferentes estilos arquitectónicos
class FabricaEdificios(ABC):
    @abstractmethod
    def crear_edificio(self) -> Edificio:
        pass

    @abstractmethod
    def crear_estilo_arquitectonico(self) -> EstiloArquitectonico:
        pass

    # Nueva funcionalidad en el método abstracto
    def crear_ciudad(self, cantidad_edificios: int) -> list:
        ciudad = []
        for _ in range(cantidad_edificios):
            edificio = self.crear_edificio()
            estilo = self.crear_estilo_arquitectonico()
            ciudad.append((edificio, estilo))
        return ciudad



# Implementación concreta de la Abstract Factory
class FabricaEdificiosConcretos(FabricaEdificios):
    def crear_edificio(self) -> Edificio:
        return EdificioResidencial()

    def crear_estilo_arquitectonico(self) -> EstiloArquitectonico:
        return EstiloModerno()

class FabricaEdificiosConcretosAmpliada(FabricaEdificios):
    def crear_edificio(self) -> Edificio:
        return EdificioResidencial()

    def crear_estilo_arquitectonico(self) -> EstiloArquitectonico:
        # Puedes cambiar el estilo que deseas usar aquí
        return EstiloContemporaneo()


def main():
        # Fábrica original
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

    # Fábrica ampliada
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

    # Crear una ciudad usando el nuevo método
    ciudad_fabrica_ampliada = fabrica_ampliada.crear_ciudad(cantidad_edificios=5)
    
    print("Ciudad fabricada con Fábrica ampliada:")
    for edificio, estilo in ciudad_fabrica_ampliada:
        print(f"Edificio: {edificio}, Estilo: {estilo}")

main()