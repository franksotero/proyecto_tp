from clientes import clientes, listar_clientes
from productos import listar_productos, productos

"""
Estructura de una venta:
    {
        "id": 1,
        "cliente_id": 1,
        "cliente_nombre": "Ana Gomez",
        "items": [
            {"producto_id": 1, "nombre": "Pan lactal", "categoria": "almacen",
             "cantidad": 2, "precio_unitario": 1200.0, "descuento": 0.0, "subtotal": 2400.0},
            ...
        ],
        "total": 4110.0,
        "estado": "activa"   # o "cancelada"
    }
"""

ventas = []


def menu_ventas(rol):
    opcion = ""
    while opcion != "5":
        print("\n=================================")
        print(f"\033[1;34m        GESTIÓN DE VENTAS ({rol.upper()})         \033[0m")
        print("=================================")
        print("1. Registrar ventas ")
        print("2. Consultar ventas")
        print("3. Actualizar ventas")
        print("4. Eliminar ventas")
        print("5. Volver al menu principal")
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            registrar_ventas()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            actualizar_ventas()
        elif opcion == "4":
            eliminar_ventas()
        elif opcion == "5":
            print("\033[1;34mRegresando al menu principal...\033[0m")
        else:
            print("\033[31mOpción invalida\033[0m")


def buscar_cliente_por_id(cliente_id):
    for cliente in clientes:
        if cliente[0] == cliente_id:
            return cliente
    return None


def buscar_producto_por_id(producto_id):
    for producto in productos:
        if producto[0] == producto_id:
            return producto
    return None


# CREAR
def registrar_ventas():
    print("---- REGISTRAR VENTA ----")
    listar_clientes()

    cliente_id = int(input("\nIngrese ID del cliente: "))
    cliente = buscar_cliente_por_id(cliente_id)

    if cliente is None:
        print("\033[31mCliente no encontrado. Operación cancelada.\033[0m")
        return
    else:  # Si el cliente existe, continuar con la venta
        una_venta = []
        producto_id = 1
        while producto_id != 0:
            listar_productos()
            producto_id = int(input("\nIngrese ID del producto (0 para finalizar): "))
            producto = buscar_producto_por_id(producto_id)

            if producto is None:
                print("\033[31mProducto no encontrado. Intente nuevamente.\033[0m")
            else:  # si el producto existe, continuar con la venta
                cantidad = int(
                    input(
                        f"Ingrese cantidad de {producto[1]} (En stock: {producto[3]}): "
                    )
                )
                while cantidad <= 0 or cantidad > producto[3]:
                    print(
                        "Error: Cantidad inválida. Debe ser mayor que 0 y menor o igual al stock disponible."
                    )
                    cantidad = int(
                        input(
                            f"Ingrese cantidad de {producto[1]} (En stock: {producto[3]}): "
                        )
                    )

                subtotal = producto[3] * cantidad  # precio unitario * cantidad
                precio_final = subtotal - (subtotal * producto[4])

                una_venta.append(
                    {
                        "producto_id": producto[0],
                        "nombre": producto[1],
                        "categoria": producto[2],
                        "cantidad": cantidad,
                        "precio_unitario": producto[3],
                        "descuento": producto[4],
                        "subtotal": subtotal,
                        "precio_final": precio_final,
                    }
                )

        diccionario_venta = {
            "id": len(ventas) + 1,
            "cliente_id": cliente[0],
            "cliente_nombre": cliente[1],
            "items": una_venta,
            # Suma de los precios finales de cada item
            "total": sum(item["precio_final"] for item in una_venta),
        }

        ventas.append(diccionario_venta)
        print("\033[32mVenta registrada correctamente.\033[0m")


# LEER
def listar_ventas():
    print("listar ventas")


# ACTUALIZAR
def actualizar_ventas():
    print("actualizar ventas")


# ELIMINAR
def eliminar_ventas():
    print("eliminar ventas")
