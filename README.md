# Ejercicios_Estructura_Datos

El link de mi repositorio es el siguiente: [https://github.com/paulaanb/Ejercicios_Estructura_Datos]

El codigo de este ejercicio es:

# Ejercicio 1
    class Bloque: 
      # Un bloque es un conjunto de instrucciones ejecutadas 
      # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
    class Si: 
      # Representa una instrucción 'if'. 'condicion' es una cadena 
      # de caracteres que contiene la evaluación de la condición, 
       # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
      # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
      # si no se verifica. 
 
      def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
    class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
    class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 

     mostrar_ok = Mostrar('"OK"') 
    mostrar_ko = Mostrar('"KO"') 
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
    bloque_alternativa = Bloque() 
    bloque_alternativa.agregarInstruccion(alternativa) 
    bucle = MientrasQue(True, bloque_alternativa) 


# Ejercicio 2
    class MVC:

      def __init__(self, linea1, linea2):
        self.__linea1 = linea1
        self.__linea2 = linea2
        #Convertimos las lineas de texto a mayusculas para que sean cadena de texto
        if linea(self.__linea1, str):
            self.__linea1.upper()
        elif linea(self.__linea2, str):
            self.__linea2.upper()
        else:
            raise TypeError("La linea introducida no es una cadena de texto.")
        
      def respuesta(self):
        file = open("Frases.txt", "w")
        file.write(self.__linea1, "\n")
        file.write(self.__linea2)
        file.close()
       
 # Ejercicio 3
 
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
        
 # Main
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
    #100% + 5,5% = 105,5%

    producto = Producto(Naturaleza.servicio) # 20% de Iva 
    precio_neto = FactoryFactura.crear(producto).facturar() 
    print(precio_neto) 
    #100% + 20% = 120%
