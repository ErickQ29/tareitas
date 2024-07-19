class Membresia:
    def __init__(self, cliente, tipo_membresia, precio):
        self.cliente = cliente
        self.tipo_membresia = tipo_membresia
        self.precio = precio
    
    def calculo_final(self):
        if self.tipo_membresia == 'Básica':
            descuento = 0.05
        elif self.tipo_membresia == 'Premium':
            descuento = 0.10
        elif self.tipo_membresia == 'VIP':
            descuento = 0.15
        else:
            descuento = 0
        
        precio_descuento = self.precio * descuento
        precio_final = self.precio - precio_descuento
        
        print(f"Cliente: {self.cliente}")
        print(f"Tipo de membresía: {self.tipo_membresia}")
        print(f"Precio: ${self.precio}")
        print(f"Descuento: ${precio_descuento:.2f}")
        print(f"Precio final: ${precio_final:.2f}")

def main():
    cliente = input("Ingrese el nombre del cliente: ")
    tipo_membresia = input("Ingrese el tipo de membresía (Básica, Premium, VIP): ")
    precio = float(input("Ingrese el precio de la membresía: "))
    
    membresia = Membresia(cliente, tipo_membresia, precio)
    membresia.calculo_final()

if __name__ == "__main__":
    main()
