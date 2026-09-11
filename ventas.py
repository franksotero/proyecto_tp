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
            registrar_ventas(rol)
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


def buscar_venta_por_id(venta_id):
    for venta in ventas:
        if venta["id"] == venta_id:
            return venta
    return None


# CREAR
def registrar_ventas(rol):
    print("---- REGISTRAR VENTA ----")
    listar_clientes(rol)

    cliente_id = int(input("\nIngrese ID del cliente: "))
    cliente = buscar_cliente_por_id(cliente_id)

    if cliente is None:
        print("\033[31mCliente no encontrado. Operación cancelada.\033[0m")
        return
    else:  # Si el cliente existe, continuar con la venta
        una_venta = []
        while True:
            print("\n\033[1;33;44m---- LISTA DE PRODUCTOS ----\033[0m")
            listar_productos(productos)
            producto_id = int(input("\nIngrese ID del producto (0 para finalizar): "))
            if producto_id == 0:
                break  # salir del bucle si el usuario ingresa 0
            producto = buscar_producto_por_id(producto_id)

            if producto is None:
                print("\033[31mProducto no encontrado. Intente nuevamente.\033[0m")
            else:  # si el producto existe, continuar con la venta
                cantidad = int(input(f"Ingrese cantidad de {producto[1]}: "))
                if cantidad <= 0:
                    print("\033[31mCantidad inválida. Intente nuevamente.\033[0m")
                    continue
                elif cantidad > producto[4]:
                    print("\033[31mStock insuficiente.\033[0m")
                    continue

                subtotal = producto[3] * cantidad  # precio unitario * cantidad
                precio_final = subtotal - (subtotal * producto[5])  # descuento
                producto[4] -= cantidad  # actualizar stock del producto

                item_existe = None

                for item in una_venta:
                    if item["producto_id"] == producto_id:
                        item_existe = item
                        break

                if item_existe is None:
                    # agregar un nuevo item a la venta
                    una_venta.append(
                        {
                            "producto_id": producto[0],
                            "nombre": producto[1],
                            "categoria": producto[2],
                            "cantidad": cantidad,
                            "precio_unitario": producto[3],
                            "descuento": producto[5],
                            "subtotal": subtotal,
                            "precio_final": precio_final,
                        }
                    )
                else:
                    # actualizar la cantidad y el subtotal del producto existente en la venta
                    item_existe["cantidad"] += cantidad
                    item_existe["subtotal"] += subtotal
                    item_existe["precio_final"] += precio_final

                print(f"\nItem agregado: {producto[1]}")
                print(f"Subtotal: ${subtotal}")
                print(f"Precio Final: ${precio_final}")

        if len(una_venta) == 0:
            print("\033[31mNo se registró ningún producto. Venta cancelada.\033[0m")
            return

        diccionario_venta = {
            "id": max((venta["id"] for venta in ventas), default=0) + 1,
            "cliente_id": cliente[0],
            "cliente_nombre": cliente[1],
            "items": una_venta,
            # Suma de los precios finales de cada item
            "total": sum(item["precio_final"] for item in una_venta),
        }

        ventas.append(diccionario_venta)
        print("\033[32m\nVenta registrada correctamente.\033[0m")
        print(f"Total de la venta: ${diccionario_venta['total']}")


# LEER
def listar_ventas():
    print("\n\033[1;33;44m---- LISTA DE VENTAS ----\033[0m")
    print(
        f"{'ID VENTA':<8} | {'ID CLIENTE':<10} | {'NOMBRE Y APELLIDO':<17} | {'ITEMS':<5} | {'UNIDADES':<8} | {'TOTAL':<10}"
    )
    print("-" * 70)
    for venta in ventas:
        print(
            f"{venta['id']:<8} | {venta['cliente_id']:<10} | {venta['cliente_nombre']:<17} | {len(venta['items']):<5} | {sum(item['cantidad'] for item in venta['items']):<8} | ${venta['total']:<10}"
        )

    venta_id = int(
        input("\nIngrese el ID de la venta para ver detalles o presione 0 para salir: ")
    )
    if venta_id == 0:
        return

    for venta in ventas:
        if venta["id"] == venta_id:
            print(f"\nDetalles de la venta ID {venta_id}:")
            print(
                f"{'ID PRODUCTO':<12} | {'NOMBRE Y APELLIDO':<22} | {'CATEGORÍA':<12} | {'CANTIDAD':<8} | {'PRECIO UNITARIO':<15} | {'DESCUENTO':<10} | {'SUBTOTAL':<10} | {'PRECIO FINAL':<12}"
            )
            print("-" * 120)
            for item in venta["items"]:
                print(
                    f"{item['producto_id']:<12} | {item['nombre']:<22} | {item['categoria']:<12} | {item['cantidad']:<8} | ${item['precio_unitario']:<14.2f} | {item['descuento'] * 100:<9.1f}% | ${item['subtotal']:<9} | ${item['precio_final']:<11}"
                )
            print("-" * 120)
            print(f"Total de la venta: ${venta['total']}")
            return
    print("\033[31mID de venta no encontrado.\033[0m")


