import socket
from ping3 import ping

import reportes

PUERTOS_CONOCIDOS = {
    21: "--> ftp",
    22: "--> ssh",
    80: "--> http",
    443: "--> https",
}


def ping_dominio():
    host = input("Ingrese un dominio: ")
    try:
        respuesta = ping(host)
        respuesta_str = str(respuesta)
        s = respuesta_str[0:5]
        info_dominio = socket.gethostbyaddr(host)

        if respuesta is not False and respuesta is not None:
            print(f"""

        HOST ACTIVO

        Tiempo:
        {s}

        IP:
        {host}

        Nombre:
        {info_dominio}
        """)
        else:
            print("El host no esta activo")
    except:
        print("El host no esta activo o el dominio/IP estan mal escritos")

    input("\nPresiona Enter para volver al menú principal...")


def escanear_puertos():
    ip = input("Ingrese una IP/dominio: ")
    seleccion = input("Presione '1' para especificar puerto o escriba '2' para elegir rango: ")

    if seleccion == "2":
        puerto_inicial = input("Escriba el puerto de inicio: ")
        puerto_final = input("Escriba el puerto final: ")
        puerto_inicial_ent = int(puerto_inicial)
        puerto_final_ent = int(puerto_final)

        print(" ")
        print(f"objetivo: {ip}")
        print("Escaneando...")

        puertos_abiertos = []
        for i in range(puerto_inicial_ent, puerto_final_ent + 1):
            socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cliente.settimeout(0.8)
            conexion = socket_cliente.connect_ex((ip, i))
            socket_cliente.close()
            if conexion == 0:
                puertos_abiertos.append(i)

        if puertos_abiertos:
            print(f"Los puerto/os abierto/os son: {puertos_abiertos}")
            for puerto in puertos_abiertos:
                if puerto in PUERTOS_CONOCIDOS:
                    print(puerto, PUERTOS_CONOCIDOS[puerto])
        else:
            print("Todos los puertos estan cerrados o el host esta apagado")

        reportes.generar_reporte(
            ip,
            puertos_abiertos=puertos_abiertos,
            rango=(puerto_inicial, puerto_final),
        )

    if seleccion == "1":
        puerto = input("Escriba el puerto especifico: ")
        puerto_esp = int(puerto)

        print(" ")
        print(f"objetivo: {ip}")
        print("Escaneando...")

        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexion = socket_cliente.connect_ex((ip, puerto_esp))
        socket_cliente.close()

        if conexion == 0:
            if puerto_esp in PUERTOS_CONOCIDOS:
                print(f"Puerto abierto: {puerto_esp}", PUERTOS_CONOCIDOS[puerto_esp])
            else:
                print(f"Puerto abierto: {puerto_esp}")
        else:
            print("El puerto especifico no esta abierto o el host esta apagado")

        reportes.generar_reporte(
            ip,
            puertos_abiertos=(puerto_esp if conexion == 0 else None),
            puerto_especifico=puerto,
        )

    print(" ")
    input("\nPresiona Enter para volver al menú principal...")


def resolver_dns():
    print("""
    =====================================
                Resolve DNS
    =====================================
    """)
    dominio = input("Ingrese el Dominio host: ")
    try:
        ip = socket.gethostbyname(dominio)
        print(f"La IP del dominio {dominio} es {ip}")
    except socket.gaierror:
        print("No se pudo resolver el DNS del dominio")

    input("\nPresiona Enter para volver al menú principal...")