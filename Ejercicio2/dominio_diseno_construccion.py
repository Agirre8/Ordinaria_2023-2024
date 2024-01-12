
from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class DiseñoArquitectonico:
    detalles: str


@dataclass
class Fase:
    nombre: str
    completada: bool = False


@dataclass
class Proyecto:
    nombre: str
    fases: List[Fase]
    diseño_arquitectonico: DiseñoArquitectonico
    edificio: Edificio