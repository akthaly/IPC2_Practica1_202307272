class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio = precio
    
    def __str__(self):
        # La f al principio es para indicar que es un string formateado (f-string) 
        return f'  Placa: {self.placa}\n  Marca: {self.marca}\n  Modelo: {self.modelo}\n  Descripción: {self.descripcion}\n  Precio: Q{self.precio}\n'
    
    