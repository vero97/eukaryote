from Persona import Cliente
from Persona import Empleado
from Proveedor import Proveedor
from Producto import *
from Empresa import Restaurante
from Comprobante import FacturaConNombre
#from Comprobante import FacturaSinNombre
#from Tarjeta import TarjetaCredito

''''''
class Vista():

    def vista_agregar_cliente(self):

        print("Crear Cliente")

        ruc = input('Ingrese numero de RUC:\t')
        ci = int(input('Ingrese numero de cedula:\t'))
        nombre = input('Ingrese nombre del Cliente:\t')
        apellido = input('Ingrese apellido del Cliente:\t')
        direccion = input('Ingrese direccion del Cliente:\t')
        numero_contacto = input('Ingrese un numero de contacto del Cliente:\t')
        email = input('Ingrese una direccion de email:\t')

        nuevo_cliente = Cliente(ruc, ci, nombre, apellido, direccion, numero_contacto, email)

        return nuevo_cliente

    def vista_agregar_empleado(self):

        print("Crear Empleado")

        ci = input('Ingrese numero de cedula:\t')
        nombre = input('Ingrese nombre del empleado:\t')
        apellido = input('Ingrese apellido del empleado:\t')
        direccion = input('Ingrese direccion del empleado:\t')
        fecha_nacimiento = input('Ingrese fecha de nacimiento:\t')
        usuario = input('Defina un usuario para el empleado:\t')
        contrasenia = input('Ingrese una contraseña temporal para el empleado:\t')
        numero_contacto = input('Ingrese un numero de contacto:\t')
        email = input('Ingrese una direccion de mail para el empleado:\t')

        nuevo_empleado = Empleado(ci, nombre, apellido, direccion, fecha_nacimiento, 
            usuario, contrasenia, numero_contacto, email)
        return nuevo_empleado

    def vista_agregar_proveedor(self):

        print('Crear proveedor')

        ruc = input('Ingrese ruc del proveedor:\t')
        nombre = input('Ingrese nombre del proveedor:\t')
        direccion = input('Ingrese direccion del proveedor:\t')
        numero_contacto = input('Ingrese numero de contacto del proveedor:\t')
        email = input('Ingrese una direccion de correo del proveedor:\t')

        nuevo_proveedor = Proveedor(ruc, nombre, direccion, numero_contacto, email)

        return nuevo_proveedor

    def vista_listar_empleados(self, empleados):

        print("Listado de personas en la base de datos \n")

        if empleados:

            for empleado in empleados:

                print('Nombre: ' + empleado.nombre, 'Apellido: '+ empleado.apellido, empleado.contrasenia)

    def vista_leer_ci_empleado(self):

        print('Ingrese el nùmero de cedula que desea buscar')
        cedula_empleado = input()
        return int(cedula_empleado)

    def imprimir_empleado(self, resultado_empleado):

        print('El empleado encontrado es : ', format(resultado_empleado))

    def vista_listar_clientes(self, clientes):

        print('Listado de clientes en la base de datos: \n')

        if clientes:

            for cliente in clientes:

                print('Nombre: ' + cliente.nombre, 'Apellido: '+ cliente.apellido,
                      'Numero de contacto: ' +
                      cliente.numero_contacto, 'Email: ' + cliente.email)

    def vista_leer_ci_cliente(self):

        print('Ingrese cedula del cliente que desea buscar:')
        cedula_cliente = input()

        return int(cedula_cliente)

    def imprimir_cliente(self, resultado_cliente):

        print('El cliente encontrado es : ', format(resultado_cliente))

    def vista_listar_proveedores(self, proveedores):

        print('Listado de proveedores: \n')

        if proveedores:

            for proveedor in proveedores:

                print('Nombre: ' + proveedor.nombre, 'RUC: '+ proveedor.ruc,
                      'Telefono: ' + proveedor.numero_contacto)

    def vista_leer_ruc_proveedor(self):

        print('Ingrese RUC del proveedor que desea buscar')
        ruc_proveedor = input()

        return str(ruc_proveedor)

    def imprimir_proveedor(self, resultado_proveedor):

        print('El proveedor es: ', format(resultado_proveedor))

    '''Agregaremos las hamburguesas a nuestra base de datos mediante estos metodos.
    Listaremos las hamburguesas de nuestra base de datos.
    En caso de querer buscar los datos de una hamburguesa especifica, debemos ingresar 
    el codigo de la hamburguesa, luego, se imprimira nuestra busqueda.'''

    def vista_agregar_hamburguesa(self):

        print('Ingrese las hamburguesas a la base de datos. \n')

        codigo = input('Ingrese el codigo para la hamburguesa:\t')
        nombre = input('Ingrese una descripcion de la hamburguesa:\t')
        precio = int(input('Ingrese el precio para la hamburguesa:\t'))
        grupo = input('Ingrese grupo de la hamburguesa:\t')

        nueva_hamburguesa = Hamburguesa(codigo, nombre, precio, grupo)

        return nueva_hamburguesa

    def vista_listar_hamburguesas(self, hamburguesas):

        print("Listado de hamburguesas en el negocio: \n")

        if hamburguesas:

            for hamburguesa in hamburguesas:

                print('Nombre: ' + hamburguesa.nombre, 'Precio: '+ str(hamburguesa.precio), 'Grupo: '+ hamburguesa.grupo)

    def vista_leer_codigo_hamburguesa(self):

        print('Ingrese codigo de la hamburguesa que desea agregar al pedido, o simplemente buscar')
        codigo_hamburguesa = input()

        return str(codigo_hamburguesa)

    def imprimir_hamburguesa(self, resultado_hamburguesa):

        print('La hamburguesa es : ', format(resultado_hamburguesa))

    '''Agregaremos las pizzas a nuestra base de datos mediante estos metodos.
    Listaremos las pizzas de nuestra base de datos.
    En caso de querer buscar los datos de una pizza especifica, debemos ingresar 
    el codigo de la pizza, luego, se imprimira nuestra busqueda.'''

    def vista_agregar_pizza(self):

        print('Ingrese las pizzas a la base de datos. \n')

        codigo = input('Ingrese el codigo para la pizza:\t')
        nombre = input('Ingrese una descripcion de la pizza:\t')
        precio = int(input('Ingrese el precio para la pizza:\t'))
        sabor = input('Ingrese sabor de la pizza:\t')

        nueva_pizza = Pizza(codigo, nombre, precio, sabor)

        return nueva_pizza

    def vista_listar_pizzas(self, pizzas):

        print("Listado de pizzas en el negocio: \n")

        if pizzas:

            for pizza in pizzas:

                print('Nombre: ' + pizza.nombre, 'Precio: ',pizza.precio,
                      'Sabor: '+ pizza.sabor)

    def vista_leer_codigo_pizza(self):

        print('Ingrese codigo de la pizza que desea agregar al pedido, o simplemente buscar')
        codigo_pizza = input()

        return str(codigo_pizza)

    def imprimir_pizza(self, resultado_pizza):

        print('La pizza es: ', format(resultado_pizza))

    '''Agregaremos las papas fritas a nuestra base de datos mediante estos metodos.
    Listaremos las papas fritas de nuestra base de datos.
    En caso de querer buscar los datos de una papa frita especifica, debemos ingresar 
    el codigo de la papa frita, luego, se imprimira nuestra busqueda.'''

    def vista_agregar_papas_fritas(self):

        print('Ingrese las papas fritas a la base de datos. \n')

        codigo = input('Ingrese el codigo para la papa frita:\t')
        nombre = input('Ingrese una descripcion de la papa frita:\t')
        precio = int(input('Ingrese el precio para la papa frita:\t'))
        tamanio = input('Ingrese tamaño de la papa frita:\t')

        nueva_papa_frita = PapaFrita(codigo, nombre, precio, tamanio)

        return nueva_papa_frita

    def vista_listar_papas_fritas(self, papas_fritas):

        print("Listado de papas fritas en el negocio: \n")

        if papas_fritas:

            for papa_frita in papas_fritas:

                print('Nombre: ' + papa_frita.nombre, 'Precio: ', papa_frita.precio, 'Tamaño: '+ papa_frita.tamanio)

    def vista_leer_codigo_papa_frita(self):

        print('Ingrese codigo de la papa frita que desea agregar al pedido, o simplemente buscar')
        codigo_papa_frita = input()

        return str(codigo_papa_frita)

    def imprimir_papa_frita(self, resultado_papa_frita):

        print('La papa frita es: ', format(resultado_papa_frita))

    '''Agregaremos los lomitos a nuestra base de datos mediante estos metodos.
    Listaremos los lomitos de nuestra base de datos.
    En caso de querer buscar los datos de un lomito especifico, debemos ingresar 
    el codigo de la lomito, luego, se imprimira nuestra busqueda.'''

    def vista_agregar_lomitos(self):

        print('Ingrese los lomitos a la base de datos. \n')

        codigo = input('Ingrese el codigo para el lomito:\t')
        nombre = input('Ingrese una descripcion del lomito:\t')
        precio = int(input('Ingrese el precio del lomito:\t'))
        grupo = input('Ingrese un grupo:\t')

        nuevo_lomito = Lomito(codigo, nombre, precio, grupo)

        return nuevo_lomito

    def vista_listar_lomitos(self, lomitos):

        print("Listado de lomitos en el negocio: \n")

        if lomitos:

            for lomito in lomitos:

                print('Nombre: ' + lomito.nombre, 'Precio: ', lomito.precio, 'Grupo: '+ lomito.grupo)

    def vista_leer_codigo_lomito(self):

        print('Ingrese codigo de la papa frita que desea agregar al pedido, o simplemente buscar')
        codigo_lomito = input()

        return str(codigo_lomito)

    def imprimir_lomito(self, resultado_lomito):

        print('El lomito es: ', format(resultado_lomito))

    '''Agregaremos las bebidas con alcohol a nuestra base de datos mediante estos metodos.
    Listaremos las bebidas con alcohol base de datos.
    En caso de querer buscar los datos de una bebida especifica, debemos ingresar 
    el codigo de la bebida cpn alcohol, luego, se imprimira nuestra busqueda.'''

    def vista_agregar_bebida_con_alcohol(self):

        print('Ingrese las bebidas con alcohol a la base de datos. \n')

        codigo = input('Ingrese el codigo para la bebida:\t')
        ca_nombre = input('Ingrese nombre de la bebida:\t')
        ca_precio = int(input('Ingrese el precio:\t'))

        nuevo_con_alcohol = BebidaConAlcohol(codigo, ca_nombre, ca_precio)

        return nuevo_con_alcohol

    def vista_listar_bebibas_con_alcohol(self, alcoholicas):

        print("Listado de lomitos en el negocio: \n")

        if alcoholicas:

            for con_alcohol in alcoholicas:

                print('Nombre: ' + con_alcohol.ca_nombre, 'Precio: ', con_alcohol.ca_precio)

    def vista_leer_codigo_ca(self):

        print('Ingrese codigo de la bebida, o simplemente buscar')
        codigo_ca = input()

        return str(codigo_ca)

    def imprimir_con_alcohol(self, resultado_ca):

        print('La bebida es: ', format(resultado_ca))

    '''Agregaremos las bebidas sin alcohol a nuestra base de datos mediante estos metodos.
    Listaremos las bebidas sin alcohol base de datos.
    En caso de querer buscar los datos de una bebida especifica, debemos ingresar 
    el codigo de la bebida cpn alcohol, luego, se imprimira nuestra busqueda.'''

    def vista_agregar_bebida_sin_alcohol(self):

        print('Ingrese las bebidas sin alcohol a la base de datos. \n')

        codigo = input('Ingrese el codigo para la bebida:\t')
        sa_nombre = input('Ingrese nombre de la bebida:\t')
        sa_precio = int(input('Ingrese el precio:\t'))

        nuevo_sin_alcohol = BebidaSinAlcohol(codigo, sa_nombre, sa_precio)

        return nuevo_sin_alcohol

    def vista_listar_bebidas_sin_alcohol(self, no_alcoholicas):

        print("Listado de lomitos en el negocio: \n")

        if no_alcoholicas:

            for sin_alcohol in no_alcoholicas:

                print('Nombre: ' + sin_alcohol.sa_nombre, 'Precio: ', sin_alcohol.sa_precio)

    def vista_leer_codigo_sa(self):

        print('Ingrese codigo de la bebida, o simplemente buscar')
        codigo_sa = input()

        return str(codigo_sa)

    def imprimir_sin_alcohol(self, resultado_sa):

        print('La bebida es: ', format(resultado_sa))

    '''Metodos vista_opciones_X (X representa las diferentes opciones que utilizaremos mas adelante.
    Se definen estos metodos ya que nos serviran a la hora de que el usuario lo utilice a la hora de:
    agregar, buscar, listar, etc. los productos, clientes, etc.'''

    def vista_opciones_productos(self):

        print('Opcion 1: Cargar nueva variedad de hamburguesa')
        print('Opcion 2: Cargar nueva variedad de pizza')
        print('Opcion 3: Cargar nueva variedad de papas fritas')
        print('Opcion 4: Cargar nueva variedad de lomito')
        print('Opcion 5: Cargar nueva variedad de bebida con alcohol')
        print('Opcion 6: Cargar nueva variedad de bebida sin alcohol')

        opcion = int(input('INGRESE OPCION PARA AGREGAR NUEVOS PRODUCTOS A LA BASE DE DATOS:\t'))

        return opcion

    def vista_opciones_personas_proveedores(self):

        print('Opcion 1: Cargar nuevo Empleado')
        print('Opcion 2: Cargar nuevo Cliente')
        print('Opcion 3: Cargar nuevo Proveedor')

        opcion = int(input('INGRESE OPCION PARA AGREGAR NUEVAS PERSONAS Y PROVEEDORES:\t'))

        return opcion

    def vista_opciones_busqueda_personas_proveedores(self):

        print('Opcion 1: Buscar  Empleado')
        print('Opcion 2: Buscar  Cliente')
        print('Opcion 3: Buscar  Proveedor')

        opcion = int(input('INGRESE OPCION PARA BUSCAR PERSONAS Y PROVEEDORES:\t'))

        return opcion

    def vista_opciones_listar_personas_proveedores(self):

        print('Opcion 1: Listar  Empleado')
        print('Opcion 2: Listar  Cliente')
        print('Opcion 3: Listar  Proveedor')

        opcion = int(input('INGRESE OPCION PARA LISTAR PERSONAS Y PROVEEDORES EN LA BASE DE DATOS:\t'))

        return opcion

    def vista_opciones_buscar_producto(self):

        print('Opcion 1: Buscar hamburguesa')
        print('Opcion 2: Buscar pizza')
        print('Opcion 3: Buscar papas fritas')
        print('Opcion 4: Buscar lomito')
        print('Opcion 5: Buscar bebida con alcohol')
        print('Opcion 6: Buscar bebida sin alcohol')

        opcion = int(input('INGRESE OPCION PARA BUSCAR PRODUCTOS DE LA BASE DE DATOS:\t'))

        return opcion

    def vista_opciones_listar_productos(self):

        print('Opcion 1: Listar hamburguesa')
        print('Opcion 2: Listar pizza')
        print('Opcion 3: Listar papas fritas')
        print('Opcion 4: Listar lomito')
        print('Opcion 5: Listar bebida con alcohol')
        print('Opcion 6: Listar bebida sin alcohol')

        try:

            opcion = int(input('INGRESE OPCION PARA BUSCAR PRODUCTOS DE LA BASE DE DATOS:\t'))

        except ValueError:

            raise

        else:

            return opcion


    '''Metodo que nos sirve para guardar los datos de uestra empresa..'''

    def vista_agregar_datos_empresa(self):

        print('Inicializaremos las informaciones de nuestra empresa')

        nombre = input('Ingrese el nombre de su empresa')
        ruc = input('Ingrese el ruc de su empresa')
        direccion = input('Ingrese la direccion de su empresa')
        numero_contacto = input('Ingrese el contato de su empresa')
        email = input('Ingrese el email de su empresa')

        nueva_empresa = Restaurante(nombre, ruc, direccion, numero_contacto, email)

        return nueva_empresa

    def vista_leer_ruc_de_empresa(self):

        ruc_empresa = input('Ingresa el ruc de tu empresa')

        return ruc_empresa

    def imprimir_empresa(self, resultado_empresa):

        print('Estos son los datos de mi empresa: ' + format(resultado_empresa))

    '''Metodos para instanciar los datos de la factura. Esto nos va permitir guardar la factura emitida.

    Sea esta con o sin nombre.'''

    def vista_agregar_datos_factura_con_nombre(self, fecha_emision, ruc_ci, razon_social,
                                               direccion, total_producto, total_factura,
                                               numero_factura, timbrado):

        fecha_emision = fecha_emision
        ruc_ci = ruc_ci
        razon_social = razon_social
        direccion = direccion
        total_producto = total_producto
        total_factura = total_factura
        numero_factura = numero_factura
        timbrado = timbrado

        nueva_factura = FacturaConNombre(fecha_emision, ruc_ci, razon_social, direccion, total_producto, total_factura, numero_factura, timbrado)

        return nueva_factura

    '''Listar facturas emitidas'''

    def vista_listar_facturas(self, facturas):

        if facturas:

            for factura in facturas:

                print('Fecha de Emision:' + str(factura.fecha_emision), 'Emitida a la razon social: ' + str(fatura.razon_social))

    '''Busqueda de factura por ruc del cliente'''

    def vista_leer_ruc_cliente(self):

        try:

            ruc_cliente = input('Ingrese su ruc')

        except Exception as e:

            raise Exception('Ha ocurrido una excepcion.' +str(e))

        return ruc_cliente

    def imprimir_factura_emitida(self, res):

        print('La factura es: ' + str(res))


    '''Este metodo nos darà la posibilidad de elegir si la factura que debemos 
    emitir va ser con o sin nombre.'''

    def vista_opcion_factura(self):

        opcion_factura = int(input('Ingrese 1 si desea factura con nombre, y 2 si desea factura sin nombre'))

        return opcion_factura

    '''Metodo que permitira al usuario ingresar la opcion de lo que necesita cargar en el 
    pedido. '''
    def vista_obtener_precios_productos(self):

        print('Opcion 1: Hamburguesa')
        print('Opcion 2: Pizza')
        print('Opcion 3: Papas Fritas')
        print('Opcion 4: Lomito')
        print('Opcion 5: Bebida con alcohol')
        print('Opcion 6: Bebida sin alcohol')

        opcion = int(input('Ingrese opcion para agregar a su pedido:\t'))

        return opcion

    '''Metodo que permite ingresar la cantidad de productos'''

    def vista_ingresar_cantidad_productos(self):

        cantidad = int(input(print('Ingrese la cantidad del producto:\t')))

        return int(cantidad)

    '''Metodo que nos va permitir agregar mas de una opcion de producto para el cliente.
    Actualmemte se define el bloque try/except para que lance una excepcion si es que se desea. Se define
    esa excepcion por que aun no tenemos lito este bloque para su completa implementacion. Nos dira que no es posible agrear el producto.
    Y que debemos ingresar solo N para imprimir nuestra factura.'''
    def vista_agregar_otros_productos(self):

        try:

            respuesta_sistema = str(input('Ingrese una S si de sea agregra otro pedido, '
                                          'o una N si desea imprimir su factura'))

        except Exception as e:

             print('No es posible que agreguemos otro pedido. Por el momento '
                   'no està disponible.'+ str(e))

        return respuesta_sistema

    '''Metodo que debe imprimir los datos del cliente en la factura sea esta con o sin nombre.

    Recibe los parametros: ruc, nombre, apellido, direccion que son propios del cliente, 
    fecha de emision, timbrado que son propos de la factura descripcion 1 y 2, 
    que seran concatenados para obtener la descripcion a mostrar en la factura, 
    precio unitario total que son del producto
    y pagar que es el total para pagar de la factura.'''

    def imprimir_datos_para_factura(self, ruc_ci, nombre, apellido, direccion,
                                    fecha_emision, timbrado, cant_producto,
                                    descripcion1, descripcion2, precio_unitario, total, pagar):

        print('--------------------------------------------------------------------------------')
        print('RESTAURANTE DE COMIDAS RAPIDAS "TIA EMI"')
        print('1234567 - 8')
        print('Manzana 1 Lote 1. Pindolo - Aregua') 
        print('0981 - 816 - 543')
        print('tiaefastfood@gmail.com')
        print('--------------------------------------------------------------------------------')

        print('--------------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------------')

        print('RUC/CI: ' +str(ruc_ci))
        print('NOMBRE O RAZON SOCIAL: ' +str(nombre) +' ' +str(apellido))
        print('DIRECCION: ' + str(direccion))
        print('--------------------------------------------------------------------------------')
        print('Fecha de Emision: ' + str(fecha_emision) +'    '+ 'Timbrado Nº: ' + str(timbrado))
        print('--------------------------------------------------------------------------------')

        print('--------------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------------')

        print('Cantidad Producto: ', cant_producto)
        print('Descripcion Producto: ' +str(descripcion1) + ' ' + str(descripcion2))
        print('Precio Unitario: ' +str(precio_unitario))
        print('Total Por Producto: ', total)
        print('total para pagar', pagar)

    '''Vista mensajes, nos servirà para nuestro menu principal'''

    def vista_mensajes(self):

        print('¿Què desea realizar?')
        print('Opcion 1: Agregar: clientes, empleados o proveedores')
        print('Opcion 2: Listar: clientes, empleados o proveedores')
        print('Opcion 3: Buscar: clientes, empleados o proveedores')
        print('Opcion 4: Agregar nuevos productos')
        print('Opcion 5: Listar productos')
        print('Opcion 6: Buscar productos')
        print('Opcion 7: Agregar pedidos del cliente')
        print('Opcion 8: Buscar facturas emitidas ')
        print('Opcion 9: Listar facturas emitidas')
        print('Opcion 10: SALIR')

        mi_opcion = int(input())

        return mi_opcion

    def mensaje_salida(self):

        x = int(input("Esta seguro de querer salir?. Para SALIR digite 1, "
                      "para CONTINUAR la ejecucion del programa digite 2 \t"))

        return x
