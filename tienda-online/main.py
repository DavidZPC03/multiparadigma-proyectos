# by David Perez 21100266
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("No se aceptan números negativos")
        self.__precio = nuevo_precio

    def calcular_costo(self):
        return self.precio

    def disponible(self):
        return self.stock > 0
    
    def __str__(self):
        return f'{self.nombre} - ${self.precio} (Stock: {self.stock})'


class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, costo_envio):
        super().__init__(nombre, precio, stock)
        self.costo_envio = costo_envio

    def calcular_costo(self):
        return self.precio + self.costo_envio
    
    def __str__(self):
        return f"{self.nombre} (Físico) - ${self.precio} + Envío: ${self.costo_envio} (Stock: {self.stock})"


class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, stock=-1)  

    def calcular_costo(self):
       
        return self.precio * 0.9
        
    def disponible(self):
        return True
    
    def __str__(self):
        return f"{self.nombre} (Digital) - ${self.precio} (10% de descuento aplicado)"


class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email})"


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.disponible():
            self.productos.append(producto)
            if producto.stock != -1:
                producto.stock -= 1
            print(f"{producto.nombre} agregado al carrito.")
        else:
            print(f"{producto.nombre} no está disponible.")

    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos)

    def __str__(self):
        if not self.productos:
            return "Carrito vacío"
        contenido = "\n".join(str(p) for p in self.productos)
        return f"Contenido del carrito:\n{contenido}"


class Tienda:
    def __init__(self):
        self.catalogo = []

    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)
        print(f"{producto.nombre} añadido al catálogo.")

    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        detalles = "\n".join(str(p) for p in carrito.productos)
        return f"Compra de {cliente}:\n{detalles}\nTotal: ${total:.2f}"


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
    
    
#pruebas -- by gpt
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
