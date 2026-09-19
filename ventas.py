from datetime import date
from functools import reduce
from clientes import clientes, listar_clientes
from productos import listar_productos, productos


ventas = [
    {
        "id": 1,
        "cliente_id": 1,
        "cliente_nombre": "Ana Gomez",
        "fecha": (18, 9, 2026),
        "items": [
            {
                "producto_id": 1,
                "nombre": "Pan lactal",
                "categoria": "almacen",
                "cantidad": 2,
                "precio_unitario": 1200.0,
                "descuento": 0.0,
                "subtotal": 2400.0,
                "precio_final": 2400.0,
            },
            {
                "producto_id": 2,
                "nombre": "Detergente",
                "categoria": "limpieza",
                "cantidad": 1,
                "precio_unitario": 2500.0,
                "descuento": 0.10,
                "subtotal": 2500.0,
                "precio_final": 2250.0,
            },
        ],
        "total": 4650.0,
    },
    {
        "id": 2,
        "cliente_id": 2,
        "cliente_nombre": "Luis Perez",
        "fecha": (20, 8, 2026),
        "items": [
            {
                "producto_id": 6,
                "nombre": "Arroz",
                "categoria": "almacen",
                "cantidad": 5,
                "precio_unitario": 1500.0,
                "descuento": 0.0,
                "subtotal": 7500.0,
                "precio_final": 7500.0,
            },
            {
                "producto_id": 10,
                "nombre": "Aceite",
                "categoria": "almacen",
                "cantidad": 10,
                "precio_unitario": 400.0,
                "descuento": 0.15,
                "subtotal": 4000.0,
                "precio_final": 3400.0,
            },
        ],
        "total": 10900.0,
    },
    {
        "id": 3,
        "cliente_id": 3,
        "cliente_nombre": "Anastasia Diaz",
        "fecha": (14, 6, 2026),
        "items": [
            {
                "producto_id": 4,
                "nombre": "Chocolate",
                "categoria": "golosinas",
                "cantidad": 3,
                "precio_unitario": 950.0,
                "descuento": 0.0,
                "subtotal": 2850.0,
                "precio_final": 2850.0,
            }
        ],
        "total": 2850.0,
    },
]


def menu_ventas(rol):
    """
    Muestra el menú de gestión de ventas y deriva a la operación elegida
    según la opción ingresada por el usuario. La opción de eliminar
    ventas está restringida a usuarios con rol 'admin'.
    """

    opcion = ""
    while opcion != "6":
        print("\n=================================")
        print(f"\033[1;34m        GESTIÓN DE VENTAS ({rol.upper()})         \033[0m")
        print("=================================")
        print("1. Registrar ventas ")
        print("2. Consultar ventas")
        print("3. Actualizar ventas")
        print("4. Eliminar ventas")
        print("5. Consultar compras de un cliente")
        print("6. Volver al menu principal")
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            registrar_ventas()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            actualizar_ventas()
        elif opcion == "4":
            if rol == "admin":
                eliminar_ventas()
            else:
                print(
                    "\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden eliminar una venta.\033[0m"
                )
        elif opcion == "5":
            consultar_compras_de_cliente()
        elif opcion == "6":
            print("\033[1;34mRegresando al menu principal...\033[0m")
        else:
            print("\033[31mOpción invalida\033[0m")


def buscar_cliente_por_id(cliente_id):
    """Busca un cliente por su identificador único.
    cliente_id(int): ID del cliente a buscar.
    Return:  Datos del cliente si se encuentra, none en caso contrario.
    """
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return None


def buscar_producto_por_id(producto_id):
    """
    Busca un producto en la matriz de productos utilizando su ID.
    producto_id (int): ID del producto a buscar.
    Return: la fila del producto si se encuentra, None en caso contrario.
    """

    for producto in productos:
        if producto[0] == producto_id:
            return producto
    return None


def buscar_venta_por_id(venta_id):
    """
    Busca una venta en la lista de ventas utilizando su ID.
    venta_id (int): ID de la venta a buscar.
    Return: el diccionario de la venta si se encuentra, None en caso contrario.
    """

    for venta in ventas:
        if venta["id"] == venta_id:
            return venta
    return None


def consultar_compras_de_cliente():
    """
    Pide un ID de cliente, muestra sus datos y el listado de ventas asociadas a ese cliente.
    """
    id_buscar = int(input("\nIngrese el ID del cliente a consultar: "))
    cliente = buscar_cliente_por_id(id_buscar)
    if cliente is None:
        print("\033[31mCliente no encontrado.\033[0m")
        return

    print("\n--- DATOS DEL CLIENTE ---")
    print(
        f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Tipo: {cliente['tipo_cliente']}"
    )

    compras_cliente = [venta for venta in ventas if venta["cliente_id"] == id_buscar]

    if len(compras_cliente) == 0:
        print("Este cliente no tiene compras registradas.")
        return

    print(f"\n--- COMPRAS DE {cliente['nombre'].upper()} ---")
    for venta in compras_cliente:
        print(
            f"Venta ID {venta['id']} | Fecha: {venta['fecha']} | Total: ${venta['total']}"
        )


