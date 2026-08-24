usuarios = ["admin"]
contrasenas = ["1234"]

def registrar_usuario():
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
    nuevo_usuario = input("Ingresa un nuevo usuario: ")
    if nuevo_usuario in usuarios:
        print("El usuario ingresado ya existe.")
    else:
        nueva_contrasena = input("Ingresa una contraseña: ")
        usuarios.append(nuevo_usuario)
        contrasenas.append(nueva_contrasena)
        print("¡Usuario registrado con éxito!")
    menu ()

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario_ingresado = input("Usuario: ")
    contrasena_ingresada = input("Contraseña: ")
    if usuario_ingresado in usuarios:
        posicion = usuarios.index(usuario_ingresado)
        if contrasenas[posicion] == contrasena_ingresada:
            print("¡Bienvenido, ", usuario_ingresado, "!")
            menu_principal ()
        else:
            print("Contraseña incorrecta.")
            menu ()
    else:
        print("El usuario no existe.")
        menu ()


def menu():
    print("\n=== Bienvenido al sistema del supermecado ===")
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    print("3. Salir")
    opcion = input("Elige una opción (1, 2 o 3): ")
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        print("\n¡Hasta luego!")
    else:
        print("Opción no válida. Intenta de nuevo.")
        menu()

def menu_principal():
        print("\n==============================")
        print("   SISTEMA DE GESTIÓN DEL SUPERMERCADO   ")
        print("==============================")
        print("1. Módulo de Productos")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": menu_productos()
        elif opcion == "2": menu_clientes()
        elif opcion == "3": menu_ventas()
        elif opcion == "4": print("\n¡Gracias por usar el sistema!")
        else: print("Opción no válida.")
    
menu()