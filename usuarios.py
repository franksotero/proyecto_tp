"""
Módulo de autenticación y gestión de usuarios.
Maneja el inicio de sesión del personal y el registro de nuevos empleados
"""

NOMBRE_ARCHIVO_USUARIOS = "usuarios.txt"

def cargar_usuarios_desde_archivo(ruta):
    """
    Lee el archivo de texto de usuarios y retorna la lista en memoria.
    Usa manejo de excepciones try-except y la sentencia with.
    """
    lista = []
    try:
        with open(ruta, "r", encoding="utf-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if linea:
                    campos = linea.split(",")
                    lista.append([campos[0], campos[1], campos[2]])
    except FileNotFoundError:
        print(f"Aviso: El archivo '{ruta}' no existe. Se creara un nuevo archivo.")
    except OSError as err:
        print(f"Error al intentar leer '{ruta}': {err}")
    return lista
#nombre de usuario, contraseña, rol

def guardar_usuarios_en_archivo(ruta, lista_usuarios):
    """
    Guarda la lista de usuarios sobreescribiendo el archivo de texto.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as arch:
            for u in lista_usuarios:
                arch.write(f"{u[0]},{u[1]},{u[2]}\n")
    except OSError as err:
        print(f"Error al intentar escribir en '{ruta}': {err}")

usuarios = cargar_usuarios_desde_archivo(NOMBRE_ARCHIVO_USUARIOS)

def generar_usuario():
    """
    Genera un nombre de usuario en minúsculas combinando las primeras 2 iniciales del nombre y el apellido.
    """
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    usuario = (nombre[:2] + apellido).lower()
    return usuario

def registrar_usuario():
    """
    Registra un nuevo usuario con rol 'empleado' asignandole un nombre de usuario generado automaticamente.
    """
    print("\n\033[4;35m--- REGISTRO DE NUEVO USUARIO ---\033[0m")
    nuevo_usuario = generar_usuario()
    print(f"Su nombre de usuario asignado es: {nuevo_usuario}")
    for u in usuarios:
        if u[0] == nuevo_usuario:
            print("\033[31mEl usuario ingresado ya existe.\033[0m")
            return
    nueva_contrasena = input("Ingresa una contraseña: ")
    usuarios.append([nuevo_usuario, nueva_contrasena, "empleado"])
    guardar_usuarios_en_archivo(NOMBRE_ARCHIVO_USUARIOS, usuarios)
    
    print("\033[32m¡Usuario registrado con éxito como Empleado!\033[0m")

def iniciar_sesion():
    """
    Autentica a un usuario comprobando su credenciales.
    Return: El rol del usuario ('admin' o 'empleado') si es correcto, none si falla algo.
    """
    print("\n\033[4;35m--- INICIO DE SESIÓN ---\033[0m")
    usuario_ingresado = input("Usuario: ").lower()
    contrasena_ingresada = input("Contraseña: ")
    for u in usuarios:
        if u[0] == usuario_ingresado and u[1] == contrasena_ingresada:
            print(f"\n\033[32m¡Bienvenido, {usuario_ingresado} ({u[2].upper()})!\033[0m")
            return u[2]
    print("\033[31mUsuario o contraseña incorrectos.\033[0m")
    return None
