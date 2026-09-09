#nombre de usuario, contraseña, rol
usuarios = [
    ["admin", "1234", "admin"]
]


def generar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    usuario = (nombre[:2] + apellido).lower()
    return usuario

def registrar_usuario():
    print("\n\033[4;35m--- REGISTRO DE NUEVO USUARIO ---\033[0m")
    nuevo_usuario = generar_usuario()
    print(f"Su nombre de usuario asignado es: {nuevo_usuario}")
    for u in usuarios:
        if u[0] == nuevo_usuario:
            print("\033[31mEl usuario ingresado ya existe.\033[0m")
            return
    nueva_contrasena = input("Ingresa una contraseña: ")
    usuarios.append([nuevo_usuario, nueva_contrasena, "empleado"])
    print("\033[32m¡Usuario registrado con éxito como Empleado!\033[0m")

def iniciar_sesion():
    print("\n\033[4;35m--- INICIO DE SESIÓN ---\033[0m")
    usuario_ingresado = input("Usuario: ").lower()
    contrasena_ingresada = input("Contraseña: ")
    for u in usuarios:
        if u[0] == usuario_ingresado and u[1] == contrasena_ingresada:
            print(f"\n\033[32m¡Bienvenido, {usuario_ingresado} ({u[2].upper()})!\033[0m")
            return u[2]
    print("\033[31mUsuario o contraseña incorrectos.\033[0m")
    return None
