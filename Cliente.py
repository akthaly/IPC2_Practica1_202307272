class Cliente:
    def __init__(self, nombre, apellido, email, nit):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.nit = nit

    def __str__(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nEmail Registrado: {self.email}\nNumero de NIT: {self.nit}\n'
    