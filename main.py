class Libro:
    
    def __init__(self, titulo, autor, isbn, precio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.precio = precio

    def aplicar_descuento(self, porcentaje_descuento):
        cantidad_descuento = self.precio * (porcentaje_descuento / 100)
        self.precio -= cantidad_descuento

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def eliminar_libro(self, isbn):
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]
    
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]

# Creación de la biblioteca
mi_biblioteca = Biblioteca()

# Creación de libros
libro1 = Libro("La divina comedia", "Dante Alighieri", "1473", 19.99)
libro2 = Libro("El Anticristo", "Friedrich Nietzsche", "1483", 39.99)

# Agregar libros a la biblioteca
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

# Aplicar descuento a los libros
libro1.aplicar_descuento(7)
libro2.aplicar_descuento(7)

# Imprimir detalles de los libros en la biblioteca
for libro in mi_biblioteca.libros:
    print(f"titulo: {libro.titulo}, autor: {libro.autor}, precio: {libro.precio}") 
