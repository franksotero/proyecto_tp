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

def eliminar_usuario(rol):
    """
    Elimina un usuario del sistema mediante su nombre de usuario.
    Solo los admins pueden realizar esta accion. No permite eliminar al propio "admin" principal.
    """
    if rol != "admin":
        print("\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden eliminar usuarios.\033[0m")
        return
    print("\n\033[4;35m--- ELIMINAR USUARIO ---\033[0m")
    
    #Muestra los usuarios actuales que existen
    print("\n---- USUARIOS REGISTRADOS ----")
    print(f"{'USUARIO':<15} | {'ROL':<10}")
    print("-" * 30)
    for u in usuarios:
        print(f"{u[0]:<15} | {u[2]:<10}")
    print("-" * 30)

    usuario_a_eliminar = input("\nIngrese el nombre de usuario a eliminar: ").lower().strip()

    if usuario_a_eliminar == "admin":
        print("\033[31m[ERROR] No se puede eliminar al administrador principal.\033[0m")
        return

    posicion = buscar_usuario_recursivo(usuarios, usuario_a_eliminar)

    if posicion != -1:
        confirmacion = input(f"¿Está seguro de eliminar al usuario '{usuario_a_eliminar}'? (si/no): ").lower()
        if confirmacion == "si":
            usuarios.pop(posicion)
            guardar_usuarios_en_archivo(NOMBRE_ARCHIVO_USUARIOS, usuarios)
            print("\033[32m¡Usuario eliminado con éxito!\033[0m")
        else:
            print("\033[31mOperación cancelada.\033[0m")
    else:
        print("\033[31mEl usuario ingresado no existe.\033[0m")

def menu_usuarios(rol):
    """
    Despliega el menu de gestión de usuarios
    Restringido unicamente para el rol "admin".
    """
    if rol != "admin":
        print("\n\033[37;41m[ACCESO DENEGADO] Solo los administradores pueden gestionar usuarios.\033[0m")
        return

    opcion = ""
    while opcion != "3":
        print("\n==================================")
        print("\033[1;34m       GESTIÓN DE USUARIOS        \033[0m")
        print("==================================")
        print("1. Registrar nuevo usuario")
        print("2. Eliminar usuario")
        print("3. Volver al menu principal")
        opcion = input("Elige una opción (1-3): ")
        if opcion == "1":
            registrar_usuario()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            eliminar_usuario(rol)
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            print("\nRegresando al menú principal...")
        else:
            print("\n\033[31mOpción no valida. Intenta de nuevo.\033[0m")

def buscar_usuario_recursivo(lista_usuarios, usuario_buscar, i=0):
    """
    Busca la posicion de un usuario en la lista.
    - Caso Base 1: i == len(lista_usuarios) -> no se encontro, retorna -1.
    - Caso Base 2: lista_usuarios[i][0] == usuario_buscar -> Se encontro, retorna el índice "i".
    - Caso Recursivo: Llamada a la funcion incrementando "i" en 1.
    - Reduccion del dominio: Avanza indice (i) hasta el final de la lista.
    """
    if i == len(lista_usuarios):
        return -1
    if lista_usuarios[i][0] == usuario_buscar:
        return i
    
    return buscar_usuario_recursivo(lista_usuarios, usuario_buscar, i + 1)