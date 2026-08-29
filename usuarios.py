usuarios = ["admin"]
contrasenas = ["1234"]


def registrar_usuario():
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
    nuevo_usuario = input("Ingresa un nuevo usuario: ")
    nueva_contrasena = input("Ingresa una contraseña: ")
    if nuevo_usuario in usuarios:
        print("El usuario ingresado ya existe.")
    else:
        usuarios.append(nuevo_usuario)
        contrasenas.append(nueva_contrasena)
        print("¡Usuario registrado con éxito!")


def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario_ingresado = input("Usuario: ")
    contrasena_ingresada = input("Contraseña: ")
    if usuario_ingresado in usuarios:
        posicion = usuarios.index(usuario_ingresado)
        if contrasenas[posicion] == contrasena_ingresada:
            print(f"¡Bienvenido, {usuario_ingresado}!")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    else:
        print("El usuario no existe.")
        return False

