from clientes import menu_clientes
from estadisticas import menu_estadisticas
from productos import menu_productos
from usuarios import iniciar_sesion, registrar_usuario
from ventas import menu_ventas


def menu_inicio():
    opcion = ""
    while opcion != "3":
        print("\n=== BIENVENIDO AL SISTEMA DEL SUPERMERCADO ===")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Salir")
        opcion = input("Elige una opción (1, 2 o 3): ")
        if opcion == "1":
            rol = iniciar_sesion()
            if rol:
                menu_principal(rol)
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("\n¡Hasta luego!")
        else:
            print("Opción no válida. Intenta de nuevo.")


def menu_principal(rol):
    opcion = ""
    while opcion != "5":
        print(f"\n======================================")
        print(f"  SISTEMA DE GESTIÓN DEL SUPERMERCADO ({rol.upper()})  ")
        print(f"======================================")
        print("1. Módulo de Productos")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas")
        print("4. Módulo de Estadisticas")
        print("5. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_productos(rol)
        elif opcion == "2":
            menu_clientes(rol)
        elif opcion == "3":
            menu_ventas(rol)
        elif opcion == "4":
            menu_estadisticas(rol)
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema!")
        else:
            print("Opción no válida.")


menu_inicio()
