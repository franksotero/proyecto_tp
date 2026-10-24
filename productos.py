"""
Módulo para la gestión del inventario de productos.
Muestra las operaciones CRUD para los productos, control de stock,
validación de categorías y ordenamiento de datos mediante un archivo de texto
"""
NOMBRE_ARCHIVO = "productos.txt"

def cargar_productos_desde_archivo(ruta):
    """
    Lee un archivo de texto con codificación UTF-8 usando try-except y la sentencia with.
    Procesa cada línea separada por comas y retorna la lista de productos en memoria.
    """
    lista_productos = []

    try:
        with open(ruta, "r", encoding="utf-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if linea:
                    campos = linea.split(",")
                    id_prod = int(campos[0])
                    nombre = campos[1]
                    categoria = campos[2]
                    precio = float(campos[3])
                    stock = int(campos[4])
                    descuento = float(campos[5])
                    lista_productos.append([id_prod, nombre, categoria, precio, stock, descuento])
    except FileNotFoundError:
        # Si el archivo aún no fue creado, inicializa una lista vacía
        print(f"Aviso: El archivo '{ruta}' no existe todavía. Se creara un nuevo archivo.")
    except OSError as err:
        print(f"Error al intentar leer el archivo '{ruta}': {err}")
    return lista_productos

def guardar_productos_en_archivo(ruta, lista_productos):
    """
    Escribe la matriz de productos en el archivo de texto en formato delimitado por comas.
    Usa la sentencia with para garantizar el cierre adecuado del recurso.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as arch:
            for p in lista_productos:
                linea = f"{p[0]},{p[1]},{p[2]},{p[3]},{p[4]},{p[5]}\n"
                arch.write(linea)
    except OSError as err:
        print(f"Error al intentar escribir en el archivo '{ruta}': {err}")

# Carga inicial del archivo de texto
productos = cargar_productos_desde_archivo(NOMBRE_ARCHIVO)

# PRODUCTOS: ID, NOMBRE, CATEGORIA, PRECIO, STOCK, DESCUENTO

# CREATE PRODUCTO
def crear_producto():
    """Registra un nuevo producto en el catalogo.
    Solicita y valida el nombre, categoria, precio, stock y descuento,
    generando un ID de forma automatica, segun la cantidad previa de productos.
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
    guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
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

def actualizar_producto(rol):
    """
    Permite modificar los datos de un producto (nombre, categoria, precio, stock o descuento).
    Solo administradores pueden realizar modificaciones.
    """
    if rol != "admin":
        print("\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden editar productos.\033[0m")
    else:
        listar_productos(productos)
        try:
            id_buscar = int(input("\nIngresa el ID del producto a modificar: "))
        except ValueError:
            print("\033[31mError. El ID debe ser un numero entero.\033[0m")
            return

        producto = None
        i = 0
        while i < len(productos) and producto is None:
            if productos[i][0] == id_buscar:
                producto = productos[i]
            i += 1

        if producto is None:
            print("\033[31mProducto no encontrado.\033[0m")
        else:
            opcion = ""
            while opcion != "6":
                print(f"\n---- MODIFICANDO: {producto[1]} (ID: {producto[0]}) ----")
                print("1. Modificar nombre")
                print("2. Modificar categoria")
                print("3. Modificar precio")
                print("4. Modificar stock")
                print("5. Modificar descuento")
                print("6. Volver al menu de productos")

                opcion = input("Elige una opción (1-6): ")

                if opcion == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
                    if len(nuevo_nombre) > 0:
                        producto[1] = nuevo_nombre
                        guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
                        print("\033[32m¡Nombre actualizado con exito!\033[0m")
                    else:
                        print("\033[31mEl nombre no puede estar vacío.\033[0m")

                elif opcion == "2":
                    nueva_categoria = validar_categoria()
                    producto[2] = nueva_categoria
                    guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
                    print("\033[32m¡Categoria actualizada con exito!\033[0m")

                elif opcion == "3":
                    try:
                        nuevo_precio = float(input("Ingrese el nuevo precio: "))
                        while nuevo_precio <= 0:
                            nuevo_precio = float(input("\033[37;41mEl precio debe ser mayor a 0: \033[0m"))
                        producto[3] = nuevo_precio
                        guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
                        print("\033[32m¡Precio actualizado con éxito!\033[0m")
                    except ValueError:
                        print("\033[31mError. Debe ingresar un valor numerico valido.\033[0m")

                elif opcion == "4":
                    try:
                        nuevo_stock = int(input(f"Stock actual de {producto[1]}: {producto[4]}. Nuevo stock: "))
                        while nuevo_stock < 0:
                            nuevo_stock = int(input("\033[37;41mEl stock no puede ser negativo, ingrese el nuevo stock: \033[0m"))
                        producto[4] = nuevo_stock
                        guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
                        print("\033[32m¡Stock actualizado con exito!\033[0m")
                    except ValueError:
                        print("\033[31mError. Debe ingresar un numero entero valido.\033[0m")

                elif opcion == "5":
                    try:
                        nuevo_desc = float(input("Ingrese el nuevo descuento (ej: 0.10 para 10%): "))
                        while nuevo_desc < 0 or nuevo_desc > 1:
                            nuevo_desc = float(input("\033[37;41mEl descuento debe estar entre 0 y 1: \033[0m"))
                        producto[5] = nuevo_desc
                        guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
                        print("\033[32m¡Descuento actualizado con exito!\033[0m")
                    except ValueError:
                        print("\033[31mError. Debe ingresar un numero valido.\033[0m")

                elif opcion == "6":
                    print("Regresando al menu de productos...")
                else:
                    print("\033[31mOpcion no valida. Intente de nuevo.\033[0m")

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
            guardar_productos_en_archivo(NOMBRE_ARCHIVO, productos)
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

def calcular_stock_total_recursivo(lista, i=0):
    """
    Suma de forma recursiva el stock disponible de todos los productosdel supermercado
    -Caso base: cuando el indice "i" llega al final de la lista (retorna 0).
    -Caso recursivo: suma el stock del producto actual + llamada recursiva con i + 1.
    -Reduccion del dominio: incrementa "i" en 1 en cada llamada.
    """
    if i == len(lista):
        return 0
    else:
        return lista[i][4] + calcular_stock_total_recursivo(lista, i + 1)


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
    while opcion != "5":
        print("\n==================================")
        print("\033[1;34m      REPORTES Y ORDENAMIENTO     \033[0m")
        print("==================================")
        print("1. Ordenar por categoría")
        print("2. Ordenar por precio (menor a mayor)")
        print("3. Ver categorías únicas")
        print("4. Ver unidades totales en stock")
        print("5. Volver al menú de productos")

        opcion = input("Elige una opción (1-5): ")

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
            total_unidades = calcular_stock_total_recursivo(productos)
            print(f"\n\033[32mEl stock total sumado de la tienda es: {total_unidades} unidades.\033[0m")
            input("\nPresiona Enter para continuar...")
        elif opcion == "5":
            print("\nRegresando...")
        else:
            print("\n\033[31mOpción no válida. Intenta de nuevo.\033[0m")


# MENÚ PRODUCTOS
def menu_productos(rol):
    opcion = ""
    while opcion != "7":
        print("\n==================================")
        print("\033[1;34m       GESTIÓN DE PRODUCTOS       \033[0m")
        print("==================================")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Ver productos con bajo stock")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Reportes y ordenamiento")
        print("7. Salir al menu principal")

        opcion = input("Elige una opcion (1-7): ")
        if opcion == "1":
            if rol == "admin":
                crear_producto()
            else:
                print(
                    "\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden agregar un producto.\033[0m"
                )
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            listar_productos(productos)
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            mostrar_productos_poco_stock()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            actualizar_producto(rol)
        elif opcion == "5":
            if rol == "admin":
                eliminar_producto(rol)
            else:
                print("\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden eliminar un producto.\033[0m")
            input("\nPresiona Enter para continuar...")
        elif opcion == "6":
            menu_reportes()
        elif opcion == "7":
            print("\nRegresando al menú principal...")
        else:
            print("\n\033[31mOpción no válida. Intenta de nuevo.\033[0m")