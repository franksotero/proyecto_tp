"""
Modulo para la visualizacion de reportes y estadisticas generales del sistema.
"""

def menu_estadisticas():
    """
    Despliega el menu de opciones para consultar estadisticas de productos, clientes, ventas o reportes generales
    """
    opcion = ""
    while opcion != "6":
        print("\n==================================")
        print("       GESTIÓN DE ESTADISTICAS      ")
        print("==================================")
        print("1. Estadisticas de productos")
        print("2. Estadisticas de clientes")
        print("3. Estadisticas de ventas")
        print("4. Reportes generales")
        print("5. Salir al menú principal")
        opcion = input("Elige una opción (1-5): ")
        if opcion == "1":
            estadisticas_productos()
        elif opcion == "2":
            estadisticas_clientes() 
        elif opcion == "3":
            estadisticas_ventas()
        elif opcion == "4":
            reportes()
        elif opcion == "5":
            print("\nRegresando al menú principal...")
        else:
            print("\nOpción no válida. Intenta de nuevo.")
        

