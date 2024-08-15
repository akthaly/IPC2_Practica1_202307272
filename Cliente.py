class Cliente:
    def __init__(self, nombre, apellido, email, nit):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.nit = nit

    def __str__(self):
        return f'  Nombre: {self.nombre}\n  Apellido: {self.apellido}\n  Email Registrado: {self.email}\n  Numero de NIT: {self.nit}\n'
    