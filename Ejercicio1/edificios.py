from abc import ABC, abstractmethod
import copy

class Edificio(ABC):
    @abstractmethod
    def duplica(self):
        pass


class EdificioResidencial(Edificio):
    def duplica(self):
        return copy.deepcopy(self)


class EdificioComercial(Edificio):
    def duplica(self):
        return copy.deepcopy(self)


class EdificioIndustrial(Edificio):
    def duplica(self):
        return copy.deepcopy(self)
