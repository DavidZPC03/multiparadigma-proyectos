# Validador de datos

Intente aplicar una validacion en el ambiente de un formulario con una estructura similar a la que se mostro como ejemplo en clase.

## Funciones Principales

### `validar_campo(valor: any, reglas: List[Callable[[any], Tuple[bool, str]]]) -> Tuple[bool, List[str]]`

Valida un valor dado contra una lista de reglas de validación.

- **Parámetros:**

  - `valor`: El valor a validar.
  - `reglas`: Una lista de funciones de validación que toman un valor y devuelven una tupla `(bool, str)`.
- **Retorna:**

  - Una tupla `(bool, List[str])` donde el primer elemento indica si el valor es válido (`True`) o no (`False`), y el segundo elemento es una lista de mensajes de error.

### `no_vacio(valor: any) -> Tuple[bool, str]`

Valida que el valor no esté vacío.

- **Parámetros:**

  - `valor`: El valor a validar.
- **Retorna:**

  - Una tupla `(bool, str)` donde el primer elemento es `True` si el valor no está vacío, y `False` en caso contrario. El segundo elemento es un mensaje de error si el valor está vacío.

### `longitud_exacta(longitud: int) -> Callable[[any], Tuple[bool, str]]`

Devuelve una función que valida que el valor tenga una longitud exacta.

- **Parámetros:**

  - `longitud`: La longitud exacta que debe tener el valor.
- **Retorna:**

  - Una función que toma un valor y devuelve una tupla `(bool, str)` donde el primer elemento es `True` si el valor tiene la longitud exacta, y `False` en caso contrario. El segundo elemento es un mensaje de error si la longitud no coincide.

### `solo_numeros(valor: any) -> Tuple[bool, str]`

Valida que el valor contenga solo números.

- **Parámetros:**

  - `valor`: El valor a validar.
- **Retorna:**

  - Una tupla `(bool, str)` donde el primer elemento es `True` si el valor contiene solo números, y `False` en caso contrario. El segundo elemento es un mensaje de error si el valor contiene caracteres no numéricos.

### `prefijo_valido(prefijos: Tuple[str, ...]) -> Callable[[any], Tuple[bool, str]]`

Devuelve una función que valida que el valor comience con uno de los prefijos dados.

- **Parámetros:**

  - `prefijos`: Una tupla de prefijos válidos.
- **Retorna:**

  - Una función que toma un valor y devuelve una tupla `(bool, str)` donde el primer elemento es `True` si el valor comienza con uno de los prefijos, y `False` en caso contrario. El segundo elemento es un mensaje de error si el valor no comienza con ninguno de los prefijos.

## Funciones de Validación Específicas

### `validar_sku(sku: str) -> Tuple[bool, List[str]]`

Valida un SKU según las siguientes reglas:

1. No puede estar vacío.
2. Debe tener exactamente 8 caracteres.
3. Solo puede contener números.
4. Debe comenzar con uno de los prefijos válidos: "12", "34", "56".

- **Parámetros:**

  - `sku`: El SKU a validar.
- **Retorna:**

  - Una tupla `(bool, List[str])` donde el primer elemento indica si el SKU es válido, y el segundo elemento es una lista de mensajes de error.

### `validar_precio(precio: str) -> Tuple[bool, List[str]]`

Valida un precio según las siguientes reglas:

1. No puede estar vacío.
2. Solo puede contener números.

- **Parámetros:**

  - `precio`: El precio a validar.
- **Retorna:**

  - Una tupla `(bool, List[str])` donde el primer elemento indica si el precio es válido, y el segundo elemento es una lista de mensajes de error.

### `validar_cantidad(cantidad: str) -> Tuple[bool, List[str]]`

Valida una cantidad según las siguientes reglas:

1. No puede estar vacío.
2. Solo puede contener números.

- **Parámetros:**

  - `cantidad`: La cantidad a validar.
- **Retorna:**

  - Una tupla `(bool, List[str])` donde el primer elemento indica si la cantidad es válida, y el segundo elemento es una lista de mensajes de error.

## Ejemplo de Uso

El código incluye un ejemplo de uso donde se validan varios productos con diferentes SKU, precios y cantidades. Los resultados de la validación se imprimen en la consola.

```python
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
```
