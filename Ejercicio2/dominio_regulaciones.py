# dominio_regulaciones.py
from dataclasses import dataclass

@dataclass
class RestriccionAltura:
    max_altura: int


@dataclass
class RequisitoEficienciaEnergetica:
    nivel_eficiencia: str


@dataclass
class Regulacion:
    normativa_local: str
    restriccion_altura: RestriccionAltura
    requisito_eficiencia_energetica: RequisitoEficienciaEnergetica