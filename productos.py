"""
Módulo para la gestion del inventario de productos.
Muestra las operaciones CRUD para los productos, control de stock,
validación de categorías y ordenamiento de datos.
"""

# PRODUCTOS: ID, NOMBRE, CATEGORIA, PRECIO, STOCK, DESCUENTO
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
    """Registra un nuevo producto en el catalogo.
    Solicita y valida el nombre, categoria, precio, stock y descuento,
    generando un ID de forma automática, segun la cantidad previa de productos.
    """
    print("\n\033[4;35m--- AGREGAR PRODUCTO ---\033[0m")
    if len(productos) > 0:
        ultimo_id = max(map(lambda fila: fila[0], productos))
        nuevo_id = ultimo_id + 1
    else:
        nuevo_id = 1

    nombre = input("Nombre: ")
    categoria = validar_categoria()
    precio = float(input("Precio: "))
    while precio <= 0:
        precio = float(input("\033[37;41mError, el precio no puede ser nulo o negativo, ingrese el precio: \033[0m"))
    stock = int(input("Stock inicial: "))
    while stock <= 0:
        stock = int(input("\033[37;41mError, el stock no puede ser nulo o negativo, ingrese el stock: \033[0m"))
    descuento = float(input("Descuento : "))
    while descuento < 0:
        descuento = float(input("\033[37;41mError, el descuento no puede ser negativo, ingrese el descuento: \033[0m"))

    nueva_fila = [nuevo_id, nombre, categoria, precio, stock, descuento]
    productos.append(nueva_fila)
    print(f"\n\033[32m¡Producto agregado con éxito! Se le asignó el ID: {nuevo_id}\033[0m")


def obtener_categorias_unicas():
    categorias = set(p[2].lower() for p in productos)
    print("Categorías disponibles en el sistema:", list(categorias))
    return categorias


def validar_categoria():
    """
    Solicita y valida que la categoría ingresada exista en el sistema.
    """
    categorias_existentes = set(p[2].lower().strip() for p in productos)
    print("\nCategorías disponibles:", ", ".join(categorias_existentes))
    categoria = input("Ingrese la categoría: ").lower().strip()
    while categoria not in categorias_existentes:
        print("\033[31mError. La categoría no existe. Ingrese una de las categorías listadas.\033[0m")
        categoria = input("Ingrese una categoría válida: ").lower().strip()
    return categoria


# READ PRODUCTOS
def listar_productos(lista):
    """
    Imprime en formato de tabla la lista de productos.
    En caso de no haber ningun producto, no muestra nada
    """
    if len(lista) == 0:
        print("No hay productos en la lista.")
    else:
        print(f"{'ID':<4} | {'NOMBRE':<22} | {'CATEGORÍA':<12} | {'PRECIO':<10} | {'STOCK':<6} | {'DESC (%)':<8}")
        print("-" * 70)
        for fila in lista:
            desc_porcentaje = fila[5] * 100
            print(f"{fila[0]:<4} | {fila[1]:<22} | {fila[2]:<12} | ${fila[3]:<9.2f} | {fila[4]:<6} | {desc_porcentaje:<8.1f}%")
        print("-" * 70)


# UPDATE PRODUCTO
def actualizar_stock():
    """
    Permite consultar productos con bajo stock y modificar las existencias de un producto.
    """
    print("1. Para ver productos con bajo stock")
    print("2. Para actualizar stock")
    opcion = input("Elige una opción (1-2): ")
    if opcion == "1":
        mostrar_productos_poco_stock()
    elif opcion == "2":
        listar_productos(productos)
        id_buscar = int(input("\nIngresa el ID del producto para cambiar su stock: "))
        encontrado = False
        for fila in productos:
            if fila[0] == id_buscar:
                nuevo_stock = int(input(f"El stock actual de {fila[1]} es {fila[4]}. Nuevo stock: "))
                fila[4] = nuevo_stock
                print("\033[32m¡Stock actualizado!\033[0m")
                encontrado = True
        if encontrado == False:
            print("\033[31mProducto no encontrado.\033[0m")


# DELETE PRODUCTO
def eliminar_producto(rol):
    """
    Elimina un producto del inventario mediante su ID.
    rol(str): El rol del usuario autenticado, ya que solo un rol admin pueden hacerlo
    """
    listar_productos(productos)
    id_buscar = int(input("\nIngresa el ID del producto a eliminar: "))
    encontrado = False
    i = 0
    while i < len(productos) and not encontrado:
        if productos[i][0] == id_buscar:
            productos.pop(i)
            print("\033[32m¡Producto eliminado!\033[0m")
            encontrado = True
        i += 1
    if not encontrado:
        print("\033[31mProducto no encontrado.\033[0m")


def mostrar_productos_poco_stock():
    """
    Filtra y muestra en pantalla los productos cuyo stock es inferior a 10 unidades.
    """
    print("\n\033[4;35m--- PRODUCTOS CON POCO STOCK (Menos de 10) ---\033[0m")
    productos_criticos = list(filter(lambda x: x[4] < 10, productos))
    if len(productos_criticos) == 0:
        print("\033[32mTodos los productos tienen stock suficiente.\033[0m")
    else:
        for p in productos_criticos:
            print(f"ID: {p[0]} | Producto: {p[1]} | Stock actual: {p[4]}")


# ORDENAR
def ordenar_categoria_prod():
    """
    Ordena el catalogo de productos por categoria en orden alfabetico y lo muestra por pantalla.
    """
    prod_ordenados = sorted(productos, key=lambda p: p[2].lower())
    print("\n\033[4;35m--- PRODUCTOS ORDENADOS POR CATEGORÍA ---\033[0m")
    listar_productos(prod_ordenados)


def ordenar_precio_prod():
    """
    Ordena el catalogo de productos por precio de menor a mayor y lo muestra por pantalla.
    """
    prod_ordenados = sorted(productos, key=lambda p: p[3])
    print("\n--- PRODUCTOS ORDENADOS POR PRECIO ---")
    listar_productos(prod_ordenados)


def menu_reportes():
    opcion = ""
    while opcion != "4":
        print("\n==================================")
        print("\033[1;34m      REPORTES Y ORDENAMIENTO     \033[0m")
        print("==================================")
        print("1. Ordenar por categoría")
        print("2. Ordenar por precio (menor a mayor)")
        print("3. Ver categorías únicas")
        print("4. Volver al menú de productos")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            ordenar_categoria_prod()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            ordenar_precio_prod()
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            obtener_categorias_unicas()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            print("\nRegresando...")
        else:
            print("\n\033[31mOpción no válida. Intenta de nuevo.\033[31m")


# MENÚ PRODUCTOS
def menu_productos(rol):
    opcion = ""
    while opcion != "6":
        print("\n==================================")
        print("\033[1;34m       GESTIÓN DE PRODUCTOS       \033[0m")
        print("==================================")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Reportes y ordenamiento")
        print("6. Salir al menú principal")

        opcion = input("Elige una opción (1-6): ")
        if opcion == "1":
            if rol == "admin":
                crear_producto()
            else:
                print(
                    "\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden agregar un producto.\033[m"
                )
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            listar_productos(productos)
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            actualizar_stock()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            if rol == "admin":
                eliminar_producto(rol)
            else:
                print(
                    "\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden eliminar un producto.\033[0m"
                )
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
            menu_reportes()
        elif opcion == "6":
            print("\nRegresando al menú principal...")
        else:
            print("\n\033[31mOpción no válida. Intenta de nuevo.\033[/m")
