from productos import productos
from clientes import clientes, listar_clientes

ventas = []


def menu_ventas():
    opcion = ""
    while opcion != "5":
        print("\n=================================")
        print("        GESTIÓN DE VENTAS         ")
        print("=================================")
        print("1. Registrar ventas ")
        print("2. Consultar ventas")
        print("3. Reporte de ventas")
        print("4. Cancelar venta")
        print("5. Volver al menu principal")
        opcion = input("Elija una opcion:")
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            consultar_ventas()
        elif opcion == "3":
            reporte_ventas()
        elif opcion == "4":
            cancelar_venta()
        elif opcion == "5":
            print("Regresando al menu principal...L")
        else:
            print("opcion invalida")


def registrar_venta():
    print(" Registrar venta")
    listar_clientes()

    cliente_id = int(input("Ingrese ID del cliente: "))
    cliente = None
    for c in clientes:
        if c[0] == cliente_id:  # ID está en posición 0
            cliente = c
    if cliente == None:
        print("Cliente no encontrado.")
        return
    prod_id = int(input("Ingrese ID del producto: "))
    producto = None
    for p in productos:
        if p[0] == prod_id:
            producto = p
    if producto == None:
        print("Producto no encontrado.")
        return
    cantidad = int(input("Ingrese cantidad: "))
    if cantidad > producto[4]:
        print("Stock insuficiente.")
        return
    producto[4] = producto[4] - cantidad  # actualizar stock
    precio = producto[3]
    descuento = producto[5]
    total = precio * cantidad
    total = total - (total * descuento)

    venta = [f"V{len(ventas) + 1}", cliente[1], producto[1], cantidad, total]
    ventas.append(venta)
    print("Venta registrada. Cliente:", cliente[1], "- Total:", total)
