# Documentación del Simulador de Tienda Online

intento de una tienda que simular un eccomerce ---- David Perez

## Clases Principales

### `Producto`

Clase base que representa un producto en la tienda.

- **Atributos:**

  - `nombre`: Nombre del producto.
  - `precio`: Precio del producto.
  - `stock`: Cantidad disponible en stock.
- **Métodos:**

  - `calcular_costo()`: Devuelve el precio del producto.
  - `disponible()`: Devuelve `True` si el producto está disponible (stock > 0).
  - `__str__()`: Devuelve una representación en cadena del producto.
- **Propiedades:**

  - `precio`: Getter y setter para el precio. El setter valida que el precio no sea negativo.

### `ProductoFisico`

Clase que representa un producto físico, hereda de `Producto`.

- **Atributos adicionales:**

  - `costo_envio`: Costo de envío del producto.
- **Métodos:**

  - `calcular_costo()`: Devuelve el precio del producto más el costo de envío.
  - `__str__()`: Devuelve una representación en cadena del producto físico.

### `ProductoDigital`

Clase que representa un producto digital, hereda de `Producto`.

- **Métodos:**
  - `calcular_costo()`: Devuelve el precio del producto con un 10% de descuento.
  - `disponible()`: Siempre devuelve `True`, ya que los productos digitales no tienen stock.
  - `__str__()`: Devuelve una representación en cadena del producto digital.

### `Cliente`

Clase que representa un cliente de la tienda.

- **Atributos:**

  - `nombre`: Nombre del cliente.
  - `email`: Correo electrónico del cliente.
- **Métodos:**

  - `__str__()`: Devuelve una representación en cadena del cliente.

### `Carrito`

Clase que representa el carrito de compras de un cliente.

- **Atributos:**

  - `productos`: Lista de productos en el carrito.
- **Métodos:**

  - `agregar_producto(producto)`: Agrega un producto al carrito si está disponible.
  - `calcular_total()`: Calcula el costo total de los productos en el carrito.
  - `__str__()`: Devuelve una representación en cadena del contenido del carrito.

### `Tienda`

Clase que representa la tienda online.

- **Atributos:**

  - `catalogo`: Lista de productos en el catálogo de la tienda.
- **Métodos:**

  - `agregar_al_catalogo(producto)`: Agrega un producto al catálogo.
  - `buscar_producto(nombre)`: Busca un producto en el catálogo por nombre.
  - `realizar_compra(cliente, carrito)`: Realiza una compra para un cliente con los productos en el carrito.

## Ejemplo de Uso

El código incluye un ejemplo de uso donde se crea una tienda, se agregan productos al catálogo, se crea un cliente y se realiza una compra.

```python
if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_al_catalogo(Producto("Libro", 20, 5))
    tienda.agregar_al_catalogo(ProductoDigital("Ebook", 20))
    tienda.agregar_al_catalogo(ProductoFisico("Cuaderno", 10, 3, 2)) # Producto adicional

    cliente = Cliente("Ana", "ana@mail.com")
    carrito = Carrito()

    carrito.agregar_producto(tienda.buscar_producto("Libro"))
    carrito.agregar_producto(tienda.buscar_producto("Ebook"))
    carrito.agregar_producto(tienda.buscar_producto("Cuaderno"))

    print(tienda.realizar_compra(cliente, carrito))
```
