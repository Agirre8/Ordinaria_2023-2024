
from dataclasses import dataclass

@dataclass
class EstiloArquitectonico:
    nombre: str


@dataclass
class RegulacionLocal:
    restriccion_altura: int
    eficiencia_energetica: str


@dataclass
class Edificio:
    nombre: str
    tipo: str
    estilo: EstiloArquitectonico
    regulacion_local: RegulacionLocal
