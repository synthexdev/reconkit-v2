import platform
import socket
import psutil


def mostrar_info_sistema():
    info_sistema = platform.uname()
    print(" ")
    print(f"Sistema Operativo: {info_sistema.system}")
    print(" ")
    print(f"Hostname: {info_sistema.node}")
    print(" ")
    print(f"Versión del Kernel: {info_sistema.release}")
    print(" ")
    print(f"Versión del Sistema: {info_sistema.version}")
    print(" ")
    print("Versión de la distro:", platform.freedesktop_os_release().get('VERSION'))
    print(" ")
    print(f"Arquitectura: {info_sistema.machine}")
    print(" ")

    input("\nPresiona Enter para volver al menú principal...")


def mostrar_info_red():
    net_stats = psutil.net_if_stats()
    net_addrs = psutil.net_if_addrs()
    for interface, addrs in net_addrs.items():
        estado = "Activa" if net_stats[interface].isup else "Inactiva"
        print(f"\nInterfaz: {interface} ({estado})")
        for addr in addrs:
            if addr.family in [socket.AF_INET, socket.AF_INET6]:
                familia = "IPv4" if addr.family == socket.AF_INET else "IPv6"
                print(f"  - {familia}: {addr.address}")
                print(f"    Máscara: {addr.netmask}")
    print(" ")

    input("\nPresiona Enter para volver al menú principal...")