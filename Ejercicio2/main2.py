from dominio_edificios import Edificio, EstiloArquitectonico, RegulacionLocal
from dominio_diseno_construccion import DiseñoArquitectonico
from dominio_regulaciones import RestriccionAltura, RequisitoEficienciaEnergetica, Regulacion
from funciones_sistema import iniciar_proyecto, completar_fase, cumplir_regulaciones

def ejercicio2_main():
    
    estilo_moderno = EstiloArquitectonico(nombre="Moderno")
    regulacion_local_casa = RegulacionLocal(restriccion_altura=50, eficiencia_energetica="A")

    casa = Edificio(nombre="Casa", tipo="Residencial", estilo=estilo_moderno, regulacion_local=regulacion_local_casa)

    diseño_casa = DiseñoArquitectonico(detalles="Diseño detallado de la casa")

    proyecto_iniciado = iniciar_proyecto(
        nombre="Proyecto Casa",
        fases=["Diseño", "Construcción", "Mantenimiento"],
        diseño_arquitectonico=diseño_casa,
        edificio=casa
    )

    fase_completada = completar_fase(proyecto=proyecto_iniciado.proyecto, nombre_fase="Diseño")

    regulacion_casa = Regulacion(
        normativa_local="Normativa Local",
        restriccion_altura=RestriccionAltura(max_altura=60),
        requisito_eficiencia_energetica=RequisitoEficienciaEnergetica(nivel_eficiencia="A"),
    )

    cumple_regulaciones = cumplir_regulaciones(edificio=casa, regulacion=regulacion_casa)
    print("\nResultados del Proyecto:")
    print("Proyecto Iniciado:", proyecto_iniciado)
    print("\nFase Completada:", fase_completada)
    print("\nCumple Regulaciones:", cumple_regulaciones)

    
if __name__ == "__main__":
    ejercicio2_main()