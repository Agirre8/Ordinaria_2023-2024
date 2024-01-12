# funciones_sistema.py
from dominio_edificios import Edificio, EstiloArquitectonico, RegulacionLocal
from dominio_diseno_construccion import DiseñoArquitectonico, Fase, Proyecto
from dominio_regulaciones import RestriccionAltura, RequisitoEficienciaEnergetica, Regulacion
from eventos import ProyectoIniciado, FaseCompletada
from typing import List

def iniciar_proyecto(nombre: str, fases: List[str], diseño_arquitectonico: DiseñoArquitectonico, edificio: Edificio) -> Proyecto:
    fases_proyecto = [Fase(nombre=fase) for fase in fases]
    proyecto = Proyecto(nombre=nombre, fases=fases_proyecto, diseño_arquitectonico=diseño_arquitectonico, edificio=edificio)
    return ProyectoIniciado(proyecto=proyecto)

def completar_fase(proyecto: Proyecto, nombre_fase: str) -> FaseCompletada:
    fase = next((f for f in proyecto.fases if f.nombre == nombre_fase), None)
    if fase:
        fase.completada = True
        return FaseCompletada(proyecto=proyecto, fase=fase)
    else:
        raise ValueError(f"No se encontró la fase con el nombre {nombre_fase}")

def cumplir_regulaciones(edificio: Edificio, regulacion: Regulacion) -> bool:
    return (
        edificio.regulacion_local.restriccion_altura <= regulacion.restriccion_altura.max_altura
        and edificio.regulacion_local.eficiencia_energetica == regulacion.requisito_eficiencia_energetica.nivel_eficiencia
    )
