from typing import Callable, List, Tuple

# Función principal para validar un valor contra una lista de reglas.
def validar_campo(valor: any, reglas: List[Callable[[any], Tuple[bool, str]]]) -> Tuple[bool, List[str]]:
    """
    Valida un valor contra una lista de reglas.
    - Pureza: No modifica el valor original ni tiene efectos secundarios.
    - Inmutabilidad: Devuelve un nuevo resultado sin alterar el valor de entrada.
    """
    # Aplica cada regla al valor y filtra los mensajes de error.
    errores = list(filter(None, [mensaje for valido, mensaje in map(lambda r: r(valor), reglas) if not valido]))
    return len(errores) == 0, errores  # Devuelve si es válido y la lista de errores.


# Regla: Valida que el valor no esté vacío.
def no_vacio(valor: any) -> Tuple[bool, str]:
    """
    Valida que el valor no esté vacío.
    - Pureza: Solo depende del valor de entrada y no tiene efectos secundarios.
    - Inmutabilidad: Devuelve un nuevo resultado sin modificar el valor original.
    """
    return bool(valor), "Este campo no puede estar vacío."


# Regla: Valida que el valor tenga una longitud exacta.
def longitud_exacta(longitud: int) -> Callable[[any], Tuple[bool, str]]:
    """
    Devuelve una función que valida la longitud exacta del valor.
    - Pureza: La función generada es pura, ya que solo depende de su entrada.
    - Inmutabilidad: No modifica el valor original, solo lo valida.
    """
    def regla(valor: any) -> Tuple[bool, str]:
        return len(valor) == longitud, f"Debe tener exactamente {longitud} caracteres."
    return regla


# Regla: Valida que el valor contenga solo números.
def solo_numeros(valor: any) -> Tuple[bool, str]:
    """
    Valida que el valor contenga solo números.
    - Pureza: Solo depende del valor de entrada y no tiene efectos secundarios.
    - Inmutabilidad: Devuelve un nuevo resultado sin modificar el valor original.
    """
    if not valor:
        return True, ""  # Si el valor está vacío, se considera válido.
    return valor.isdigit(), "Solo se permiten números."


# Regla: Valida que el valor comience con uno de los prefijos dados.
def prefijo_valido(prefijos: Tuple[str, ...]) -> Callable[[any], Tuple[bool, str]]:
    """
    Devuelve una función que valida que el valor comience con uno de los prefijos.
    - Pureza: La función generada es pura, ya que solo depende de su entrada.
    - Inmutabilidad: No modifica el valor original, solo lo valida.
    """
    def regla(valor: any) -> Tuple[bool, str]:
        return any(valor.startswith(prefijo) for prefijo in prefijos), f"Debe comenzar con uno de estos prefijos: {', '.join(prefijos)}"
    return regla


# Función específica para validar un SKU.
def validar_sku(sku: str) -> Tuple[bool, List[str]]:
    """
    Valida un SKU según las reglas definidas.
    - Pureza: No modifica el SKU original ni tiene efectos secundarios.
    - Inmutabilidad: Devuelve un nuevo resultado sin alterar el SKU de entrada.
    """
    reglas = [
        no_vacio,
        longitud_exacta(8),
        solo_numeros,
        prefijo_valido(("12", "34", "56"))
    ]
    return validar_campo(sku, reglas)  # Aplica las reglas al SKU.


# Función específica para validar un precio.
def validar_precio(precio: str) -> Tuple[bool, List[str]]:
    """
    Valida un precio según las reglas definidas.
    - Pureza: No modifica el precio original ni tiene efectos secundarios.
    - Inmutabilidad: Devuelve un nuevo resultado sin alterar el precio de entrada.
    """
    reglas = [
        no_vacio,
        solo_numeros
    ]
    return validar_campo(precio, reglas)  # Aplica las reglas al precio.


# Función específica para validar una cantidad.
def validar_cantidad(cantidad: str) -> Tuple[bool, List[str]]:
    """
    Valida una cantidad según las reglas definidas.
    - Pureza: No modifica la cantidad original ni tiene efectos secundarios.
    - Inmutabilidad: Devuelve un nuevo resultado sin alterar la cantidad de entrada.
    """
    reglas = [
        no_vacio,
        solo_numeros
    ]
    return validar_campo(cantidad, reglas)  # Aplica las reglas a la cantidad.


# Datos de prueba para validar.
datos_productos = (
    ("12345678", "Producto válido", "100", "10"),
    ("345678", "SKU incorrecto", "50", "5"),
    ("56ABCDE1", "Formato incorrecto", "abc", "5"),
    ("12999999", "SKU válido", "30", "10")
)

# Aplica las validaciones a los datos de prueba.
resultados = tuple(
    (
        sku,
        validar_sku(sku),
        validar_precio(precio),
        validar_cantidad(cantidad)
    ) for sku, nombre, precio, cantidad in datos_productos
)

# Muestra los resultados de las validaciones.
for sku, val_sku, val_precio, val_cantidad in resultados:
    print(f"\nSKU: {sku}")
    print(" - SKU válido:", "Correcto" if val_sku[0] else f"Incorrecto: {', '.join(val_sku[1])}")
    print(" - Precio válido:", "Correcto" if val_precio[0] else f"Incorrecto: {', '.join(val_precio[1])}")
    print(" - Cantidad válida:", "Correcto" if val_cantidad[0] else f"Incorrecto: {', '.join(val_cantidad[1])}")


# Pruebas unitarias para verificar el funcionamiento del validador.
def test():
    """
    Pruebas unitarias para verificar que las funciones de validación funcionan correctamente.
    - Pureza: Las pruebas no modifican el estado del programa.
    - Inmutabilidad: Las pruebas verifican resultados sin alterar los datos originales.
    """
    assert validar_sku("12345678") == (True, [])
    assert validar_sku("345678") == (False, ["Debe tener exactamente 8 caracteres."])
    assert validar_precio("100") == (True, [])
    assert validar_precio("abc") == (False, ["Solo se permiten números."])
    assert validar_cantidad("10") == (True, [])
    assert validar_cantidad("") == (False, ["Este campo no puede estar vacío."])
    print("Todas las pruebas se completaron con éxito.")

test()