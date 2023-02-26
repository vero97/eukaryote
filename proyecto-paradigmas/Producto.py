from abc import ABCMeta, abstractmethod
from persistent import Persistent

'''CLASE ABSTRACTA PRODUCTO'''
class Producto(metaclass=ABCMeta):
    pass

'''CLASE ABSTRACTA "ALIMENTO", SU FINALIDAD ES: CLASIFICAR LOS ALIMENTOS
(PRODUCTOS) QUE SE VENDEN EN EL RESTAURANTE'''

class Alimento(metaclass=ABCMeta):
    
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

'''INFORMACION DE CLASES HEREDERAS DE ALIMENTO.
Hamburguesa: nos permitira instanciar objetos hamburguesa. hereda la clase Alimento
Pizza: nos permitira instanciar objetos pizza. hereda la clase Alimento
Papa_Frita: nos permitira instanciar objetos papa frita. hereda la clase Alimento
Lomito: nos permitira instanciar objetos lomito. hereda la clase Alimento'''

class Hamburguesa (Alimento, Persistent):
    
    def __init__(self, codigo, nombre, precio, grupo):

        Alimento.__init__(self, codigo, nombre, precio)
        self.grupo = grupo

class Pizza (Alimento, Persistent):
    
    def __init__(self, codigo, nombre, precio, sabor):

       Alimento.__init__(self, codigo, nombre, precio)
       self.sabor = sabor
                
class PapaFrita (Alimento, Persistent):

    def __init__(self, codigo, nombre, precio, tamanio):

        Alimento.__init__(self, codigo, nombre, precio)
        self.tamanio = tamanio
        
class Lomito (Alimento, Persistent):
    def __init__(self, codigo, nombre, precio, grupo):

        Alimento.__init__(self, codigo, nombre, precio)
        self.grupo = grupo    

'''CLASE ABSTRACTA "BEBIDA", SU FINALIDAD ES: CLASIFICAR LAS BEBIDAS
(PRODUCTOS) QUE SE VENDEN EN EL RESTAURANTE (CON Y SIN ALCOHOL)'''

class Bebida (metaclass=ABCMeta):

    def __init__(self, codigo):
        self.codigo = codigo
        pass

'''INFORMACION DE CLASES HEREDERAS DE BEBIDA.
BebidaConAlcohol: nos permitira instanciar objetos beida con alcohol. Hereda Bebida
BebidaSinAlcohol: nos permitira instanciar objetos beida sin alcohol. Hereda Bebida
'''

class BebidaConAlcohol(Bebida, Persistent):

    def __init__(self, codigo, ca_nombre, ca_precio):
        Bebida.__init__(self, codigo)
        self.ca_nombre = ca_nombre
        self.ca_precio = ca_precio
      
class BebidaSinAlcohol(Bebida, Persistent):

    def __init__(self, codigo, sa_nombre, sa_precio):
        Bebida.__init__(self, codigo)
        self.sa_nombre = sa_nombre 
        self.sa_precio = sa_precio
