from persistent import Persistent
from Contacto import Telefono
from Contacto import Mail

'''Esta clase nos va permitir instanciar todos los proveedores que tenga el restaurante.
Asì mismo, tendra funciones como la de reposicion de stock en caso de que haya algun faltante'''

class Proveedor(Persistent):

    def __init__(self, ruc, razon_social, direccion, numero_contacto, email):
        self.ruc = ruc
        self.razon_social = razon_social
        self.direccion = direccion
        Telefono.__init__(self, numero_contacto)
        Mail.__init__(self, email)

    
