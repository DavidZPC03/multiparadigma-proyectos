# by David Perez 21100266

# Clase base que representa un producto en la tienda.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio  # Precio del producto
        self.stock = stock    # Cantidad disponible en stock

    # Getter para el precio
    @property
    def precio(self):
        return self.__precio
    
    # Setter para el precio con validación de números negativos
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("No se aceptan números negativos")
        self.__precio = nuevo_precio

    # Método para calcular el costo del producto (por defecto, el precio)
    def calcular_costo(self):
        return self.precio

    # Método para verificar si el producto está disponible
    def disponible(self):
        return self.stock > 0
    
    # Representación en cadena del producto
    def __str__(self):
        return f'{self.nombre} - ${self.precio} (Stock: {self.stock})'


# Clase que representa un producto físico, hereda de Producto.
class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, costo_envio):
        super().__init__(nombre, precio, stock)
        self.costo_envio = costo_envio  # Costo adicional de envío

    # Método para calcular el costo total (precio + costo de envío)
    def calcular_costo(self):
        return self.precio + self.costo_envio
    
    # Representación en cadena del producto físico
    def __str__(self):
        return f"{self.nombre} (Físico) - ${self.precio} + Envío: ${self.costo_envio} (Stock: {self.stock})"


# Clase que representa un producto digital, hereda de Producto.
class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, stock=-1)  # Stock -1 indica disponibilidad ilimitada

    # Método para calcular el costo con un 10% de descuento
    def calcular_costo(self):
        return self.precio * 0.9
        
    # Método para verificar disponibilidad (siempre disponible para productos digitales)
    def disponible(self):
        return True
    
    # Representación en cadena del producto digital
    def __str__(self):
        return f"{self.nombre} (Digital) - ${self.precio} (10% de descuento aplicado)"


# Clase que representa un cliente de la tienda.
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email    # Correo electrónico del cliente
    
    # Representación en cadena del cliente
    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email})"


# Clase que representa el carrito de compras de un cliente.
class Carrito:
    def __init__(self):
        self.productos = []  # Lista de productos en el carrito

    # Método para agregar un producto al carrito si está disponible
    def agregar_producto(self, producto):
        if producto.disponible():
            self.productos.append(producto)
            if producto.stock != -1:  # Reduce el stock si no es un producto digital
                producto.stock -= 1
            print(f"{producto.nombre} agregado al carrito.")
        else:
            print(f"{producto.nombre} no está disponible.")

    # Método para calcular el costo total de los productos en el carrito
    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos)

    # Representación en cadena del contenido del carrito
    def __str__(self):
        if not self.productos:
            return "Carrito vacío"
        contenido = "\n".join(str(p) for p in self.productos)
        return f"Contenido del carrito:\n{contenido}"


# Clase que representa la tienda online.
class Tienda:
    def __init__(self):
        self.catalogo = []  # Lista de productos en el catálogo

    # Método para agregar un producto al catálogo
    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)
        print(f"{producto.nombre} añadido al catálogo.")

    # Método para buscar un producto en el catálogo por nombre
    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    # Método para realizar una compra con los productos en el carrito
    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        detalles = "\n".join(str(p) for p in carrito.productos)
        return f"Compra de {cliente}:\n{detalles}\nTotal: ${total:.2f}"


# Bloque principal para ejecutar el simulador de la tienda
if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_al_catalogo(Producto("Libro", 20, 5))
    tienda.agregar_al_catalogo(ProductoDigital("Ebook", 20))
    tienda.agregar_al_catalogo(ProductoFisico("Cuaderno", 10, 3, 2))  # Producto adicional

    cliente = Cliente("Ana", "ana@mail.com")
    carrito = Carrito()

    carrito.agregar_producto(tienda.buscar_producto("Libro"))
    carrito.agregar_producto(tienda.buscar_producto("Ebook"))
    carrito.agregar_producto(tienda.buscar_producto("Cuaderno"))

    print(tienda.realizar_compra(cliente, carrito))
    
    
# Pruebas unitarias para verificar el funcionamiento del carrito
import unittest

class TestCarrito(unittest.TestCase):
    def test_carrito_vacio(self):
        carrito = Carrito()
        self.assertEqual(carrito.calcular_total(), 0)

    def test_carrito_con_productos(self):
        carrito = Carrito()
        producto1 = Producto("Libro", 20, 5)
        producto2 = ProductoDigital("Ebook", 20)

        carrito.agregar_producto(producto1)
        carrito.agregar_producto(producto2)

        self.assertEqual(carrito.calcular_total(), 38)

if __name__ == '__main__':
    unittest.main()