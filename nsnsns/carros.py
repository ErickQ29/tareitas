class Descuento:
    def __init__(self, cliente, duracion, precio_diario):
        self.cliente = cliente
        self.duracion = duracion
        self.precio_diario = precio_diario
    
    def calculo_final(self):
        if self.duracion < 3:
            descuento = 0
        elif 3 <= self.duracion <= 6:
            descuento = 0.05
        else:
            descuento = 0.10
        
        precio_total = self.duracion * self.precio_diario
        precio_descuento = precio_total * descuento
        precio_final = precio_total - precio_descuento
        
        print(f"Cliente: {self.cliente}")
        print(f"Duración: {self.duracion} días")
        print(f"Precio diario: ${self.precio_diario}")
        print(f"Descuento: ${precio_descuento:.2f}")
        print(f"Precio final: ${precio_final:.2f}")

def main():
    cliente = input("Ingrese el nombre del cliente: ")
    duracion = int(input("Ingrese la duración del alquiler (en días): "))
    precio_diario = float(input("Ingrese el precio diario del alquiler: "))
    
    descuento = Descuento(cliente, duracion, precio_diario)
    descuento.calculo_final()

if __name__ == "__main__":
    main()
