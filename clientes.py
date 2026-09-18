"""
Módulo para la gestión de clientes.
Muestra las operaciones CRUD de los clientes,
aplicando restricciones segun el rol del usuario ingresado.
"""

# CLIENTES [id, nombre, tipo_cliente, telefono]
clientes = [
    [1, "Ana Gomez", "frecuente", "1122334455"],
    [2, "Luis Perez", "mayorista", "1199887766"],
    [3, "Anastasia Diaz", "frecuente", "1144556677"],
    [4, "Martin Lopez", "frecuente", "1133221100"],
    [5, "Sofia Ruiz", "mayorista", "1166778899"],
]


def menu_clientes(rol):
    opcion = ""
    while opcion != "5":
        print("=================================")
        print("\033[1;34m      GESTIÓN DE CLIENTES       \033[0m")
        print("=================================")

        print("1. Listar clientes")
        print("2. Registrar nuevo cliente ")
        print("3. Modificar datos de cliente ")
        print("4. Eliminar cliente ")
        print("5. Volver al menú principal")
        print("=================================")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            listar_clientes(rol)
        elif opcion == "2":
            crear_cliente()
        elif opcion == "3":
            actualizar_cliente(rol)
        elif opcion == "4":
            if rol == "admin":
                eliminar_cliente(rol)
            else:
                print(
                    "\n[ACCESO DENEGADO] Solo los administradores pueden eliminar clientes."
                )
        elif opcion == "5":
            print("Volviendo al menú principal...")
        else:
            print("\033[31mOpción no válida. Intente nuevamente.\033[0m")


# CRUD CLIENTES
def listar_clientes(rol):
    """
    Muestra la lista de clientes registrados.
    Si el usuario no es 'admin', oculta parcialmente el número de teléfono por privacidad.
    rol(str): El rol del usuario que realiza la consulta ('admin' o 'empleado').
    """
    print("\n---- LISTA DE CLIENTES ----")
    print(f"{'ID':<3} | {'NOMBRE Y APELLIDO':<18} | {'TIPO':<10} | {'TELÉFONO':<11}")
    print("-" * 55)
    if rol == "admin":
        clientes_a_mostrar = clientes
    else:
        clientes_a_mostrar = list(
            map(lambda c: [c[0], c[1], c[2], f"******{c[3][-4:]}"], clientes)
        )
    for cliente in clientes_a_mostrar:
        print(
            f"{cliente[0]:<3} | {cliente[1]:<18} | {cliente[2]:<10} | {cliente[3]:<11}"
        )


def mostrar_cliente(titulo, cliente):
    print(f"\n---- {titulo} ----")
    print(f"{'ID':<3} | {'NOMBRE Y APELLIDO':<18} | {'TIPO':<10} | {'TELÉFONO':<11}")
    print("-" * 55)

    print(f"{cliente[0]:<3} | {cliente[1]:<18} | {cliente[2]:<10} | {cliente[3]:<11}")


def mostrar_telefono_oculto(telefono):
    return "*" * (len(telefono) - 4) + telefono[-4:]


def validar_nombre():
    """Solicita y valida que el nombre y apellido ingresado tenga al menos 5 caracteres.
    """
    nombre = input("Ingrese su nombre y apellido: ").title()
    while len(nombre) < 5:
        print("ERROR. El nombre y apellido deben tener al menos 2 caracteres.")
        nombre = input("Ingrese su nombre y apellido: ").title()

    return nombre


tipos_permitidos = ("frecuente", "mayorista")


def validar_tipo_cliente():
    """
    Solicita y valida que el tipo de cliente se encuentre entre los tipos de cliente permitidos.
    """
    tipo_cliente = input("Ingrese el tipo de cliente: ").lower()
    while tipo_cliente not in tipos_permitidos:
        print(f"ERROR. Solo se permiten: {tipos_permitidos}")
        tipo_cliente = input("Ingrese el tipo de cliente: ").lower()
    return tipo_cliente


