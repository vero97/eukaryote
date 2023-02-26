from abc import ABCMeta
from Contacto import Telefono
from Contacto import Mail
from persistent import Persistent
#from Tarjeta import TarjetaCredito
#from Tarjeta import TarjetaDebito

'''CLASE ABSTRACTA PERSONA'''

'''En la clase Persona definiremos todos aquellos atributos entre los 
clientes y los empleados y que heredaran las clases Empleado y CLiente'''

class Persona(metaclass=ABCMeta):

    def __init__(self, ci, nombre, apellido, direccion, numero_contacto, 
                email):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        Telefono.__init__(self, numero_contacto)
        Mail.__init__(self, email)

    def __str__(self):
        return "%s: %s, %s, %s" % str(self.ci), self.nombre, self.apellido, self.direccion

'''Clase hija de Persona. Es la clase encargada de instanciar los objetos 
del tipo emplado.'''
class Empleado (Persona, Persistent):

    def __init__(self, ci, nombre, apellido, direccion, fecha_nacimiento,
                usuario, contrasenia, numero_contacto, email):
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.contrasenia = contrasenia
        Persona.__init__(self, ci, nombre, apellido, direccion, numero_contacto, email)

'''Clase hija de Persona. Es la clase encargada de instanciar los objetos 
del tipo cliente'''
class Cliente(Persona, Persistent):

    def __init__(self, ruc, ci, nombre, apellido, direccion, numero_contacto,
                email):
        self.ruc = ruc
        Persona.__init__(self, ci, nombre, apellido, direccion, numero_contacto,
                        email)
