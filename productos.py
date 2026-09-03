productos = [
    [1, "Pan lactal", "almacen", 1200.0, 50, 0.0],
    [2, "Detergente", "limpieza", 2500.0, 30, 0.10],
    [3, "Gaseosa Cola 2L", "bebidas", 1800.0, 45, 0.05],
    [4, "Chocolate ", "golosinas", 950.0, 100, 0.0],
    [5, "Shampoo", "Higiene", 3000.0, 7, 0.15],
    [6, "Arroz", "almacen", 1500.0, 8, 0.0],
    [7, "Galletitas ", "almacen", 1500.0, 5, 0.05],
    [8, "Papas fritas ", "snacks", 2800.0, 25, 0.10],
    [9, "Jabon ", "higiene", 1200.0, 60, 0.0],
    [10, "Aceite ", "almacen", 400.0, 18, 0.15],
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
    while precio <= 0:
        precio = float(input("Error, el precio no puede ser nulo o negativo, ingrese el precio: "))
    stock = int(input("Stock inicial: "))
    while stock <= 0:
        stock = int(input("Error, el stock no puede ser nulo o negativo, ingrese el stock: "))
    descuento = float(input("Descuento : "))
    while descuento < 0:
        descuento = float(input("Error, el descuento no puede ser negativo, ingrese el descuento: "))

    nueva_fila = [nuevo_id, nombre, categoria, precio, stock, descuento]
    productos.append(nueva_fila)
    print(f"\n¡Producto agregado con éxito! Se le asignó el ID: {nuevo_id}")

# READ PRODUCTOS
def listar_productos(lista):
    if len(lista) == 0:
        print("No hay productos en la lista.")
    else:
        print(
            f"{'ID':<4} | {'NOMBRE':<22} | {'CATEGORÍA':<12} | {'PRECIO':<10} | {'STOCK':<6} | {'DESC (%)':<8}"
        )
        print("-" * 70)
        for fila in lista:
            desc_porcentaje = fila[5] * 100
            print(
                f"{fila[0]:<4} | {fila[1]:<22} | {fila[2]:<12} | ${fila[3]:<9.2f} | {fila[4]:<6} | {desc_porcentaje:<8.1f}%"
            )
        print("-" * 70)

# UPDATE PRODUCTO
def actualizar_stock():
    print("1. Para ver productos con bajo stock")
    print("2. Para actualizar stock")
    opcion = input("Elige una opción (1-2): ")
    if opcion == "1":
        mostrar_productos_poco_stock()
    elif opcion == "2":
        listar_productos()
        id_buscar = int(input("\nIngresa el ID del producto para cambiar su stock: "))
        encontrado = False
        for fila in productos:
            if fila[0] == id_buscar:
                nuevo_stock = int(input(f"El stock actual de {fila[1]} es {fila[4]}. Nuevo stock: "))
                fila[4] = nuevo_stock
                print("¡Stock actualizado!")
                encontrado = True
        if encontrado == False:
            print("Producto no encontrado.")

# DELETE PRODUCTO
def eliminar_producto():
    listar_productos(productos)
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

def mostrar_productos_poco_stock():
    print("\n--- PRODUCTOS CON POCO STOCK (Menos de 10) ---")
    productos_criticos = list(filter(lambda x: x[4] < 10, productos))
    if len(productos_criticos) == 0:
        print("Todos los productos tienen stock suficiente.")
    else:
        for p in productos_criticos:
            print(f"ID: {p[0]} | Producto: {p[1]} | Stock actual: {p[4]}")

#ORDENAR
def ordenar_categoria_prod():
    prod_ordenados = sorted(productos, key=lambda p: p[2].lower())
    print("\n--- PRODUCTOS ORDENADOS POR CATEGORÍA ---")
    listar_productos(prod_ordenados)

def ordenar_precio_prod():
    prod_ordenados = sorted(productos, key=lambda p: p[3])
    print("\n--- PRODUCTOS ORDENADOS POR PRECIO ---")
    listar_productos(prod_ordenados) 

def menu_reportes():
    opcion = ""
    while opcion != "3":
        print("\n==================================")
        print("      REPORTES Y ORDENAMIENTO     ")
        print("==================================")
        print("1. Ordenar por categoría")
        print("2. Ordenar por precio (menor a mayor)")
        print("3. Volver al menú de productos")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            ordenar_categoria_prod()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            # Podés crear también esta función si la querés implementar
            ordenar_precio_prod() 
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            print("\nRegresando...")
        else:
            print("\nOpción no válida. Intenta de nuevo.")

# MENÚ PRODUCTOS
def menu_productos():
    opcion = ""
    while opcion != "6":
        print("\n==================================")
        print("       GESTIÓN DE PRODUCTOS       ")
        print("==================================")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Reportes y ordenamiento")
        print("6. Salir al menú principal")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            crear_producto()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            listar_productos(productos) 
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            actualizar_stock()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            eliminar_producto()
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
            menu_reportes() 
        elif opcion == "6":
            print("\nRegresando al menú principal...")
        else:
            print("\nOpción no válida. Intenta de nuevo.")
