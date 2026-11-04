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
    """Muestra estadísticas de productos vendidos y su distribución por categoría."""
    if not ventas:
        print("\n No hay ventas registradas. Volviendo al menú de estadísticas...")
        return

    print(f"\n--- ESTADÍSTICAS DE PRODUCTOS ({rol.upper()}) ---")
    conteo_productos = {}
    conteo_categorias = {}
    recaudacion_categorias = {}

    total_unidades_vendidas = 0

    for v in ventas:
        for item in v["items"]:
            prod_nombre = item["nombre"]
            cat_nombre = item["categoria"].lower()
            cant = item["cantidad"]
            monto = item["precio_final"]
            conteo_productos[prod_nombre] = conteo_productos.get(prod_nombre, 0) + cant

            conteo_categorias[cat_nombre] = conteo_categorias.get(cat_nombre, 0) + cant
            recaudacion_categorias[cat_nombre] = (recaudacion_categorias.get(cat_nombre, 0.0) + monto)

            total_unidades_vendidas += cant

    producto_top = max(conteo_productos, key=conteo_productos.get)
    print(f"- Producto más vendido: {producto_top} ({conteo_productos[producto_top]} unidades)")

    if rol == "admin":
        producto_min = min(conteo_productos, key=conteo_productos.get)
        print(f"- Producto menos vendido: {producto_min} ({conteo_productos[producto_min]} unidades)")
    print(f"\n- Conteo total de unidades vendidas en la tienda: {total_unidades_vendidas}")

    print("\n--- DESGLOSE POR CATEGORIA ---")
    print(f"{'CATEGORÍA':<15} | {'UNIDADES':<10} | {'RECAUDACIÓN ($)':<16} | {'PROMEDIO/UNID ($)':<18} | {'% DEL TOTAL':<12}")
    print("-" * 80)

    for cat, unidades in conteo_categorias.items():
        recaudado = recaudacion_categorias[cat]
        promedio_unidad = recaudado / unidades if unidades > 0 else 0
        porcentaje_relativo = (unidades / total_unidades_vendidas) * 100 if total_unidades_vendidas > 0 else 0

        print(
            f"{cat.capitalize():<15} | {unidades:<10} | ${recaudado:<15.2f} | ${promedio_unidad:<17.2f} | {porcentaje_relativo:<11.1f}%"
        )
    print("-" * 80)


# --- ESTADÍSTICAS DE CLIENTES ---
def estadisticas_clientes(ventas, rol):
    """Muestra los clientes con mayor y menor gasto según el rol del usuario."""
    if not ventas:
        print("\nNo hay ventas registradas. Volviendo al menú de estadísticas...")
        return

    print(f"\n--- ESTADISTICAS DE CLIENTES ({rol.upper()}) ---")
    gastos = {}
    for v in ventas:
        gastos[v["cliente_nombre"]] = gastos.get(v["cliente_nombre"], 0.0) + v["total"]

    cliente_top = max(gastos, key=gastos.get)
    print(f"- Cliente que más gastó: {cliente_top} (${gastos[cliente_top]:.2f})")

    if rol == "admin":
        cliente_min = min(gastos, key=gastos.get)
        print(f"- Cliente que menos gastó: {cliente_min} (${gastos[cliente_min]:.2f})")

# --- ESTADÍSTICAS DE VENTAS ---
def estadisticas_ventas(ventas, rol):
    """Muestra el promedio, cantidad, máximo y mínimo de las ventas registradas."""
    if not ventas:
        print("\nNo hay ventas registradas. Volviendo al menú de estadísticas...")
        return

    print(f"\n--- ESTADISTICAS DE VENTAS ({rol.upper()}) ---")
    promedio = sum(v["total"] for v in ventas) / len(ventas)
    print(f"- Promedio general por venta: ${promedio:.2f}")
    print(f"- Cantidad total de operaciones registradas: {len(ventas)}")

    if rol == "admin":
        mayor = max(ventas, key=lambda v: v["total"])
        menor = min(ventas, key=lambda v: v["total"])
        print(f"- Mayor venta registrada: Venta ID {mayor['id']} (${mayor['total']:.2f})")
        print(f"- Menor venta registrada: Venta ID {menor['id']} (${menor['total']:.2f})")

def reportes(ventas, clientes, rol):
    """Muestra el reporte general combinando las estadísticas del sistema."""
    print("\n==================================")
    print("      REPORTE GENERAL COMPLETO    ")
    print("==================================")
    estadisticas_productos(ventas, rol)
    estadisticas_clientes(ventas, rol)
    estadisticas_ventas(ventas, rol)
    print("==================================")