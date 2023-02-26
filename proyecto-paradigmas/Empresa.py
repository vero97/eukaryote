from abc import ABCMeta
from persistent import Persistent
from Contacto import Telefono
from Contacto import Mail

'''CLASE ABSTRACTA EMPRESA'''
class Empresa(metaclass=ABCMeta):

    pass

'''Clase Restaurante.

Clase que nos va permitir instanciar los datos de nuestra empresa. 

Actualmente se instanciaron los datos de la empresa. El hecho que que nosotros podamos
tener los datods de nuestro local hace que las actualizaciones que vayamos a hacer 
en el numero de contacto, mail, etc. 
resulten mas facil ya que accederemos a cada atributo en caso de que necesitemos. 

'''
class Restaurante(Persistent):

    def __init__(self, nombre, ruc, direccion, numero_contacto, email):
        self.nombre = nombre
        self.ruc = ruc
        self.direccion = direccion
        Telefono.__init__(self, numero_contacto)
        Mail.__init__(self, email)
        #self.monto_delivery = 5000



