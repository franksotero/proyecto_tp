from productos import menu_productos, productos
from clientes import menu_clientes, clientes
from usuarios import iniciar_sesion, registrar_usuario, generar_usuario
from ventas import registrar_venta , menu_ventas

def menu_inicio():
    opcion = ""
    while opcion != "3":
        print("\n=== BIENVENIDO AL SISTEMA DEL SUPERMERCADO ===")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Salir")
        opcion = input("Elige una opción (1, 2 o 3): ")
        if opcion == "1":
            if iniciar_sesion():
                menu_principal()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("\n¡Hasta luego!")
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_principal():
    opcion = ""
    while opcion != "4":
        print("\n======================================")
        print("  SISTEMA DE GESTIÓN DEL SUPERMERCADO  ")
        print("======================================")
        print("1. Módulo de Productos")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema!")
        else:
            print("Opción no válida.")


menu_inicio()
