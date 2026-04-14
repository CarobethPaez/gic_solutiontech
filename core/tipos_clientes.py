from core.cliente import Cliente

class ClienteRegular(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__(id_cliente, nombre, email, telefono) 
        self.tipo = "Regular"

class ClientePremium(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, descuento=15):
        super().__init__(id_cliente, nombre, email, telefono)
        self.tipo = "Premium"
        self.descuento = descuento

    def __str__(self): # Sobrescritura polimórfica 
        return super().__str__() + f" | Beneficio: {self.descuento}% OFF"

class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono, empresa):
        super().__init__(id_cliente, nombre, email, telefono)
        self.tipo = "Corporativo"
        self.empresa = empresa

    def __str__(self):
        return super().__str__() + f" | Empresa: {self.empresa}"