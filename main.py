from clientes import menu_clientes
from productos import menu_productos
from usuarios import iniciar_sesion, registrar_usuario
from ventas import menu_ventas

def menu_inicio():
    opcion = ""
    while opcion != "3":
        print("\n\033[4;35m=== BIENVENIDO AL SISTEMA DEL SUPERMERCADO ===\033[0m")
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
            print("\n\033[32m¡Hasta luego!\033[0m")
        else:
            print("\033[31mOpción no válida. Intenta de nuevo.\033[0m")

def menu_principal(rol):
    opcion = ""
    while opcion != "4":
        print(f"\n======================================")
        print(f"\033[32m  SISTEMA DE GESTIÓN DEL SUPERMERCADO ({rol.upper()})  \033[0m")
        print(f"======================================")
        print("1. Módulo de Productos")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas")
        print("4. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_productos(rol)
        elif opcion == "2":
            menu_clientes(rol)
        elif opcion == "3":
            menu_ventas(rol)
        elif opcion == "4":
            print("\n\033[32m¡Gracias por usar el sistema!\033[0m")
        else:
            print("\033[31mOpción no válida.\033[0m")

menu_inicio()
