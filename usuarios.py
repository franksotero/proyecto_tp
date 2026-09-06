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
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
    nuevo_usuario = generar_usuario()
    print(f"Su nombre de usuario asignado es: {nuevo_usuario}")
    for u in usuarios:
        if u[0] == nuevo_usuario:
            print("El usuario ingresado ya existe.")
            return
    nueva_contrasena = input("Ingresa una contraseña: ")
    usuarios.append([nuevo_usuario, nueva_contrasena, "empleado"])
    print("¡Usuario registrado con éxito como Empleado!")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario_ingresado = input("Usuario: ").lower()
    contrasena_ingresada = input("Contraseña: ")
    for u in usuarios:
        if u[0] == usuario_ingresado and u[1] == contrasena_ingresada:
            print(f"\n¡Bienvenido, {usuario_ingresado} ({u[2].upper()})!")
            return u[2]
    print("Usuario o contraseña incorrectos.")
    return None
