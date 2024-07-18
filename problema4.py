class Libro:
    def __init__(self, libros):
        self.libros = libros
        self.total_libros = len(libros)
    
    def calculo_total(self):
        ficcion = sum(1 for libro in self.libros if libro['genero'] == 'Ficción')
        no_ficcion = sum(1 for libro in self.libros if libro['genero'] == 'No ficción')
        ciencia = sum(1 for libro in self.libros if libro['genero'] == 'Ciencia')
        historia = sum(1 for libro in self.libros if libro['genero'] == 'Historia')
        
        print(f"Total de libros vendidos: {self.total_libros}")
        print(f"Total de libros de Ficción vendidos: {ficcion}")
        print(f"Total de libros de No ficción vendidos: {no_ficcion}")
        print(f"Total de libros de Ciencia vendidos: {ciencia}")
        print(f"Total de libros de Historia vendidos: {historia}")

# Ejemplo de uso
libros = [
    {'titulo': 'Libro A', 'genero': 'Ficción'},
    {'titulo': 'Libro B', 'genero': 'No ficción'},
    {'titulo': 'Libro C', 'genero': 'Ciencia'},
    {'titulo': 'Libro D', 'genero': 'Historia'},
    {'titulo': 'Libro E', 'genero': 'Ficción'},
    {'titulo': 'Libro F', 'genero': 'Historia'}
]
libro_clase = Libro(libros)
libro_clase.calculo_total()

def main():
    cantidad_libros = int(input("Ingrese la cantidad de libros a procesar: "))
    libros = []
    for _ in range(cantidad_libros):
        titulo = input("Ingrese el título del libro: ")
        genero = input("Ingrese el género del libro (Ficción, No ficción, Ciencia, Historia): ")
        libros.append({'titulo': titulo, 'genero': genero})
    
    libro_clase = Libro(libros)
    libro_clase.calculo_total()

if __name__ == "__main__":
    main()
