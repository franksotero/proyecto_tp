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


def crear_cliente():
    print("---- CREAR NUEVO CLIENTE ----")
    id = len(clientes)

    nombre = input("Ingrese su nombre y apellido: ").title()
    while len(nombre) < 5:
        print("ERROR. El nombre y apellido deben tener al menos 2 caracteres.")
        nombre = input("Ingrese su nombre y apellido: ").title()

    tipo_cliente = input("Ingrese el tipo de cliente: ").lower()
    while tipo_cliente != "frecuente" and tipo_cliente != "mayorista":
        print("ERROR. Solo existen dos tipos de clientes: frecuente o mayorista.")
        tipo_cliente = input("Ingrese el tipo de cliente: ").lower()

    telefono = input("Ingrese el número de teléfono: ")
    while len(telefono) < 10:
        print("ERROR. El teléfono debe tener 10 números.")
        telefono = input("Ingrese el número de teléfono: ")

    nuevo_cliente = [id, nombre, tipo_cliente, telefono]
    clientes.append(nuevo_cliente)
    print("¡Cliente creado con éxito!")
