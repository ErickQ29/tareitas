class Envio:
    def __init__(self, cliente, peso, distancia):
        self.cliente = cliente
        self.peso = peso
        self.distancia = distancia
        self.costo_km = 1.50
    
    def calculo_final(self):
        costo_total = self.distancia * self.costo_km
        
        print(f"Cliente: {self.cliente}")
        print(f"Peso del paquete: {self.peso} kg")
        print(f"Distancia: {self.distancia} km")
        print(f"Costo por km: ${self.costo_km}")
        print(f"Costo total del envío: ${costo_total:.2f}")

def main():
    cliente = input("Ingrese el nombre del cliente: ")
    peso = float(input("Ingrese el peso del paquete (kg): "))
    distancia = float(input("Ingrese la distancia a recorrer (km): "))
    
    envio = Envio(cliente, peso, distancia)
    envio.calculo_final()

if __name__ == "__main__":
    main()
