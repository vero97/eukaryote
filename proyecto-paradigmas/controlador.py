from modelo import Modelo
from vista import Vista

'''
Controlador: clase que nos permitira llamar a cada una de las funciones que ,vayamos a necesitar.
'''
class Controlador():

    def __init__(self):

        self.modelo = Modelo()
        self.vista = Vista()

    '''Este metodo no permitira agregar a los clientes, empleados y proveedores.'''

    def agregar_personas_proveedores(self):

        respuesta = self.vista.vista_opciones_personas_proveedores()

        if(respuesta == 1):

            empleado = self.vista.vista_agregar_empleado()
            self.modelo.guardar_empleado(empleado)

        elif(respuesta == 2):

            cliente = self.vista.vista_agregar_cliente()
            self.modelo.guardar_cliente(cliente)            

        elif(respuesta == 3):

            proveedor = self.vista.vista_agregar_proveedor()
            self.modelo.guardar_proveedor(proveedor)            

    '''Este metodo no permitira buscar a los clientes, empleados y proveedores.'''

    def buscar_personas_proveedores(self):

        respuesta = self.vista.vista_opciones_busqueda_personas_proveedores()

        if(respuesta == 1):

            cedula_empleado = self.vista.vista_leer_ci_empleado()
            resultado_empleado = self.modelo.buscar_empleado(cedula_empleado)
            self.vista.imprimir_empleado(resultado_empleado)

        elif(respuesta == 2):

            cedula_cliente = self.vista.vista_leer_ci_cliente()
            resultado_cliente = self.modelo.buscar_cliente(cedula_cliente)
            self.vista.imprimir_cliente(resultado_cliente)

        elif(respuesta == 3):

            ruc_proveedor = self.vista.vista_leer_ruc_proveedor()
            resultado_proveedor = self.modelo.buscar_proveedor(ruc_proveedor)
            self.vista.imprimir_proveedor(resultado_proveedor)

    '''Este metodo no permitira listar a los clientes, empleados y proveedores.'''

    def listar_personas_proveedores(self):

        respuesta = self.vista.vista_opciones_listar_personas_proveedores()

        if(respuesta == 1):

            empleados = self.modelo.listar_empleados()
            self.vista.vista_listar_empleados(empleados)            

        elif(respuesta == 2):

            clientes = self.modelo.listar_clientes()
            self.vista.vista_listar_clientes(clientes)

        elif(respuesta == 3):

            proveedores = self.modelo.listar_proveedores()
            self.vista.vista_listar_proveedores(proveedores)

    ''' Este bloque de codigo nos va permitir listar todos los productos de nuestra base de datos.'''

    def listar_productos(self):

        respuesta = self.vista.vista_opciones_listar_productos()

        if(respuesta == 1):

            hamburguesas = self.modelo.listar_hamburguesas()
            self.vista.vista_listar_hamburguesas(hamburguesas)

        elif(respuesta == 2):

            pizzas = self.modelo.listar_pizzas()
            self.vista.vista_listar_pizzas(pizzas)

        elif(respuesta == 3):

            papas_fritas = self.modelo.listar_papas_fritas()
            self.vista.vista_listar_papas_fritas(papas_fritas)

        elif(respuesta == 4):

            lomitos = self.modelo.listar_lomitos()
            self.vista.vista_listar_lomitos(lomitos)

        elif(respuesta == 5):

            alcoholicas = self.modelo.listar_bebidas_alcoholicas()
            self.vista.vista_listar_bebibas_con_alcohol(alcoholicas)

        elif(respuesta == 6):

            no_alcoholicas = self.modelo.listar_bebidas_no_alcoholicas()
            self.vista.vista_listar_bebidas_sin_alcohol(no_alcoholicas)

    '''En este bloque de codigo podremos buscar los productos de la base de datos, 
    debemos pasar el còdigo del producto que necesitamos y nos arrojara un resultado.'''

    def buscar_productos(self):

        respuesta = self.vista.vista_opciones_buscar_producto()

        if(respuesta == 1):

            codigo_hamburguesa = self.vista.vista_leer_codigo_hamburguesa()
            resultado_hamburguesa = self.modelo.buscar_hamburguesa(codigo_hamburguesa)
            self.vista.imprimir_hamburguesa(resultado_hamburguesa)

        elif(respuesta == 2):

            codigo_pizza = self.vista.vista_leer_codigo_pizza()
            resultado_pizza = self.modelo.buscar_pizza(codigo_pizza)
            self.vista.imprimir_pizza(resultado_pizza)

        elif(respuesta == 3):

            codigo_papa_frita = self.vista.vista_leer_codigo_papa_frita()
            resultado_papa_frita = self.modelo.buscar_papas_fritas(codigo_papa_frita)
            self.vista.imprimir_papa_frita(resultado_papa_frita)

        elif(respuesta == 4):

            codigo_lomito = self.vista.vista_leer_codigo_lomito()
            resultado_lomito = self.modelo.buscar_lomito(codigo_lomito)
            self.vista.imprimir_lomito(resultado_lomito)

        elif(respuesta == 5):

            codigo_ca = self.vista.vista_leer_codigo_ca()
            resultado_ca = self.modelo.buscar_bebida_con_alcohol(codigo_ca)
            self.vista.imprimir_con_alcohol(resultado_ca)

        elif(respuesta == 6):

            codigo_sa = self.vista.vista_leer_codigo_sa()
            resultado_sa = self.modelo.buscar_bebida_sin_alcohol(codigo_sa)
            self.vista.imprimir_sin_alcohol(resultado_sa) 

    '''Este bloque de codigo nos permitira agregar todos los productos a nuestra base de datos.'''

    def agregar_nuevos_productos(self):

        respuesta = self.vista.vista_opciones_productos()

        if(respuesta == 1):

            hamburguesa = self.vista.vista_agregar_hamburguesa()
            self.modelo.guardar_hamburguesa(hamburguesa)

        elif(respuesta == 2):

            pizza = self.vista.vista_agregar_pizza()
            self.modelo.guardar_pizza(pizza)

        elif(respuesta == 3):

            papa_frita = self.vista.vista_agregar_papas_fritas()
            self.modelo.guardar_papa_frita(papa_frita)

        elif(respuesta == 4):

            lomito = self.vista.vista_agregar_lomitos()
            self.modelo.guardar_lomito(lomito)

        elif(respuesta == 5):

            con_alcohol = self.vista.vista_agregar_bebida_con_alcohol()
            self.modelo.guardar_bebida_con_alcohol(con_alcohol)

        elif(respuesta == 6):

            sin_alcohol = self.vista.vista_agregar_bebida_sin_alcohol()
            self.modelo.guardar_bebida_sin_alcohol(sin_alcohol)           

    '''Metodo en el que agregaremos y guardaremos los datos de nuestra empresa'''

    def agregar_datos_empresa(self):

        empresa = self.vista.vista_agregar_datos_empresa()
        self.modelo.guardar_empresa(empresa)

    '''Metodo que nos permitirà buscar a nuestra empresa y nos retornara los datos de ella'''

    def buscar_mi_empresa(self):

        ruc_empresa = self.vista.vista_leer_ruc_de_empresa()
        resultado_empresa = self.modelo.buscar_empresa(ruc_empresa)
        self.vista.imprimir_empresa(resultado_empresa)

    '''
    - Descripcion del metodo:

    Metodo que me permitira cargar los datos de clientes en la factura.

    - En el  bloque de codigo try/except: Opcion S:

    Si deseamos agregar otro producto nos levantara una excepcion ya que el modulo no està
    disponible aun.

    La idea en este bloque es poder agregar mas productos en caso de que el cliente lo precise.

    Estuve probando varias maneras y aùn no lo puedo obtener.

    - Si la opcion  es N: nos va imprimir la factura para el cliente.
    '''

    def agregar_pedidos(self):

        opcion_factura = self.vista.vista_opcion_factura()

        if(opcion_factura == 1):

            cedula_cliente = self.vista.vista_leer_ci_cliente()
            ci_cliente = self.modelo.obtener_ci_cliente(cedula_cliente)
            ruc_cliente = self.modelo.obtener_ruc_cliente(cedula_cliente)
            nombre_cliente = self.modelo.obtener_nombre_cliente(cedula_cliente)
            apellido_cliente = self.modelo.obtener_apellido_cliente(cedula_cliente)
            direccion_cliente = self.modelo.obtener_direccion_cliente(cedula_cliente)
            fecha_emision = self.modelo.obtener_fecha_emision()
            timbrado = self.modelo.obtener_timbrado()
            numero_factura = self.modelo.obtener_numero_factura()

            respuesta = self.vista.vista_obtener_precios_productos()

            if(respuesta == 1):

                codigo = self.vista.vista_leer_codigo_hamburguesa()
                descripcion1 = self.modelo.obtener_nombre_hamburguesa(codigo)
                descripcion2 = self.modelo.obtener_grupo_hamburguesa(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                precio = self.modelo.obtener_precio_hamburguesa(codigo)
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 2):

                codigo = self.vista.vista_leer_codigo_pizza()
                precio = self.modelo.obtener_precio_pizza(codigo)
                descripcion1 = self.modelo.obtener_nombre_pizza(codigo)
                descripcion2 = self.modelo.obtener_sabor_pizza(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 3):

                codigo = self.vista.vista_leer_codigo_papa_frita()
                precio = self.modelo.obtener_precio_pizza(codigo)
                descripcion1 = self.modelo.obtener_nombre_papa_frita(codigo)
                descripcion2 = self.modelo.obtener_tamanio_papa_frita(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 4):

                codigo = self.vista.vista_leer_codigo_lomito()
                precio = self.modelo.obtener_precio_lomito(codigo)
                descripcion1 = self.modelo.obtener_nombre_lomito(codigo)
                descripcion2 = self.modelo.obtener_grupo_lomito(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 5):

                codigo = self.vista.vista_leer_codigo_ca()
                precio = self.modelo.obtener_precio_bebida_con_alcohol(codigo)
                descripcion1 = self.modelo.obtener_nombre_bebida_con_alcohol(codigo)
                descripcion2 = '.'
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 6):

                codigo = self.vista.vista_leer_codigo_ca()
                precio = self.modelo.obtener_precio_bebida_sin_alcohol(codigo)
                descripcion1 = self.modelo.obtener_nombre_bebida_sin_alcohol(codigo)
                descripcion2 = '.'           
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

                factura = self.vista.vista_agregar_datos_factura_con_nombre(fecha_emision, ruc_cliente, nombre_cliente,
                        direccion_cliente, total, total_factura, numero_factura, timbrado)
                self.modelo.guardar_factura(factura)

            try:

                respuesta_sistema = self.vista.vista_agregar_otros_productos()

                if(respuesta_sistema == 'S'):

                    raise Exception('No es posible agregar otro pedido a la misma factura')

            except Exception as e:

                raise Exception('NO es posible agregar.')

            else:

                if(respuesta_sistema == 'S'):

                    respuesta = self.vista.vista_obtener_precios_productos()

                    if(respuesta == 1):

                        codigo = self.vista.vista_leer_codigo_hamburguesa()
                        precio = self.modelo.obtener_precio_hamburguesa(codigo)
                        descripcion1 = self.modelo.obtener_nombre_hamburguesa(codigo)
                        descripcion2 = self.modelo.obtener_grupo_hamburguesa(codigo)
                        cantidad= self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 2):

                        codigo = self.vista.vista_leer_codigo_pizza()
                        precio = self.modelo.obtener_precio_pizza(codigo)
                        descripcion1 = self.modelo.obtener_nombre_pizza(codigo)
                        descripcion2 = self.modelo.obtener_sabor_pizza(codigo)
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 3):

                        codigo = self.vista.vista_leer_codigo_papa_frita()
                        precio = self.modelo.obtener_precio_pizza(codigo)
                        descripcion1 = self.modelo.obtener_nombre_papa_frita(codigo)
                        descripcion2 = self.modelo.obtener_tamanio_papa_frita(codigo)
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 4):

                        codigo = self.vista.vista_leer_codigo_lomito()
                        precio = self.modelo.obtener_precio_lomito(codigo)
                        descripcion1 = self.modelo.obtener_nombre_lomito(codigo)
                        descripcion2 = self.modelo.obtener_grupo_lomito(codigo)
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 5):

                        codigo = self.vista.vista_leer_codigo_ca()
                        precio = self.modelo.obtener_precio_bebida_con_alcohol(codigo)
                        descripcion1 = self.modelo.obtener_nombre_bebida_con_alcohol(codigo)
                        descripcion2 = '.'
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 6):

                        codigo = self.vista.vista_leer_codigo_ca()
                        precio = self.modelo.obtener_precio_bebida_sin_alcohol(codigo)
                        descripcion1 = self.modelo.obtener_nombre_bebida_sin_alcohol(codigo)
                        descripcion2 = '.'           
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)
 
                elif(respuesta_sistema == 'N'):

                    self.vista.imprimir_datos_para_factura(ci_cliente, nombre_cliente, apellido_cliente,
                    direccion_cliente, fecha_emision, timbrado, cantidad, descripcion1, descripcion2, precio, total, total_factura)

        elif(opcion_factura == 2):

            cedula_cliente = self.vista.vista_leer_ci_cliente()
            ci_cliente = self.modelo.obtener_ci_cliente(cedula_cliente)
            nombre_cliente = self.modelo.obtener_nombre_cliente(cedula_cliente)
            apellido_cliente = self.modelo.obtener_apellido_cliente(cedula_cliente)
            direccion_cliente = self.modelo.obtener_direccion_cliente(cedula_cliente)
            fecha_emision = self.modelo.obtener_fecha_emision()
            timbrado = self.modelo.obtener_timbrado()
            numero_factura = self.modelo.obtener_numero_factura()

            respuesta = self.vista.vista_obtener_precios_productos()

            if(respuesta == 1):

                codigo = self.vista.vista_leer_codigo_hamburguesa()
                descripcion1 = self.modelo.obtener_nombre_hamburguesa(codigo)
                descripcion2 = self.modelo.obtener_grupo_hamburguesa(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                precio = self.modelo.obtener_precio_hamburguesa(codigo)
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 2):

                codigo = self.vista.vista_leer_codigo_pizza()
                precio = self.modelo.obtener_precio_pizza(codigo)
                descripcion1 = self.modelo.obtener_nombre_pizza(codigo)
                descripcion2 = self.modelo.obtener_sabor_pizza(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 3):

                codigo = self.vista.vista_leer_codigo_papa_frita()
                precio = self.modelo.obtener_precio_pizza(codigo)
                descripcion1 = self.modelo.obtener_nombre_papa_frita(codigo)
                descripcion2 = self.modelo.obtener_tamanio_papa_frita(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 4):

                codigo = self.vista.vista_leer_codigo_lomito()
                precio = self.modelo.obtener_precio_lomito(codigo)
                descripcion1 = self.modelo.obtener_nombre_lomito(codigo)
                descripcion2 = self.modelo.obtener_grupo_lomito(codigo)
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 5):

                codigo = self.vista.vista_leer_codigo_ca()
                precio = self.modelo.obtener_precio_bebida_con_alcohol(codigo)
                descripcion1 = self.modelo.obtener_nombre_bebida_con_alcohol(codigo)
                descripcion2 = '.'
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            elif(respuesta == 6):

                codigo = self.vista.vista_leer_codigo_ca()
                precio = self.modelo.obtener_precio_bebida_sin_alcohol(codigo)
                descripcion1 = self.modelo.obtener_nombre_bebida_sin_alcohol(codigo)
                descripcion2 = '.'           
                cantidad = self.vista.vista_ingresar_cantidad_productos()
                total = self.modelo.calcular_monto_total(cantidad, precio)
                total_factura = self.modelo.total_factura(total)

            factura = self.vista.vista_agregar_datos_factura_sin_nombre(fecha_emision, ruc_cliente, nombre_cliente, direccion_cliente, 
                        total, total_factura, numero_factura, timbrado)
            self.modelo.guardar_factura(factura)

            try:

                respuesta_sistema = self.vista.vista_agregar_otros_productos()

                if(respuesta_sistema == 'S'):

                    raise Exception('No es posible agregar otro pedido a la misma factura')

            except Exception as e:

                raise Exception('NO es posible agregar.')

            else:

                if(respuesta_sistema == 'S'):

                    respuesta = self.vista.vista_obtener_precios_productos()

                    if(respuesta == 1):

                        codigo = self.vista.vista_leer_codigo_hamburguesa()
                        precio = self.modelo.obtener_precio_hamburguesa(codigo)
                        descripcion1 = self.modelo.obtener_nombre_hamburguesa(codigo)
                        descripcion2 = self.modelo.obtener_grupo_hamburguesa(codigo)
                        cantidad= self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 2):

                        codigo = self.vista.vista_leer_codigo_pizza()
                        precio = self.modelo.obtener_precio_pizza(codigo)
                        descripcion1 = self.modelo.obtener_nombre_pizza(codigo)
                        descripcion2 = self.modelo.obtener_sabor_pizza(codigo)
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 3):

                        codigo = self.vista.vista_leer_codigo_papa_frita()
                        precio = self.modelo.obtener_precio_pizza(codigo)
                        descripcion1 = self.modelo.obtener_nombre_papa_frita(codigo)
                        descripcion2 = self.modelo.obtener_tamanio_papa_frita(codigo)
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 4):

                        codigo = self.vista.vista_leer_codigo_lomito()
                        precio = self.modelo.obtener_precio_lomito(codigo)
                        descripcion1 = self.modelo.obtener_nombre_lomito(codigo)
                        descripcion2 = self.modelo.obtener_grupo_lomito(codigo)
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 5):

                        codigo = self.vista.vista_leer_codigo_ca()
                        precio = self.modelo.obtener_precio_bebida_con_alcohol(codigo)
                        descripcion1 = self.modelo.obtener_nombre_bebida_con_alcohol(codigo)
                        descripcion2 = '.'
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                    elif(respuesta == 6):

                        codigo = self.vista.vista_leer_codigo_ca()
                        precio = self.modelo.obtener_precio_bebida_sin_alcohol(codigo)
                        descripcion1 = self.modelo.obtener_nombre_bebida_sin_alcohol(codigo)
                        descripcion2 = '.'           
                        cantidad = self.vista.vista_ingresar_cantidad_productos()
                        total = self.modelo.calcular_monto_total(cantidad, precio)
                        total_factura = self.modelo.total_factura(total)

                elif(respuesta_sistema == 'N'):

                    self.vista.imprimir_datos_para_factura(ci_cliente, nombre_cliente, apellido_cliente, direccion_cliente, fecha_emision, timbrado, cantidad, descripcion1, descripcion2, precio, total, total_factura)

    '''Para saber que faturas han sido emitidas'''

    def facturas_emitidas(self):

        ruc_cliente = self.vista.vista_leer_ruc_cliente()
        res_factura = self.modelo.buscar_facturas(ruc_cliente)
        self.vista.imprimir_factura_emitida(res_factura)

    '''Listar fatcuras'''

    def listar_facturas(self):

        facturas = self.modelo.listar_facturas()
        self.vista.vista_listar_facturas(facturas)

    '''Inicializamos la limpieza de pantalla'''

    def clear_so_screen(self):

        self.modelo.clear_screen()

    '''Metodo para salir'''
    def exit(self):

        self.modelo.project_exit()
