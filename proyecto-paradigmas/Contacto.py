from abc import ABCMeta
from persistent import Persistent

'''CLASE ABSTRACTA CONTACTO'''
class Contacto(metaclass=ABCMeta):

    pass

'''Las clases de contacto: Telefono, Mail, RedSocial, son para tener los datos de los clientes
y que sea facil el acceso a ellos.

POdremos instanciar contactos del tipo telefono, mail y red social, actualmente en nuestra implementacion
tenemos solo Telefono y MAil.'''
class Telefono(object):

    def __init__(self, numero_contacto):
        
        self.numero_contacto = numero_contacto

class Mail(object):

    def __init__(self, email):
        
        self.email = email
