class Producto:
    def __init__(self, Nombre_Producto, ID_Producto, Precio, Cantidad_Stock):
        self.nombre = Nombre_Producto
        self.id = ID_Producto
        self.precio = Precio
        self.stock = Cantidad_Stock

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def quitar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else: 
            print("insuficiente cantidad en stock")

    def valor_total(self):
        return self.precio * self.stock

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id_producto):
        self.productos = [producto for producto in self.productos if producto.id != id_producto]

    def buscar_producto_por_nombre(self, nombre_producto):
        return [producto for producto in self.productos if producto.nombre.lower() == nombre_producto.lower()]

    def calcular_valor_total_stock(self):
        total = sum(producto.valor_total() for producto in self.productos)
        return total


# Ejemplo de uso
producto1 = Producto("Laptop", 1, 1500.00, 10)
producto2 = Producto("Mouse", 2, 25.00, 200)

tienda = Tienda()
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Agregar y quitar stock
producto1.agregar_stock(5)
producto2.quitar_stock(20)

# Buscar producto por nombre
resultados_busqueda = tienda.buscar_producto_por_nombre("Laptop")
for producto in resultados_busqueda:
    print(f"Producto encontrado: {producto.nombre} con ID: {producto.id}")

# Calcular valor total del stock
valor_total_stock = tienda.calcular_valor_total_stock()
print(f"Valor total del stock en la tienda: ${valor_total_stock}")