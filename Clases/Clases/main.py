from Ejercicio1 import *
from Ejercicio2 import *
from Ejercicio3 import *



print ("Ejercicio 1 \n")
 


print ("Ejercicio 2 \n")

linea_1 = "Hola me llamo Paula"
linea_2 = "Estoy estudiando en la UAX"

textoescrito = MVC(linea_1, linea_2)
textoescrito.escribir()


print ("Ejercicio 3 \n")
Naturaleza = Naturaleza()

producto = Producto(Naturaleza.alimentaria) # 5,5% de Iva 
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto) 
# 100% + 5,5% = 105,5%

producto = Producto(Naturaleza.servicio) # 20% de Iva 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 100% + 20% = 120%