from typing import Callable, List, Tuple

def validar_campo(valor: any, reglas: List[Callable[[any], Tuple[bool, str]]]) -> Tuple[bool, List[str]]:
    errores = list(filter(None, [mensaje for valido, mensaje in map(lambda r: r(valor), reglas) if not valido]))
    return len(errores) == 0, errores

def no_vacio(valor: any) -> Tuple[bool, str]:
    return bool(valor), "Este campo no puede estar vacío."

def longitud_exacta(longitud: int) -> Callable[[any], Tuple[bool, str]]:
    def regla(valor: any) -> Tuple[bool, str]:
        return len(valor) == longitud, f"Debe tener exactamente {longitud} caracteres."
    return regla

def solo_numeros(valor: any) -> Tuple[bool, str]:
    if not valor:
        return True, ""
    return valor.isdigit(), "Solo se permiten números."

def prefijo_valido(prefijos: Tuple[str, ...]) -> Callable[[any], Tuple[bool, str]]:
    def regla(valor: any) -> Tuple[bool, str]:
        return any(valor.startswith(prefijo) for prefijo in prefijos), f"Debe comenzar con uno de estos prefijos: {', '.join(prefijos)}"
    return regla

def validar_sku(sku: str) -> Tuple[bool, List[str]]:
    reglas = [
        no_vacio,
        longitud_exacta(8),
        solo_numeros,
        prefijo_valido(("12", "34", "56"))
    ]
    return validar_campo(sku, reglas)

def validar_precio(precio: str) -> Tuple[bool, List[str]]:
    reglas = [
        no_vacio,
        solo_numeros
    ]
    return validar_campo(precio, reglas)

def validar_cantidad(cantidad: str) -> Tuple[bool, List[str]]:
    reglas = [
        no_vacio,
        solo_numeros
    ]
    return validar_campo(cantidad, reglas)

datos_productos = (
    ("12345678", "Producto válido", "100", "10"),
    ("345678", "SKU incorrecto", "50", "5"),
    ("56ABCDE1", "Formato incorrecto", "abc", "5"),
    ("12999999", "SKU válido", "30", "10")
)

resultados = tuple(
    (
        sku,
        validar_sku(sku),
        validar_precio(precio),
        validar_cantidad(cantidad)
    ) for sku, nombre, precio, cantidad in datos_productos
)

for sku, val_sku, val_precio, val_cantidad in resultados:
    print(f"\nSKU: {sku}")
    print(" - SKU válido:", "Correcto" if val_sku[0] else f"Incorrecto: {', '.join(val_sku[1])}")
    print(" - Precio válido:", "Correcto" if val_precio[0] else f"Incorrecto: {', '.join(val_precio[1])}")
    print(" - Cantidad válida:", "Correcto" if val_cantidad[0] else f"Incorrecto: {', '.join(val_cantidad[1])}")

def test():
    assert validar_sku("12345678") == (True, [])
    assert validar_sku("345678") == (False, ["Debe tener exactamente 8 caracteres."])
    assert validar_precio("100") == (True, [])
    assert validar_precio("abc") == (False, ["Solo se permiten números."])
    assert validar_cantidad("10") == (True, [])
    assert validar_cantidad("") == (False, ["Este campo no puede estar vacío."])
    print("Todas las pruebas se completaron con éxito.")

test()
