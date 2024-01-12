
# eventos.py
from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dominio_diseno_construccion import Proyecto, Fase

@dataclass
class ProyectoIniciado:
    proyecto: Proyecto


@dataclass
class FaseCompletada:
    proyecto: Proyecto
    fase: Fase