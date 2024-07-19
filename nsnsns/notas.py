class Notas:
    def __init__(self, notas):
        self.notas = notas
        self.total_notas = len(notas)
    
    def calculo_total(self):
        desaprobadas = sum(1 for nota in self.notas if nota < 71)
        aprobadas = self.total_notas - desaprobadas
        promedio_total = sum(self.notas) / self.total_notas
        promedio_aprobadas = sum(nota for nota in self.notas if nota >= 71) / aprobadas if aprobadas > 0 else 0
        promedio_desaprobadas = sum(nota for nota in self.notas if nota < 71) / desaprobadas if desaprobadas > 0 else 0
        
        print(f"Total de notas desaprobadas: {desaprobadas}")
        print(f"Total de notas aprobadas: {aprobadas}")
        print(f"Promedio total de notas: {promedio_total:.2f}")
        print(f"Promedio de notas aprobadas: {promedio_aprobadas:.2f}")
        print(f"Promedio de notas desaprobadas: {promedio_desaprobadas:.2f}")

def main():
    cantidad_notas = int(input("Ingrese la cantidad de notas a procesar: "))
    notas = []
    for _ in range(cantidad_notas):
        nota = int(input("Ingrese una nota: "))
        notas.append(nota)
    
    nota_clase = Notas(notas)
    nota_clase.calculo_total()

if __name__ == "__main__":
    main()
