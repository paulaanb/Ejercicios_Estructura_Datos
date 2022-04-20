#Enunciado: siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar, las convierta a mayúsculas y las escriba en un archivo. Tenga en cuenta que para beneficiarse plenamente de las ventajas del design pattern MVC, los atributos, en particular los del modelo, se deben encapsular.


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