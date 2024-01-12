from abc import ABC, abstractmethod
import copy

class EstiloArquitectonico(ABC):
    @abstractmethod
    def duplica(self):
        pass


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