def validar_telefono():
    """
    Solicita y valida que el numero telefonico tenga una longitud minima de 10 digitos.
    """
    telefono = input("Ingrese el número de teléfono: ")
    while len(telefono) < 10:
        print("\033[31mERROR. El teléfono debe tener 10 números.\033[0m")
        telefono = input("Ingrese el número de teléfono: ")
    return telefono


def crear_cliente():
    """
    Registra un nuevo cliente solicitando y validando sus datos personales.
    """
    print("\n\033[1;33;44m---- CREAR NUEVO CLIENTE ----\033[0m")
    if len(clientes) > 0:
        ultimo_id = max(fila[0] for fila in clientes)
        nuevo_id = ultimo_id + 1
    else:
        nuevo_id = 1
    nombre = validar_nombre()
    tipo_cliente = validar_tipo_cliente()
    telefono = validar_telefono()

    nuevo_cliente = [nuevo_id, nombre, tipo_cliente, telefono]
    clientes.append(nuevo_cliente)
    print("\033[32m¡Cliente creado con éxito!\033[0m")


def actualizar_cliente(rol):
    """
    Permite modificar los datos (nombre, tipo o teléfono) de un cliente existente.
    rol (str): El rol del usuario autenticado.
    Solo administradores pueden modificar el telefono, por privacidad.
    """
    print("\n\033[1;33;44m---- ACTUALIZAR DATOS DE UN CLIENTE ----\033[0m")
    listar_clientes(rol)
    id_buscar = int(input("\nIngresa el ID del cliente que quieres modificar: "))
    encontrado = False
    for cliente in clientes:
        if cliente[0] == id_buscar:
            encontrado = True
            opcion = 0
            while opcion != 4:
                mostrar_cliente("ESTAS ACTUALIZANDO A", cliente)
                print("\n1. Actualizar nombre y apellido")
                print("2. Actualizar tipo de cliente")
                print("3. Actualizar número de teléfono")
                print("4. Salir")

                opcion = int(input("Elige una opción: "))
                if opcion == 1:
                    nuevo_nombre = validar_nombre()
                    cliente[1] = nuevo_nombre
                    print("\033[32mNombre y apellido actualizado correctamente.\033[0m")
                elif opcion == 2:
                    nuevo_tipo_cliente = validar_tipo_cliente()
                    cliente[2] = nuevo_tipo_cliente
                    print("\033[32mTipo de cliente actualizado correctamente.\033[0m")
                elif opcion == 3:
                    if rol == "admin":
                        nuevo_telefono = validar_telefono()
                        cliente[3] = nuevo_telefono
                        print(
                            "\033[32mNúmero de teléfono actualizado correctamente.\033[0m"
                        )
                    else:
                        print(
                            "\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden modificar el teléfono.\033[0m"
                        )
                elif opcion == 4:
                    print("Volviendo al gestión de clientes...")
                else:
                    print("\033[31mError. Opción invalida. Intenta de nuevo.\033[0m")
    if encontrado != True:
        print("\033[31mEl ID no existe.\033[0m")


def eliminar_cliente(rol):
    print("\n\033[1;33;44m---- ELIMINAR UN CLIENTE ----\033[0m")
    listar_clientes(rol)
    id_buscar = int(input("\nIngresa el ID del cliente que quieres eliminar: "))
    encontrado = False
    for cliente in clientes:
        if cliente[0] == id_buscar:
            encontrado = True
            mostrar_cliente("ESTAS POR ELIMINAR A", cliente)
            opcion = input("¿Estas seguro? (si/no): ").lower()
            if opcion == "si":
                clientes.remove(cliente)
                print("\033[32m¡Cliente eliminado con éxito!\033[0m")
            else:
                print("\033[31mOperación cancelada.\033[0m")
    if encontrado != True:
        print("\033[31mEl ID no existe.\033[0m")