# ACTUALIZAR
def actualizar_ventas():
    print("---- ACTUALIZAR VENTAS ----")

    print("\n\033[1;33;44m---- LISTA DE VENTAS ----\033[0m")
    print(f"{'ID VENTA':<8} | {'NOMBRE Y APELLIDO':<17} | {'ITEMS':<5} | {'TOTAL':<10}")
    print("-" * 70)
    for venta in ventas:
        print(
            f"{venta['id']:<8} | {venta['cliente_nombre']:<17} | {len(venta['items']):<5} | ${venta['total']:<10}"
        )

    venta_id = int(input("\nIngrese el ID de la venta a actualizar: "))
    venta = buscar_venta_por_id(venta_id)

    if venta is None:
        print("\033[31mID de venta no encontrado.\033[0m")
        return

    print(
        f"{'ID PRODUCTO':<12} | {'NOMBRE Y APELLIDO':<22} | {'CANTIDAD':<8} | {'PRECIO FINAL':<12}"
    )
    print("-" * 120)
    for item in venta["items"]:
        print(
            f"{item['producto_id']:<12} | {item['nombre']:<22} | {item['cantidad']:<8} | ${item['precio_final']:<12}"
        )
        print("-" * 120)
        print(f"Total de la venta: ${venta['total']}")

    producto_id = int(input("\nIngrese el ID del producto a actualizar: "))
    item = next(
        (item for item in venta["items"] if item["producto_id"] == producto_id),
        None,
    )

    if item is None:
        print("\033[31mID de producto no encontrado.\033[0m")
        return

    producto = buscar_producto_por_id(producto_id)
    cantidad_anterior = item["cantidad"]
    producto[4] += cantidad_anterior

    nueva_cantidad = int(
        input(
            f"Ingrese la nueva cantidad de {producto[1]} "
            f"(0 para eliminar el producto, stock disponible: {producto[4]}): "
        )
    )
    while nueva_cantidad < 0 or nueva_cantidad > producto[4]:
        print(
            "\033[31mCantidad inválida. Debe ser 0 o mayor y no superar el stock disponible.\033[0m"
        )
        nueva_cantidad = int(
            input(
                f"Ingrese la nueva cantidad de {producto[1]} "
                f"(0 para eliminar el producto, stock disponible: {producto[4]}): "
            )
        )

    if nueva_cantidad == 0:
        venta["items"].remove(item)
        venta["total"] = sum(item["precio_final"] for item in venta["items"])

        if len(venta["items"]) == 0:
            ventas.remove(venta)
            print("\033[32mVenta eliminada porque quedó sin productos.\033[0m")
        else:
            print("\033[32mProducto eliminado de la venta.\033[0m")
            print(f"Nuevo total de la venta: ${venta['total']}")
        return

    producto[4] -= nueva_cantidad
    subtotal = producto[3] * nueva_cantidad
    precio_final = subtotal - (subtotal * producto[5])

    item["cantidad"] = nueva_cantidad
    item["subtotal"] = subtotal
    item["precio_final"] = precio_final
    venta["total"] = sum(item["precio_final"] for item in venta["items"])

    print("\033[32mVenta actualizada correctamente.\033[0m")
    print(f"Nuevo total de la venta: ${venta['total']}")


# ELIMINAR
def eliminar_ventas():
    print("---- ELIMINAR VENTA ----")

    if len(ventas) == 0:
        print("\033[31mNo hay ventas registradas.\033[0m")
        return

    print(f"{'ID VENTA':<8} | {'NOMBRE Y APELLIDO':<17} | {'ITEMS':<5} | {'TOTAL':<10}")
    print("-" * 70)
    for venta in ventas:
        print(
            f"{venta['id']:<8} | {venta['cliente_nombre']:<17} | "
            f"{len(venta['items']):<5} | ${venta['total']:<10}"
        )

    venta_id = int(input("\nIngrese el ID de la venta a eliminar (0 para salir): "))
    if venta_id == 0:
        return

    venta = buscar_venta_por_id(venta_id)
    if venta is None:
        print("\033[31mID de venta no encontrado.\033[0m")
        return

    confirmacion = input(f"¿Confirma eliminar la venta {venta_id}? (si/no): ").lower()
    if confirmacion != "si":
        print("Operación cancelada.")
        return

    for item in venta["items"]:
        producto = buscar_producto_por_id(item["producto_id"])
        if producto is not None:
            producto[4] += item["cantidad"]

    ventas.remove(venta)
    print("\033[32mVenta eliminada y stock restaurado correctamente.\033[0m")
