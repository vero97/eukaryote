from abc import ABCMeta
from persistent import Persistent

class Tarjeta (metaclass=ABCMeta):
    '''Clase abstracta Tarjeta'''

    def __init__ (self, fecha_vencimiento, denominacion):

        self.fecha_vecimiento = fecha_vencimiento
        self.denomiacion = denominacion

class TarjetaCredito (Tarjeta, Persistent):
    '''INFORMACION DE CLASES.
    TarjetaCredito: Nos va permitir instanciar objetos del tipo tarjeta de credito. Hereda Tarjeta.
    Este modulo esta aun en desarrollo'''

    def __init__ (self, fecha_vencimiento, denominacion):
        Tarjeta.__init__(self, fecha_vencimiento, denominacion)
      
class TarjetaDebito (Tarjeta, Persistent):
    '''INFORMACION DE CLASES.
    TarjetaDebito: Nos va permitir instanciar objetos del tipo tarjeta de debito. Hereda Tarjeta.
    Este modulo esta aun en desarrollo'''
    def __init__ (self, fecha_vencimiento, denominacion):
        Tarjeta.__init__(self, fecha_vencimiento, denominacion)