def mostrar_ventas():
    """
    Muestra un resumen tabulado de todas las ventas registradas,
    junto con el total general facturado calculado con reduce.
    """

    print("\n\033[1;33;44m---- LISTA DE VENTAS ----\033[0m")
    print(
        f"{'ID VENTA':<8} | {'ID CLIENTE':<10} | {'NOMBRE Y APELLIDO':<17} | {'ITEMS':<5} | {'UNIDADES':<8} | {'TOTAL':<10}"
    )
    print("-" * 70)
    for venta in ventas:
        print(
            f"{venta['id']:<8} | {venta['cliente_id']:<10} | {venta['cliente_nombre']:<17} | {len(venta['items']):<5} | {sum(item['cantidad'] for item in venta['items']):<8} | ${venta['total']:<10}"
        )

    total_facturado = reduce(
        lambda acumulado, venta: acumulado + venta["total"], ventas, 0
    )
    print(f"\n\033[1;32mTotal facturado: ${total_facturado}\033[0m")


def mostrar_detalles_venta(venta):
    """
    Muestra el detalle de los productos de una venta puntual.
    venta (dict): la venta cuyos items se van a mostrar.
    """

    print(f"\nDetalles de la venta ID {venta['id']}:")
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


# CREAR
def registrar_ventas():
    """
    Permite registrar una nueva venta, seleccionando un cliente y agregando productos.
    Actualiza el stock de los productos vendidos y calcula el total de la venta.
    """
    print("---- REGISTRAR VENTA ----")
    listar_clientes()

    cliente_id = int(input("\nIngrese ID del cliente: "))
    cliente = buscar_cliente_por_id(cliente_id)

    if cliente is None:
        print("\033[31mCliente no encontrado. Operación cancelada.\033[0m")
        return

    una_venta = []

    print("\n\033[1;33;44m---- LISTA DE PRODUCTOS ----\033[0m")
    listar_productos(productos)

    producto_id = int(input("\nIngrese ID del producto (0 para finalizar): "))
    while producto_id != 0:
        producto = buscar_producto_por_id(producto_id)
        if producto is None:
            print("\033[31mProducto no encontrado. Intente nuevamente.\033[0m")
        else:
            cantidad = int(input(f"Ingrese cantidad de {producto[1]}: "))
            if cantidad <= 0:
                print("\033[31mCantidad inválida. Intente nuevamente.\033[0m")
            elif cantidad > producto[4]:
                print("\033[31mStock insuficiente. Intente nuevamente.\033[0m")
            else:
                subtotal = producto[3] * cantidad
                precio_final = subtotal - (subtotal * producto[5])
                producto[4] -= cantidad  # actualizar stock

                # verificamos si el producto ya está en la venta
                item_existe = None
                for item in una_venta:
                    if item["producto_id"] == producto_id:
                        item_existe = item

                # si el producto no existe en la venta, lo agregamos
                if item_existe is None:
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
                    # si el producto existe en la venta, actualizamos la cantidad y los totales
                    item_existe["cantidad"] += cantidad
                    item_existe["subtotal"] += subtotal
                    item_existe["precio_final"] += precio_final

                print(f"\n\033[32mProducto {producto[1]} agregado a la venta.\033[0m")

        print("\n\033[1;33;44m---- LISTA DE PRODUCTOS ----\033[0m")
        listar_productos(productos)
        producto_id = int(input("\nIngrese ID del producto (0 para finalizar): "))

    if len(una_venta) == 0:
        print("\033[31mNo se registró ningún producto. Venta cancelada.\033[0m")
        return

    hoy = date.today()
    diccionario_venta = {
        "id": max((venta["id"] for venta in ventas), default=0) + 1,
        "cliente_id": cliente["id"],
        "cliente_nombre": cliente["nombre"],
        "fecha": (hoy.day, hoy.month, hoy.year),
        "items": una_venta,
        "total": sum(item["precio_final"] for item in una_venta),
    }

    ventas.append(diccionario_venta)
    print("\033[32m\nVenta registrada correctamente.\033[0m")
    print(f"Total de la venta: ${diccionario_venta['total']}")


# LEER
def listar_ventas():
    """
    Muestra el historial resumido de ventas y permite consultar los detalles de una venta especifica.
    """

    mostrar_ventas()

    venta_id = int(
        input("\nIngrese el ID de la venta para ver detalles o presione 0 para salir: ")
    )
    if venta_id == 0:
        return

    venta = buscar_venta_por_id(venta_id)
    if venta is None:
        print("\033[31mID de venta no encontrado.\033[0m")
        return

    mostrar_detalles_venta(venta)


# ACTUALIZAR
def actualizar_ventas():
    """
    Permite modificar la cantidad de productos de una venta o eliminarlos, reajustando el stock.
    """
    print("---- ACTUALIZAR VENTAS ----")
    mostrar_ventas()

    venta_id = int(input("\nIngrese el ID de la venta a actualizar: "))
    venta = buscar_venta_por_id(venta_id)

    if venta is None:
        print("\033[31mID de venta no encontrado.\033[0m")
        return

    mostrar_detalles_venta(venta)

    producto_id = int(input("\nIngrese el ID del producto a actualizar: "))
    # buscamos el item que coincida con el ID del producto
    item_encontrado = [
        item for item in venta["items"] if item["producto_id"] == producto_id
    ]

    if len(item_encontrado) == 0:
        print("\033[31mID de producto no encontrado.\033[0m")
        return

    # obtenemos el primer (y único) item que coincide con el producto_id
    item = item_encontrado[0]
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
    """
    Elimina una venta seleccionada por ID, previa confirmación del usuario,
    y reintegra al stock las unidades de todos sus productos.
    """

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
