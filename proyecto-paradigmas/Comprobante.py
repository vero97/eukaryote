from abc import ABCMeta, abstractmethod
from persistent import Persistent

'''CLASE ABSTRACTA COMPROBANTE'''
class Comprobante(metaclass=ABCMeta):
    
    pass

'''CLASE ABSTRACTA DOCUMENTO'''
class Documento(metaclass=ABCMeta):
    
    pass

'''CLASE ABSTRACTA FACTURA. UNA FACTURA ES UN DOCUMENTO'''
class Factura (metaclass=ABCMeta):

    def __init__ (self, numero_factura, timbrado):
    
        self.numero_factura = numero_factura
        self.timbrado = timbrado

'''CLASE FACTURA CON NOMBRE: CLASE HIJA DE FACTURA

La factura con nombre nos va permitir emitir la factura a nombre de algun cliente, en caso que este lo solicite.
Tambièn esta clase emitirà facturas sin nombre a aquellas personas que no esten registradas en el sietema,
o que no quieran factura.

RAZON SOCIAL: es el nombre y apellido del cliente'''
class FacturaConNombre(Factura, Persistent):

    def __init__ (self, fecha_emision, ruc_ci, razon_social, direccion, total_por_producto, total_factura, numero_factura, timbrado):

        self.fecha_emision = fecha_emision
        self.ruc_ci = ruc_ci
        self.razon_social = razon_social
        self.direccion = direccion
        self.total_por_producto = total_por_producto
        self.total_factura = total_factura    
        Factura.__init__(self, numero_factura, timbrado)

