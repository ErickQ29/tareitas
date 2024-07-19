class Producto:
    def __init__(self, productos):
        self.productos = productos
        self.total_productos = len(productos)
    
    def calculo_total(self):
        alimentos = sum(1 for producto in self.productos if producto['categoria'] == 'Alimentos')
        bebidas = sum(1 for producto in self.productos if producto['categoria'] == 'Bebidas')
        higiene = sum(1 for producto in self.productos if producto['categoria'] == 'Higiene')
        otros = sum(1 for producto in self.productos if producto['categoria'] == 'Otros')
        
        promedio_total = self.total_productos
        promedio_alimentos = alimentos / self.total_productos if self.total_productos > 0 else 0
        promedio_bebidas = bebidas / self.total_productos if self.total_productos > 0 else 0
        promedio_higiene = higiene / self.total_productos if self.total_productos > 0 else 0
        promedio_otros = otros / self.total_productos if self.total_productos > 0 else 0
        
        print(f"Total de productos vendidos: {self.total_productos}")
        print(f"Total de alimentos vendidos: {alimentos}")
        print(f"Total de bebidas vendidas: {bebidas}")
        print(f"Total de productos de higiene vendidos: {higiene}")
        print(f"Total de otros productos vendidos: {otros}")
        print(f"Promedio de ventas de alimentos: {promedio_alimentos:.2f}")
        print(f"Promedio de ventas de bebidas: {promedio_bebidas:.2f}")
        print(f"Promedio de ventas de higiene: {promedio_higiene:.2f}")
        print(f"Promedio de ventas de otros productos: {promedio_otros:.2f}")

def main():
    cantidad_productos = int(input("Ingrese la cantidad de productos a procesar: "))
    productos = []
    for _ in range(cantidad_productos):
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto (Alimentos, Bebidas, Higiene, Otros): ")
        productos.append({'nombre': nombre, 'categoria': categoria})
    
    producto_clase = Producto(productos)
    producto_clase.calculo_total()

if __name__ == "__main__":
    main()
