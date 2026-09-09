from productos import productos, listar_productos
from clientes import clientes, listar_clientes

ventas = []


def menu_ventas(rol):
    opcion = ""
    while opcion != "5":
        print("\n=================================")
        print(f"\033[1;34m        GESTIÓN DE VENTAS ({rol.upper()})         \033[0m")
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
            if rol == "admin":
                reporte_ventas()
            else:
                print("\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden ver el reporte de ventas.\033[0m")
        elif opcion == "4":
            if rol == "admin":
                cancelar_venta()
            else:
                print("\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden cancelar ventas.\033[0m")
        elif opcion == "5":
            print("\033[1;34mRegresando al menu principal...\033[0m")
        else:
            print("\033[31mopcion invalida\033[0m")


def registrar_venta():
    print(" Registrar venta")
    listar_clientes()

    cliente_id = int(input("Ingrese ID del cliente: "))
    cliente = None
    for c in clientes:
        if c[0] == cliente_id:  # ID está en posición 0
            cliente = c
    if cliente == None:
        print("\033[31mCliente no encontrado.\033[0m")
        return

    listar_productos(productos)
    prod_id = int(input("Ingrese ID del producto: "))
    producto = None
    for p in productos:
        if p[0] == prod_id:
            producto = p
    if producto == None:
        print("\033[31mProducto no encontrado.\033[0m")
        return
    cantidad = int(input("Ingrese cantidad: "))
    if cantidad > producto[4]:
        print("\033[31mStock insuficiente.\033[0m")
        return
    producto[4] = producto[4] - cantidad  # actualizar stock
    precio = producto[3]
    descuento = producto[5]
    total = precio * cantidad
    total = total - (total * descuento)

    venta = [f"V{len(ventas) + 1}", cliente[1], producto[1], cantidad, total]
    ventas.append(venta)
    print("\033[32mVenta registrada. Cliente:", cliente[1], "- Total:\033[0m", total)
