from usuarios import buscar_usuario_recursivo
from productos import calcular_stock_total_recursivo
from ventas import buscar_producto_por_id, buscar_venta_por_id


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

def test_calcular_stock_total_recursivo_con_datos():
    matriz_productos_prueba = [
        [1, "Pan lactal", "almacen", 1200.0, 50, 0.0],
        [2, "Detergente", "limpieza", 2500.0, 30, 0.1],
        [3, "Chocolate", "golosinas", 950.0, 20, 0.0],
    ]
    total = calcular_stock_total_recursivo(matriz_productos_prueba)
    assert total == 100