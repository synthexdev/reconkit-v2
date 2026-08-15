import os
import sys
import time


def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' para Linux y macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def carga_falsa(segundos=2):
    simbolos = ["/", "-", "|", "\\"]
    # Cada vuelta dura 0.1 segundos
    pasos = int(segundos / 0.1)

    print("\n")
    for i in range(pasos):
        simbolo = simbolos[i % len(simbolos)]
        # \r regresa el cursor al inicio de la línea sin saltar
        sys.stdout.write(f"\r[+] Cargando módulos de ReconKit... [{simbolo}]")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n[+] ¡Listo! Iniciando interfaz...")
    time.sleep(0.5)


def mostrar_banner():
    print("""

████  █████  ███   ███  █   █ █   █ ███ █████    █   █  ███
█░░░█ █░░░░░█ ░░░ █ ░░█ ██  █░█░ █ ░ █░░ ░█░░░   █░  █░█ ░░█
████░░████░░█░ ░░░█░ ░█░█░█ █░███ ░ ░█░░░ █░░░░  █░░ █░░░ █░░
█░░█░ █░░░░ █░░   █░░ █░█░░██░█░░█ ░ █░░  █░░     █░█ ░░ █ ░
█░░░█░█████░ ███   ███ ░█░░ █░█░░░█ ███░  █░░      █ ░ █████░   
 ░░  ░ ░░░░░  ░░░   ░░░ ░░░  ░░░░  ░ ░░░   ░░       ░ ░ ░░░░░
  ░   ░ ░░░░░  ░░░   ░░░  ░   ░ ░   ░ ░░░   ░        ░   ░░░░░

[+] ReconKit v2
[+] Python 3.x
[+] By: Synthex
""")


def mostrar_menu():
    print("""

=====================================

            ReconKit v2

=====================================

      [RECONOCIMIENTO]
1) Ping a Dominio
2) Escanear IP/Dominio
3) Resolver DNS

     [SISTEMA]
4) Info del sistema principal
5) Info de la red
0) Salir

""")
    return input("Ingrese una opcion: ")