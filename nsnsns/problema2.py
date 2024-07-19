class Empleado:
    def __init__(self, Nombre, ID, Salario, Departamento):
        self.nombre = Nombre
        self.id = ID
        self.salario = Salario
        self.departamento = Departamento

    def aplicar_aumento(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        print(f"Nuevo salario de {self.nombre}: {self.salario}")

class Departamento:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def eliminar_empleados(self, id):
        self.empleados = [empleado for empleado in self.empleados if empleado.id != id]

    def calcular_salario_promedio(self):
        total_salarios = sum(empleado.salario for empleado in self.empleados)
        promedio = total_salarios / len(self.empleados)
        return promedio
    
# Creación de empleados
empleado1 = Empleado("Erick", 1, 4000, "CyberSegurity")
empleado2 = Empleado("Ana", 2, 4100, "Software Development")
empleado3 = Empleado("Karla", 3, 4500, "Networking")

# Creación del departamento y adición de empleados
departamento = Departamento()
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)
departamento.agregar_empleado(empleado3)

# Aplicar aumento al salario del empleado1
empleado1.aplicar_aumento(10)
empleado2.aplicar_aumento(10)
empleado3.aplicar_aumento(10)

# Calcular y mostrar el salario promedio del departamento
promedio = departamento.calcular_salario_promedio()
print(f"Salario promedio del departamento: {promedio}")
