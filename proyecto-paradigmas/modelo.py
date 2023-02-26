from mizodb import MiZODB, transaction
from persistent.list import PersistentList
from Persona import Empleado
from Persona import Cliente
from Proveedor import Proveedor
from Producto import Hamburguesa
from Producto import Pizza
from Producto import PapaFrita
from Producto import Lomito
from Producto import BebidaConAlcohol
from Producto import BebidaSinAlcohol
from Empresa import Restaurante
from Comprobante import FacturaConNombre

from datetime import datetime
import platform
import os
import time
import sys

'''Clase Modelo: En esta clase se van a definir todas las operaciones que vayamos a necesitar
para nuestro sistema.

Actualmente encontraremos metodos como: guardar, listar, buscar, obtener, calcular, etc. 

Se iràn explicando su funcionamiento ya dentro de la clase antes de la definicion def.'''

class Modelo():

    '''METODOS PARA BUSCAR, LISTAR Y GUARDAR A LOS CLIENTES, EMPLEADOS Y PROVEEDORES.
    PERTENECEN A LAS CLASES: Empleado, Cliente y Proveedor.'''

    '''Defimnios el mètodo que listarà a todos los empleados'''
    def listar_empleados(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz
        empleados = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]
            
            if isinstance(obj, Empleado):
            
                empleado = Empleado(obj.ci, obj.nombre, obj.apellido,
                                    obj.direccion, obj.fecha_nacimiento,
                                    obj.usuario, obj.contrasenia, obj.numero_contacto,
                                    obj.email)

                empleados.append(empleado)
        db.close()
        return empleados

    '''Defimos el mètodo que listarà a todos los clientes'''    

    def listar_clientes(self):
        
        db = MiZODB('./Data.fs')
        dbroot = db.raiz
        clientes = []

        for key in dbroot.keys():
            
            obj = dbroot[key]

            if isinstance(obj, Cliente):
                cliente = Cliente(obj.ruc, obj.ci, obj.nombre, obj.apellido,
                                  obj.direccion, obj.numero_contacto, obj.email)

                clientes.append(cliente)
        db.close()
        return clientes

    '''Definimos el mètodo que listarà a todos los proveedores''' 

    def listar_proveedores(self):
        
        db = MiZODB('./Data.fs')
        dbroot = db.raiz
        proveedores = []

        for key in dbroot.keys():
            
            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Proveedor):
                proveedor = Proveedor(obj.ruc, obj.razon_social,
                                      obj.direccion, obj.numero_contacto, obj.email)

                proveedores.append(proveedor)

        db.close()
        return proveedores

    '''Metodo que permite guardar los objetos empleado'''

    def guardar_empleado(self, empleado):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz
        
        dbroot[empleado.ci] = empleado

        transaction.commit()
        db.close()        

    '''Metodo que permite guardar los objetos cliente'''

    def guardar_cliente(self, cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[cliente.ruc] = cliente
        dbroot[cliente.ci] = cliente

        transaction.commit()
        db.close()

    def no_guardar_cliente(self, cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[cliente.ruc] = cliente
        dbroot[cliente.ci] = cliente

        transaction.abort()
        db.close()
    '''Metodo que permite guardar los objetos cliente'''

    def guardar_proveedor(self, proveedor):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[proveedor.ruc] = proveedor

        transaction.commit()
        db.close()

    '''Metodo que no confirmarà la transacciòn.'''

    def abortar_transaccion(self, proveedor):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[proveedor.ruc] = proveedor

        transaction.abort()
        db.close()

    '''Mètodo que permite buscar al empleado. Recibe como parametro la cedula del empleado'''

    def buscar_empleado(self, cedula_empleado):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        empleado = 'Empleado no encontrado'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Empleado):

                if (int(obj.ci) == cedula_empleado):

                    empleado = {"Cedula Empleado": obj.ci, "Nombre ": obj.nombre,
                                "Apellido ": obj.apellido, "Direccion ": obj.direccion}
        db.close()
        return empleado       

    '''Mètodo que permite buscar al cliente. Recibe como parametro la cedula del cliente'''

    def buscar_cliente(self, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        cliente = 'Cliente no encontrado'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente or str(obj.ruc) == cedula_cliente):

                    cliente = {"Nombre ": obj.nombre, "Apellido ": obj.apellido,
                               "Direccion ": obj.direccion}
        db.close()
        return cliente

    '''Mètodo que permite buscar al proveedor. Recibe como parametro el RUC del proveedor'''

    def buscar_proveedor(self, ruc_proveedor):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        proveedor = 'Proveedor no encontrado'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Proveedor):

                if (obj.ruc == ruc_proveedor):

                    proveedor = {"Nombre ": obj.nombre, "Direccion ": obj.direccion}
        db.close()
        return proveedor

    '''METODOS PARA BUSQUEDA, PARA LISTAR Y PARA GUARDAR LOS PRODUCTOS.
    CORRESPONDEN A LAS CLASES: Hamburguesa, Pizza, Papa_Frita, Lomito, 
    Bebida_Con_Alcohol y Bebida_Sin_Alcohol.

    Las busquedas se realizan mediante el codigo de cada producto. Este codigo es alfanumerico.'''

    def listar_hamburguesas(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        hamburguesas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Hamburguesa):

                hamburguesa = Hamburguesa(obj.codigo, obj.nombre, obj.precio, obj.grupo)
                hamburguesas.append(hamburguesa)

        db.close()
        return hamburguesas

    def listar_pizzas(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        pizzas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Pizza):

                pizza = Pizza(obj.codigo, obj.nombre, obj.precio, obj.sabor)
                pizzas.append(pizza)

        db.close()
        return pizzas

    def listar_papas_fritas(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        papas_fritas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, PapaFrita):

                papa_frita = PapaFrita(obj.codigo, obj.nombre, obj.precio, obj.tamanio)
                papas_fritas.append(papa_frita)

        db.close()
        return papas_fritas

    def listar_lomitos(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        lomitos = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Lomito):

                lomito = Lomito(obj.codigo, obj.nombre, obj.precio, obj.grupo)
                lomitos.append(lomito)

        db.close()
        return lomitos

    def listar_bebidas_alcoholicas(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        alcoholicas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, BebidaConAlcohol):

                con_alcohol = BebidaConAlcohol(obj.codigo, obj.ca_nombre, obj.ca_precio)
                alcoholicas.append(con_alcohol)

        db.close()
        return alcoholicas

    def listar_bebidas_no_alcoholicas(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        no_alcoholicas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, BebidaSinAlcohol):

                sin_alcohol = BebidaSinAlcohol(obj.codigo, obj.sa_nombre, obj.sa_precio)
                no_alcoholicas.append(sin_alcohol)

        db.close()
        return no_alcoholicas

    def buscar_hamburguesa(self, codigo_hamburguesa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        hamburguesa = 'No existe este producto'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Hamburguesa):

                if (obj.codigo == codigo_hamburguesa):

                    hamburguesa = {"Nombre ": obj.nombre, "Precio ": obj.precio,
                                   "Grupo ": obj.grupo}
        db.close()
        return hamburguesa

    def buscar_pizza(self, codigo_pizza):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        pizza = 'No existe este producto'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Pizza):

                if (obj.codigo == codigo_pizza):

                     pizza = {"Nombre ": obj.nombre, "Precio ": obj.precio,
                              "Grupo ": obj.sabor}
        db.close()
        return pizza

    def buscar_papas_fritas(self, codigo_papa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        papa_frita = 'No existe este producto'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, PapaFrita):

                if (obj.codigo == codigo_papa):

                    pizza = {"Nombre ": obj.nombre, "Precio ": obj.precio,
                             "Grupo ": obj.tamanio}

        db.close()
        return papa_frita

    def buscar_lomito(self, codigo_lomito):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        lomito = 'No existe este producto'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Lomito):

                if (obj.codigo == codigo_lomito):

                    lomito = {"Nombre ": obj.nombre, "Precio ": obj.precio, "Grupo ": obj.grupo}

        db.close()
        return lomito

    def guardar_hamburguesa(self, hamburguesa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[hamburguesa.codigo] = hamburguesa

        transaction.commit()
        db.close()

    def guardar_pizza(self, pizza):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[pizza.codigo] = pizza

        transaction.commit()
        db.close()

    def guardar_papa_frita(self, papa_frita):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[papa_frita.codigo] = papa_frita

        transaction.commit()
        db.close()

    def guardar_lomito(self, lomito):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[lomito.codigo] = lomito

        transaction.commit()
        db.close()

    def guardar_bebida_con_alcohol(self, con_alcohol):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[con_alcohol.codigo] = con_alcohol

        transaction.commit()
        db.close()

    def guardar_bebida_sin_alcohol(self, sin_alcohol):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[sin_alcohol.codigo] = sin_alcohol

        transaction.commit()
        db.close()

    def buscar_bebida_con_alcohol(self, codigo_ca):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        con_alcohol = 'Bebida no encontrada'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, BebidaConAlcohol):

                if (obj.codigo == codigo_ca):

                    con_alcohol = {"Nombre ": obj.ca_nombre, "Precio ": obj.ca_precio}

        db.close()
        return con_alcohol

    def buscar_bebida_sin_alcohol(self, codigo_sa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        sin_alcohol = 'Bebida no encontrada'

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, BebidaSinAlcohol):

                if (obj.codigo == codigo_sa):

                    sin_alcohol =  {"Nombre ": obj.sa_nombre, "Precio ": obj.sa_precio}

        db.close()
        return sin_alcohol

    '''METODOS PARA BUSCAR, LISTAR Y GUARDAR LOS DATOS DE NUESTRA EMPRESA.
    CORRESPONDE A LA CLASE: Restaurante.'''

    '''Metodo para guardar los datos de la empresa'''

    def listar_datos_empresa(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        empresas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Restaurante):

                empresa = Restaurante(obj.nombre, obj.ruc, obj.direccion, obj.numero_contacto, obj.email)
                empresas.append(empresa)

        db.close()
        return empresas

    '''Metodo que me permitira guardar los datos de la empresa que debemos crear'''

    def guardar_empresa(self, empresa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[empresa.ruc] = empresa

        transaction.commit()
        db.close()

    '''Metodo de busqueda que nos permitira buscar los datos de la empresa si lo necesitasemos.'''
    def buscar_empresa(self, ruc_empresa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        empresa = 'empresa no encontrada'

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Restaurante):

                if (obj.ruc == ruc_empresa):

                    empresa = {obj.nombre, obj.ruc, obj.direccion,
                               obj.numero_contacto, obj.email}

        db.close()
        return empresa

    '''METODOS PARA GUARDAR, LISTAR Y BUSCAR LAS FACTURAS.'''

    '''Metodo que me permitirà listar las facturas en el sistema'''

    def listar_facturas(self):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        facturas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, FacturaConNombre):

                factura = FacturaConNombre(obj.fecha_emision, obj.ruc_ci, obj.razon_social,
                                           obj.direccion, obj.total_por_producto, obj.total_factura,
                                           obj.numero_factura, obj.timbrado)
                facturas.append(factura)

        db.close()
        return facturas

    '''Metodo que me permitira guardar la factura en el sistema'''
    def guardar_factura(self, factura):
        
        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        dbroot[factura.ruc_ci] = factura

        transaction.commit()
        db.close()

    '''Metodo que nos permitira buscra las facturas en el sistema, sean estas emitidas con nombre o sin nombre'''

    def buscar_facturas(self, ruc_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        factura = 'Factura no emitida'
        
        try:

            for key in dbroot.keys():

                obj = dbroot[key]

                if isinstance(obj, FacturaConNombre):

                    if (int(obj.ruc_cliente) == ruc_cliente):

                        factura =  {"Razon Social ": obj.razon_social,
                                    "Fecha de Emision ": obj.fecha_emision}

            db.close()
            return factura

        except Exception as e:

            raise Exception(factura)

    '''En esta seccion de nuestro modelo definiremos los metodos que nos permitiran
    obtener todos los datos que vayamos precisando a la hora de generar nuestra factura a los
    clientes. 
    Aqui buscaremos cada uno de los datos que vayamos precisando a la hora de ejecutar nuestro
    programa.'''

    def obtener_nombre_cliente(self, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente):

                    cliente = {obj.nombre}
        db.close()
        return cliente

    def obtener_apellido_cliente(self, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente):

                    cliente = {obj.apellido}
        db.close()
        return cliente

    def obtener_ci_cliente(self, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente):

                    cliente = {obj.ci}
        db.close()
        return cliente

    def obtener_ruc_cliente(self, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente):

                    cliente = {obj.ruc}
        db.close()
        return cliente

    def obtener_direccion_cliente(self, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente):

                    cliente = {obj.direccion}
        db.close()
        return cliente

    '''Los siguientes metodos nos van a servir para poder obtener los precios y descripciones 
    de los productos de nuestra base de datos'''

    '''Para obtener el precio unitario, nombre y grupo de la hamburguesa. Estos nos serviran a la hora de generar 
    nuestra factura con nombre y sin nombre.
    En la factura se visualizara de la siguiente manera:

    CANTIDAD   DESCRIPCION          PRECIO UNITARIO   TOTAL

       2       Hamburguesa, Simple     10000          20000

    DESCRIPCION: Veinte mil guaranies.          TOTAL A PAGAR: 20000

    Esta seria la visualizacion para todos los productos.'''

    def obtener_precio_hamburguesa(self, codigo_hamburguesa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Hamburguesa):

                if (obj.codigo == codigo_hamburguesa):

                    hamburguesa = int(obj.precio)
        db.close()
        return hamburguesa

    def obtener_nombre_hamburguesa(self, codigo_hamburguesa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Hamburguesa):

                if (obj.codigo == codigo_hamburguesa):

                    hamburguesa = obj.nombre
        db.close()
        return hamburguesa

    def obtener_grupo_hamburguesa(self, codigo_hamburguesa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Hamburguesa):

                if (obj.codigo == codigo_hamburguesa):

                    hamburguesa = obj.grupo
        db.close()
        return hamburguesa

    '''Metodo para obtener nombre, sabor y precio unitario de la pizza.'''

    def obtener_nombre_pizza(self, codigo_pizza):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Pizza):

                if (obj.codigo == codigo_pizza):

                     pizza = obj.nombre
        db.close()
        return pizza

    def obtener_sabor_pizza(self, codigo_pizza):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Pizza):

                if (obj.codigo == codigo_pizza):

                     pizza = obj.sabor
        db.close()
        return pizza

    def obtener_precio_pizza(self, codigo_pizza):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Pizza):

                if (obj.codigo == codigo_pizza):

                     pizza = int(obj.precio)
        db.close()
        return pizza

    '''Para las papas fritas'''

    def obtener_nombre_papa_frita(self, codigo_papa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, PapaFrita):

                if (obj.codigo == codigo_papa):

                    papa_frita = obj.nombre

        db.close()
        return papa_frita

    def obtener_tamanio_papa_frita(self, codigo_papa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, PapaFrita):

                if (obj.codigo == codigo_papa):

                    papa_frita = obj.tamanio

        db.close()
        return papa_frita

    def obtener_precio_papa_frita(self, codigo_papa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, PapaFrita):

                if (obj.codigo == codigo_papa):

                    papa_frita = int(obj.precio)

        db.close()
        return papa_frita

    '''Para los lomitos.'''

    def obtener_precio_lomito(self, codigo_lomito):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Lomito):

                if (obj.codigo == codigo_lomito):

                    lomito = int(obj.precio)

        db.close()
        return lomito

    def obtener_nombre_lomito(self, codigo_lomito):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Lomito):

                if (obj.codigo == codigo_lomito):

                    lomito = obj.nombre

        db.close()
        return lomito

    def obtener_grupo_lomito(self, codigo_lomito):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, Lomito):

                if (obj.codigo == codigo_lomito):

                    lomito = obj.nombre

        db.close()
        return lomito

    '''Para las bebidas con alcohol'''

    def obtener_nombre_bebida_con_alcohol(self, codigo_ca):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, BebidaConAlcohol):

                if (obj.codigo == codigo_ca):

                    con_alcohol = obj.ca_nombre

        db.close()
        return con_alcohol

    def obtener_nombre_bebida_con_alcohol(self, codigo_ca):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, BebidaConAlcohol):

                if (obj.codigo == codigo_ca):

                    con_alcohol = int(obj.ca_precio)

        db.close()
        return con_alcohol

    '''Para las bebidas sin alcohol'''

    def obtener_nombre_bebida_sin_alcohol(self, codigo_sa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, BebidaSinAlcohol):

                if (obj.codigo == codigo_sa):

                    sin_alcohol =  obj.sa_nombre

        db.close()
        return sin_alcohol

    def obtener_precio_bebida_sin_alcohol(self, codigo_sa):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]

            if isinstance(obj, BebidaSinAlcohol):

                if (obj.codigo == codigo_sa):

                    sin_alcohol =  int(obj.sa_precio)

        db.close()
        return sin_alcohol

    '''Metodos para inicializar los valores de la factura'''
 
    '''Metodo que me permitira obtener la fecha del dia en que se emitio la factura'''

    def obtener_fecha_emision(self):

        fecha_emision = datetime.now()

        formateo_fecha_emision = fecha_emision.strftime('%d/%m/%Y')

        return formateo_fecha_emision

    '''Metodo que retorna el timbrado actual de la factura'''

    def obtener_timbrado(self):

        timbrado = '12352618'

        return timbrado

    def obtener_numero_factura(self):

        contador = 0

        contador = contador + 1

        return contador

    '''Metodo para limpiar la pantalla de nuestra terminal'''
    @staticmethod
    def clear_screen(self):

        time.sleep(3)

        if(platform == 'Windows'):

            os.system('cls')

        else:

            os.system('clear')

    '''Metodo para salir del menu de nuestro programa'''
    
    @staticmethod
    def project_exit(self):

       sys.exit()

    '''Metodo que va permitir modificar el precio del producto.'''

    #Para modificar el precio de la hamburguesa
    def modificar_precio_hamburguesa(self, codigo_hamburguesa, nuevo_precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Hamburguesa):

                if(obj.codigo == codigo_hamburguesa):

                    precio_hamburguesa = obj.precio
                    auxiliar = nuevo_precio
                    obj.precio = auxiliar
        
        transaction.commit()
        db.close()

    #Para modificar el precio del lomito.

    def modificar_precio_lomito(self, codigo_lomito, nuevo_precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Lomito):

                if(obj.codigo == codigo_lomito):

                    precio_lomito = obj.precio
                    auxiliar = nuevo_precio
                    obj.precio = auxiliar
        
        transaction.commit()
        db.close()

    #Para modificar el precio de la pizza.

    def modificar_precio_pizza(self, codigo_pizza, nuevo_precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Lomito):

                if(obj.codigo == codigo_pizza):

                    precio_pizza = obj.precio
                    auxiliar = nuevo_precio
                    obj.precio = auxiliar
        
        transaction.commit()
        db.close()

    #Para modificar el precio de la papa frita.

    def modificar_precio_papa_frita(self, codigo_papa_frita, nuevo_precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, PapaFrita):

                if(obj.codigo == codigo_papa_frita):

                    precio_papa_frita = obj.precio
                    auxiliar = nuevo_precio
                    obj.precio = auxiliar
        
        transaction.commit()
        db.close()

    #Para modificar el precio de la bebida alcoholica.

    def modificar_precio_bebida_con_alcohol(self, codigo_alcohol, nuevo_precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, BebidaConAlcohol):

                if(obj.codigo == codigo_alcohol):

                    precio_bebida_alcoholica = obj.ca_precio
                    auxiliar = nuevo_precio
                    obj.ca_precio = auxiliar
        
        transaction.commit()
        db.close()

    #Para modificar el precio de la bebida alcoholica.

    def modificar_precio_bebida_sin_alcohol(self, codigo_sin_alcohol, nuevo_precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, BebidaSinAlcohol):

                if(obj.codigo == codigo_sin_alcohol):

                    precio_bebida_sin_alcohol = obj.sa_precio
                    auxiliar = nuevo_precio
                    obj.sa_precio = auxiliar
        
        transaction.commit()
        db.close()

    '''Metodo que me permite modificar el numero de contacto, direccion y tambien email del cliente'''

    #Para modificar el numero de contacto.

    def modificar_numero_cliente(self, cedula_cliente, nuevo_contacto):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if(int(obj.cedula) == cedula_cliente):

                    cliente_numero = obj.numero_contacto
                    auxiliar = nuevo_contacto
                    obj.numero_contacto = nuevo_contacto

        transaction.commit()
        db.close()

    #Para modificar la direccion email del cliente.

    def modificar_mail_cliente(self, cedula_cliente, nuevo_mail):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Cliente):
                if(int(obj.cedula) == cedula_cliente):
                    obj.email = nuevo_mail

        transaction.commit()
        db.close()

    #Para modificar la direccion de domicilio del cliente.

    def modificar_direccion_cliente(self, cedula_cliente, nueva_direccion):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if(int(obj.cedula) == cedula_cliente):
                    obj.direccion = nueva_direccion

        transaction.commit()
        db.close()

    '''Metodo para modificar contraseña del empleado, numero de contacto, email y direccion de domiciolio'''

    #Para modificar direccion del domicilio del empleado.

    def modificar_direccion_empleado(self, cedula_empleado, nueva_direccion):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Empleado):
                if(int(obj.cedula) == cedula_empleado):
                    obj.direccion = nueva_direccion
        transaction.commit()
        db.close()

    #Para modificar mail del empleado

    def modificar_mail_empleado(self, cedula_empleado, nuevo_mail):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Empleado):

                if(int(obj.cedula) == cedula_empleado):
                    obj.email = nuevo_mail

        transaction.commit()
        db.close()

    #Para modificar contacto del empleado.

    def modificar_numero_empleado(self, cedula_empleado, nuevo_contacto):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():
            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Empleado):

                if (int(obj.cedula) == cedula_empleado):

                    obj.numero_contacto = nuevo_contacto

        transaction.commit()
        db.close()

    #Para modificar contraseña del usuario.

    def modificar_contrasenia_empleado(self, cedula_empleado, nueva_contrasenia):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():
            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Empleado):
                if int(obj.cedula) == cedula_empleado:

                    obj.contrasenia = nueva_contrasenia

        transaction.commit()
        db.close()

    '''def cargar_factura(self, formateo_fecha_emision, ruc_ci, razon_social, direccion,
        total_por_producto, total_fatura, contador, timbrado, cantidad, precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        facturas_emitidas = []

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, FacturaConNombre) and isinstance(obj, Empleado)
                and'''

    '''Metodo que recibe dos parametros que son: cantidad y precio. Donde cantidad
    es la cantidad de cada producto que pide el cliente y precio es el precio del 
    producto que elige el cliente'''

    @staticmethod
    def total_por_producto(self, cantidad, precio):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        total = (lambda cantidad, precio : cantidad*precio) #funcion lambda para el calculo de total
        totales_por_producto = []

        cantidades_precios = []
        cantidades_precios.append((cantidad, precio))

        for cp in cantidades_precios:

            cantidad = cp[0]
            precio = cp[1]

            total_producto = total(cantidad, precio)

            totales_por_producto.append(total_producto)

        return totales_por_producto

    '''Metodo que recibe como parametro la lista de los totales por produicto
    y suma cada elemento de la lista para obtener el monto total de la factura'''

    @staticmethod
    def total_factura(self, totales_por_producto):
        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        monto_factura = sum(totales_por_producto)

        return monto_factura

    '''Metodo para validar ingreso al sistema'''
    @staticmethod
    def validar_ingreso(*args, user, password):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]
            if isinstance(obj, Empleado):

                if (obj.usuario) == user and (obj.contrasenia) == password:

                    return True
                else:

                    return False

    @staticmethod
    def validar_existencia_cliente(*args, cedula_cliente):

        db = MiZODB('./Data.fs')
        dbroot = db.raiz

        cliente = 'Cliente no encontrado'

        for key in dbroot.keys():

            obj = dbroot[key]
            obj = dbroot[key]

            if isinstance(obj, Cliente):

                if (int(obj.ci) == cedula_cliente or str(obj.ruc) == cedula_cliente):

                    cliente = True
        db.close()
        return cliente
