"""
Modulo para la visualizacion de reportes y estadisticas generales del sistema.
"""
from clientes import clientes
from ventas import ventas 

def menu_estadisticas(ventas,clientes,rol):
    """
    Despliega el menu de opciones para consultar estadisticas de productos, clientes, ventas o reportes generales
    """
    opcion = ""
    while opcion != "5":
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
            estadisticas_productos(ventas,rol)
        elif opcion == "2":
            estadisticas_clientes(ventas,rol) 
        elif opcion == "3":
            estadisticas_ventas(ventas,rol)
        elif opcion == "4":
            reportes(ventas,clientes,rol)
        elif opcion == "5":
            print("\nRegresando al menú principal...")
        else:
            print("\nOpción no válida. Intenta de nuevo.")


def estadisticas_productos(ventas, rol):
    if not ventas:
        print("\n No hay ventas registradas. Volviendo al menú de estadísticas...")
        return

    print(f"\n--- ESTADÍSTICAS DE PRODUCTOS ({rol.upper()}) ---")
    conteo = {}
    for v in ventas:
        for item in v["items"]:
            conteo[item["nombre"]] = conteo.get(item["nombre"], 0) + item["cantidad"]

    producto_top = max(conteo, key=conteo.get)
    print(f"Más vendido: {producto_top} ({conteo[producto_top]} unidades)")

    if rol == "admin":
        producto_min = min(conteo, key=conteo.get)
        print(f"Menos vendido: {producto_min} ({conteo[producto_min]} unidades)")


# --- ESTADÍSTICAS DE CLIENTES ---
def estadisticas_clientes(ventas, rol):
    if not ventas:
        print("\nNo hay ventas registradas. Volviendo al menú de estadísticas...")
        return

    print(f"\n--- ESTADÍSTICAS DE CLIENTES ({rol.upper()}) ---")
    gastos = {}
    conteo = {}
    for v in ventas:
        gastos[v["cliente_nombre"]] = gastos.get(v["cliente_nombre"], 0) + v["total"]
        conteo[v["cliente_nombre"]] = conteo.get(v["cliente_nombre"], 0) + 1

    cliente_top = max(gastos, key=gastos.get)
    print(f"Cliente que más gastó: {cliente_top} (${gastos[cliente_top]})")

    if rol == "admin":
        cliente_min = min(conteo, key=conteo.get)
        print(f"Cliente con menos ventas: {cliente_min} ({conteo[cliente_min]} ventas)")


# --- ESTADÍSTICAS DE VENTAS ---
def estadisticas_ventas(ventas, rol):
    if not ventas:
        print("\n No hay ventas registradas. Volviendo al menú de estadísticas...")
        return

    print(f"\n--- ESTADÍSTICAS DE VENTAS ({rol.upper()}) ---")
    promedio = sum(v["total"] for v in ventas) / len(ventas)
    print(f"Promedio de ventas: ${promedio:.2f}")

    if rol == "admin":
        mayor = max(ventas, key=lambda v: v["total"])
        menor = min(ventas, key=lambda v: v["total"])
        print(f"Mayor venta: ID {mayor['id']} (${mayor['total']})")
        print(f"Menor venta: ID {menor['id']} (${menor['total']})")


def reportes(ventas, clientes, rol):
    print("\n=== REPORTE GENERAL ===")
    estadisticas_productos(ventas, rol)
    estadisticas_clientes(ventas, rol)
    estadisticas_ventas(ventas, rol)
    print("=======================")