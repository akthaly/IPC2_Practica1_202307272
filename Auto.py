class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio = precio
    
    def __str__(self):
        # La f al principio es para indicar que es un string formateado (f-string) 
        return f'Placa: {self.placa}\nMarca: {self.marca}\nModelo: {self.modelo}\nDescripción: {self.descripcion}\nPrecio: {self.precio}\n'
    
    