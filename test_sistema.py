from usuarios import buscar_usuario_recursivo
from productos import calcular_stock_total_recursivo
from ventas import buscar_producto_por_id, buscar_venta_por_id


# -------------------------------------------------------------------
# CASO DE PRUEBA 1: Búsqueda recursiva de usuarios (usuarios.py)
# -------------------------------------------------------------------
def test_buscar_usuario_recursivo_existente():
    lista_prueba = [
        ["admin", "1234", "admin"],
        ["ivarguello", "5678", "empleado"],
    ]
    
    posicion = buscar_usuario_recursivo(lista_prueba, "admin")
    assert posicion == 0

def test_buscar_usuario_recursivo_inexistente():
    lista_prueba = [["admin", "1234", "admin"]]
    
    posicion = buscar_usuario_recursivo(lista_prueba, "usuario_falso")
    assert posicion == -1