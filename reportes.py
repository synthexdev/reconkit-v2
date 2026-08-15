import os
from datetime import datetime


def generar_reporte(ip, puertos_abiertos, rango=None, puerto_especifico=None):
    reporte = input("Deseas generar un reporte del resultado?[S/N]: ")
    if reporte.lower() != "s":
        return

    nombre_usuario = input("Introduce el nombre para el reporte: ")
    nombre_archivo = f"{nombre_usuario}.txt"
    tiempo = datetime.now()

    if rango:
        detalle = f"Rango de puertos escaneado: {rango}"
    else:
        detalle = f"Puerto escaneado: {puerto_especifico}"

    texto_archivo = f"""
    =====================================

            ReconKit V2 Report

    =====================================

        Objetivo: {ip}
        Fecha: {tiempo.strftime("%d/%m/%Y")}
        hora: {tiempo.strftime("%H:%M:%S")}

        {detalle}

        Puertos abiertos: {puertos_abiertos}
    """

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto_archivo)

    ruta = os.path.join(os.getcwd(), nombre_archivo)
    print(f"Reporte creado con exito en {ruta}")