productos = [
    [1, "Pan lactal", "alimentos", 1200.0, 50, 0.0],
    [2, "Detergente", "limpieza", 2500.0, 30, 0.10],
    [3, "Gaseosa Cola 2L", "bebidas", 1800.0, 45, 0.05],
    [4, "Chocolate ", "golosinas", 950.0, 100, 0.0],
    [5, "Shampoo", "Higiene", 3000.0, 20, 0.15],
    [6, "Medialunas", "panadería", 3500.0, 15, 0.0],
    [7, "Jamon Cocido", "fiambrería", 1500.0, 40, 0.05],
    [8, "Papas fritas", "snacks", 2800.0, 25, 0.10],
    [9, "Jabon", "higiene", 650.0, 60, 0.0],
    [10, "Queso Cremoso", "lácteos", 4200.0, 18, 0.15],
]


# CREATE PRODUCTO
def crear_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    if len(productos) > 0:
        ultimo_id = max(fila[0] for fila in productos)
        nuevo_id = ultimo_id + 1
    else:
        nuevo_id = 1

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))
    descuento = float(input("Descuento : "))

    nueva_fila = [nuevo_id, nombre, categoria, precio, stock, descuento]
    productos.append(nueva_fila)
    print(f"\n¡Producto agregado con éxito! Se le asignó el ID: {nuevo_id}")


# READ PRODUCTOS
def listar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    if len(productos) == 0:
        print("No hay productos en la lista.")
    else:
        print(
            f"{'ID':<4} | {'NOMBRE':<15} | {'CATEGORÍA':<12} | {'PRECIO':<10} | {'STOCK':<6} | {'DESC (%)':<8}"
        )
        print("-" * 70)
        for fila in productos:
            desc_porcentaje = fila[5] * 100
            print(
                f"{fila[0]:<4} | {fila[1]:<15} | {fila[2]:<12} | ${fila[3]:<9.2f} | {fila[4]:<6} | {desc_porcentaje:<8.1f}%"
            )
        print("-" * 70)


# UPDATE PRODUCTO
def actualizar_stock():
    listar_productos()
    id_buscar = int(input("\nIngresa el ID del producto para cambiar su stock: "))
    encontrado = False
    for fila in productos:
        if fila[0] == id_buscar:
            nuevo_stock = int(
                input(f"El stock actual de {fila[1]} es {fila[4]}. Nuevo stock: ")
            )
            fila[4] = nuevo_stock
            print("¡Stock actualizado!")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")
        menu_productos()


# DELETE PRODUCTO
def eliminar_producto():
    listar_productos()
    id_buscar = int(input("\nIngresa el ID del producto a eliminar: "))
    encontrado = False
    for i in range(len(productos)):
        if productos[i][0] == id_buscar:
            productos.pop(i)
            print("¡Producto eliminado!")
            encontrado = True
            menu_productos()
    if not encontrado:
        print("Producto no encontrado.")


# MENÚ PRODUCTOS ---
def menu_productos():
    opcion = ""
    while opcion != "5":
        print("\n=================================")
        print("      GESTIÓN DE PRODUCTOS       ")
        print("=================================")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Salir al menú principal")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            crear_producto()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            listar_productos()
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            actualizar_stock()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            eliminar_producto()
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
            print("\nRegresando al menú principal...")
        else:
            print("\nOpción no válida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")
