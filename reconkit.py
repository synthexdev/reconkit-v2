import interfaz
import sistema
import reconocimiento

interfaz.mostrar_banner()
interfaz.carga_falsa(2)

while True:
    interfaz.limpiar_pantalla()
    usuario = interfaz.mostrar_menu()

    if usuario == "1":
        reconocimiento.ping_dominio()

    if usuario == "2":
        reconocimiento.escanear_puertos()

    if usuario == "3":
        reconocimiento.resolver_dns()

    if usuario == "4":
        sistema.mostrar_info_sistema()

    if usuario == "5":
        sistema.mostrar_info_red()

    if usuario == "0":
        print("\nCerrando ReconKit v2. Hasta luego!")
        break