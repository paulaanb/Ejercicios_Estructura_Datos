#Enunciado: Implementar un programa que factura productos por valor de 100, con la tasa de IVA correcta, según sean productos de alimentación o servicios.

class Naturaleza:
    def __init__(self):
        self.alimentaria = 0.055 #5,5%
        self.servicio = 0.2 #20%


class Producto(Naturaleza):
    def __init__(self, tasa_iva):
        self.tasa_iva = tasa_iva
    def facturar(self):
        return 100 + 100*self.tasa_iva


class FactoryFactura(Producto):
    def __init__(self):
        pass
    def crear(self):
        clase = Producto(self.tasa_iva)
        return clase