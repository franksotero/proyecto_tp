# CLIENTES [id, nombre, tipo_cliente, telefono]
clientes = [
    [0, "Ana Gomez", "frecuente", "1122334455"],
    [1, "Luis Perez", "mayorista", "1199887766"],
    [2, "Anastasia Diaz", "frecuente", "1144556677"],
    [3, "Martin Lopez", "ocasional", "1133221100"],
    [4, "Sofia Ruiz", "mayorista", "1166778899"],
]


def menu_clientes():
    opcion = ""
    while opcion != "5":
        print("\n=================================")
        print("       GESTIÓN DE CLIENTES       ")
        print("=================================")
        print("1. Listar clientes")
        print("2. Registrar nuevo cliente ")
        print("3. Modificar datos de cliente ")
        print("4. Eliminar cliente ")
        print("5. Volver al menú principal")
        print("=================================")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            crear_cliente()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente nuevamente.")


# CRUD CLIENTES
def listar_clientes():
    print("\n---- LISTA DE CLIENTES ----")
    print(f"{'ID':<3} | {'NOMBRE Y APELLIDO':<18} | {'TIPO':<10} | {'TELÉFONO':<11}")
    print("-" * 55)
    for cliente in clientes:
        print(
            f"{cliente[0]:<3} | {cliente[1]:<18} | {cliente[2]:<10} | {cliente[3]:<11}"
        )


def mostrar_cliente(cliente):
    print("\n---- ESTAS MODIFICANDO AL CLIENTE ----")
    print(f"{'ID':<3} | {'NOMBRE Y APELLIDO':<18} | {'TIPO':<10} | {'TELÉFONO':<11}")
    print("-" * 55)

    print(f"{cliente[0]:<3} | {cliente[1]:<18} | {cliente[2]:<10} | {cliente[3]:<11}")


def validar_nombre():
    nombre = input("Ingrese su nombre y apellido: ").title()
    while len(nombre) < 5:
        print("ERROR. El nombre y apellido deben tener al menos 2 caracteres.")
        nombre = input("Ingrese su nombre y apellido: ").title()

    return nombre


def validar_tipo_cliente():
    tipo_cliente = input("Ingrese el tipo de cliente: ").lower()
    while tipo_cliente != "frecuente" and tipo_cliente != "mayorista":
        print("ERROR. Solo existen dos tipos de clientes: frecuente o mayorista.")
        tipo_cliente = input("Ingrese el tipo de cliente: ").lower()

    return tipo_cliente


def validar_telefono():
    telefono = input("Ingrese el número de teléfono: ")
    while len(telefono) < 10:
        print("ERROR. El teléfono debe tener 10 números.")
        telefono = input("Ingrese el número de teléfono: ")

    return telefono


def crear_cliente():
    print("\n---- CREAR NUEVO CLIENTE ----")
    id = len(clientes)
    nombre = validar_nombre()
    tipo_cliente = validar_tipo_cliente()
    telefono = validar_telefono()

    nuevo_cliente = [id, nombre, tipo_cliente, telefono]
    clientes.append(nuevo_cliente)
    print("¡Cliente creado con éxito!")


def actualizar_cliente():
    print("\n---- ACTUALIZAR DATOS DE UN CLIENTE ----")
    listar_clientes()

    id_buscar = int(input("\nIngresa el ID del cliente que quieres modificar: "))

    encontrado = False

    for cliente in clientes:
        if cliente[0] == id_buscar:
            encontrado = True
            opcion = 0
            while opcion != 4:
                mostrar_cliente(cliente)
                print("\n1. Actualizar nombre y apellido")
                print("2. Actualizar tipo de cliente")
                print("3. Actualizar número de teléfono")
                print("4. Salir")

                opcion = int(input("Elige una opción: "))
                if opcion == 1:
                    nuevo_nombre = validar_nombre()
                    cliente[1] = nuevo_nombre
                    print("Nombre y apellido actualizado correctamente.")
                elif opcion == 2:
                    nuevo_tipo_cliente = validar_tipo_cliente()
                    cliente[2] = nuevo_tipo_cliente
                    print("Tipo de cliente actualizado correctamente.")
                elif opcion == 3:
                    nuevo_telefono = validar_telefono()
                    cliente[3] = nuevo_telefono
                    print("Número de teléfono actualizado correctamente.")
                elif opcion == 4:
                    print("Volviendo al gestión de clientes...")
                else:
                    print("Error. Opción invalida. Intenta de nuevo.")
            break

    if encontrado != True:
        print("El ID no existe.")


def eliminar_cliente():
    print("---- ELIMINAR UN CLIENTE ----")
