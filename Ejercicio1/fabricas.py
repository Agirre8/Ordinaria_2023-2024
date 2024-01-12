from abc import ABC, abstractmethod
from edificios import Edificio, EdificioResidencial
from estilos_arquitectonicos import EstiloArquitectonico, EstiloModerno, EstiloContemporaneo


class FabricaEdificios(ABC):
    @abstractmethod
    def crear_edificio(self) -> Edificio:
        pass

    @abstractmethod
    def crear_estilo_arquitectonico(self) -> EstiloArquitectonico:
        pass

    def crear_ciudad(self, cantidad_edificios: int) -> list:
        ciudad = []
        for _ in range(cantidad_edificios):
            edificio = self.crear_edificio()
            estilo = self.crear_estilo_arquitectonico()
            ciudad.append((edificio, estilo))
        return ciudad

class FabricaEdificiosConcretos(FabricaEdificios):
    def crear_edificio(self) -> Edificio:
        return EdificioResidencial()

    def crear_estilo_arquitectonico(self) -> EstiloArquitectonico:
        return EstiloModerno()

class FabricaEdificiosConcretosAmpliada(FabricaEdificios):
    def crear_edificio(self) -> Edificio:
        return FabricaEdificiosConcretos().crear_edificio()

    def crear_estilo_arquitectonico(self) -> EstiloArquitectonico:
        return EstiloContemporaneo()
