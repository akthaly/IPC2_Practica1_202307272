class Compras:
    def __init__ (self, autos, cliente, ID):
        self.autos = autos
        self.cliente = cliente
        self.ID = ID

    def totalCompra(self):
        total = 0
        for autos in self.autos:
            total += autos.precio
        return total
    
    def totalCompraSeguro(self):
        total = 0
        for autos in self.autos:
            total += autos.precio + autos.precio*0.15
        return total
    
    def __str__(self):
        autos_info = "\n".join(str(auto) for auto in self.autos)
        return f"ID Compra: {self.ID}\nCLIENTE(S):\n{self.cliente}\nAUTO(S) COMPRADO(S):\n{autos_info}\n"