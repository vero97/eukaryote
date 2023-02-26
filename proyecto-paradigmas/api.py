import tkinter

from GUI import *
from modelo import *
from mizodb import *
'''
Clase Aplicacion: donde se definen las funciones para agregar clientes,
empleados, proveedores.
LAs funciones son ventanas en donde se colocan los botones, 
cajas de texto, etc.

No logrè hacer que alguna de ellas funcione, pero la intenciòn era llamar 
a las funciones de la clase Modelo() y pasar los parametros necesarios 
para que se puedan instanciar las clases.
LAs funciones ventana, son las que empaquetan los botones y labels 
utilizados para poder hacer un poco de lo solicitado.
'''
class Aplicacion(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        Aplicacion.ventana_inicio(master)

    @staticmethod
    def ventana_inicio(master):

        ventana_inicio = master

        ventana_inicio.title("Menu Inicio")
        ventana_inicio.geometry("500x300+400+100")

        #Etiquetas
        label_ventana_inicio1 = MiLabel(ventana_inicio,
                                        text="Bienvenido!!. Inicie su sesion")
        label_ventana_inicio1.config(font=("MonoSpace", 10))
        label_ventana_inicio1.place(x=15, y=15)

        #Etiqueta Usuario
        label_ventana_inicio2 = MiLabel(ventana_inicio,text= "Usuario: ")
        label_ventana_inicio2.config(font=("MonoSpace", 15))
        label_ventana_inicio2.place(x=20, y=40)

        #Entradas de texto Usuario
        entry_texto_entrada1 = MiCajaTexto(ventana_inicio,
                                           font=("MonoSpace", 15))
        entry_texto_entrada1.place(x=200, y=40)
        entry_texto_entrada1.focus()

        #Etiqueta Contraseña
        label_ventana_inicio3 = MiLabel(ventana_inicio, text="Contraseña: ")
        label_ventana_inicio3.config(font=("MonoSpace", 15))
        label_ventana_inicio3.place(x=20, y=80)

        #Entrada de texto contraseña
        entry_texto_entrada2 = MiCajaTexto(ventana_inicio,
                                           font=("MonoSpace", 15), show="*")
        entry_texto_entrada2.place(x=200, y=80)

        #Botones para ingreso y salida del sistema
        button_aceptar_inicio = MiBoton(ventana_inicio, text="Confirmar",
        command=lambda: Aplicacion.confirmar_ingreso(
                         Modelo.validar_ingreso(user=entry_texto_entrada1.get(),
                             password=entry_texto_entrada2.get()),
                             ventana_inicio))
        button_aceptar_inicio.place(x=20, y=120)

        button_salir_inicio = MiBoton(ventana_inicio, text="Salir",
                                      command=lambda: ventana_inicio.destroy())
        button_salir_inicio.place(x=200, y=120)

    '''Metodo que confirma el ingreso al sistema'''
    @staticmethod
    def confirmar_ingreso(funcion, ventana):

        if funcion == True:

            PopupInfo("Ingreso Correcto", "Ha iniciado sesion correctamente", ventana)
            Aplicacion.ventana_seleccion_menu(ventana)
        else:
            PopupError("Error de Ingreso", "Intentelo de nuevo:Usuario o contraseña incorrectos", ventana)

    ''''@staticmethod
    def menu_principal(ventana):

        ventana.withdraw()
        ventana_menu = MiTopLevel(ventana)
        ventana_menu.title('Menu Principal')

        #button_salir_menu = MiBoton(ventana_menu, text="Salir",
        #                              command=lambda: ventana_menu.destroy())
        #button_salir_menu.place(x=200, y=120).pack()

        menu = MiMenuBoton(ventana_menu)
        #ventana.config(menu)

        #Menu Cliente
        cliente_menu = MiMenuBoton(menu)
        cliente_menu.add_command(label="Agregar Cliente",
        command= lambda: Aplicacion.ventana_cliente(ventana_menu))

        cliente_menu.add_command(label="Modificar Cliente",
        command= lambda: Aplicacion.ventana_cliente(ventana_menu))

        cliente_menu.add_command(label="Buscar Cliente",
        command= lambda: Aplicacion.ventana_cliente(ventana_menu))

        cliente_menu.add_command(label="Listar Cliente",
        command= lambda: Aplicacion.ventana_cliente(ventana_menu))

        cliente_menu.add_cascade(label="Clientes", menu=cliente_menu)

        #Menu Empleado
        empleado_menu = MiMenuBoton(menu)
        empleado_menu.add_command(label="Agregar Empleado",
        command= lambda: Aplicacion.ventana_empleado(ventana_menu))

        empleado_menu.add_command(label="Modificar Empleado",
        command= lambda: Aplicacion.ventana_empleado(ventana_menu))

        empleado_menu.add_command(label="Buscar Empleado",
        command= lambda: Aplicacion.ventana_empleado(ventana_menu))

        empleado_menu.add_command(label="Listar Empleado",
        command= lambda: Aplicacion.ventana_empleado(ventana_menu))

        empleado_menu.add_cascade(label="Empleado", menu=empleado_menu)

        #Menu Producto
        producto_menu = MiMenuBoton(menu)
        producto_menu.add_command(label="Agregar Producto",
        command= lambda: Aplicacion.ventana_producto(ventana_menu))

        producto_menu.add_command(label="Modificar Producto",
        command= lambda: Aplicacion.ventana_producto(ventana_menu))

        producto_menu.add_command(label="Buscar Producto",
        command= lambda: Aplicacion.ventana_producto(ventana_menu))

        producto_menu.add_command(label="Listar Producto",
        command= lambda: Aplicacion.ventana_producto(ventana_menu))

        producto_menu.add_command(label="Eliminar Producto",
        command= lambda: Aplicacion.ventana_producto(ventana_menu))

        producto_menu.add_cascade(label="Producto", menu=producto_menu)

        #Menu Proveedor
        proveedor_menu = MiMenuBoton(menu)
        proveedor_menu.add_command(label="Agregar Proveedor",
        command= lambda: Aplicacion.ventana_proveedor(ventana_menu))

        proveedor_menu.add_command(label="Buscar Proveedor",
        command= lambda: Aplicacion.ventana_proveedor(ventana_menu))

        proveedor_menu.add_command(label="Listar Proveedor",
        command= lambda: Aplicacion.ventana_proveedor(ventana_menu))

        proveedor_menu.add_cascade(label="Proveedor", menu=proveedor_menu)

        #Menu Factura
        factura_menu = MiMenuBoton(menu)
        factura_menu.add_command(label="Modificar Factura",
        command= lambda: Aplicacion.ventana_factura(ventana_menu))

        factura_menu.add_command(label="Listar Factura",
        command= lambda: Aplicacion.ventana_factura(ventana_menu))

        factura_menu.add_command(label="Imprimir Factura",
        command= lambda: Aplicacion.ventana_factura(ventana_menu))

        factura_menu.add_cascade(label="Factura", menu=factura_menu)

        ventana.protocol("WM_DELETE_WINDOW", "onexit")'''

    @staticmethod
    def ventana_seleccion_menu(ventana):

        ventana.withdraw()
        ventana_boton = MiTopLevel(ventana)
        ventana_boton.title('Seleccione')
        ventana_boton.geometry("500x300+400+100")

        label_seleccion = MiLabel(ventana_boton,
                            text="Bienvenido!!. Haga clic al menu que desea acceder")
        label_seleccion.place(x=10, y=10)

        button_persona = MiBoton(ventana_boton, text="Persona",
                        command= lambda:Aplicacion.ventana_persona(ventana_boton))
        button_persona.place(x=30, y=40)

        button_producto = MiBoton(ventana_boton, text="Producto",
                        command= lambda:Aplicacion.ventana_producto(ventana_boton))
        button_producto.place(x=30, y=80)

        button_producto = MiBoton(ventana_boton, text="Proveedor",
                    command= lambda:Aplicacion.ventana_agg_proveedor(ventana_boton))
        button_producto.place(x=30, y=120)

        button_restaurante = MiBoton(ventana_boton, text="Restaurante",
                        command= lambda:Aplicacion.ventana_agg_cliente(ventana_boton))
        button_restaurante.place(x=30, y=160)

        button_salir = MiBoton(ventana_boton, text="Exit",
                               command=lambda: ventana_boton.destroy())
        button_salir.place(x=30, y=200)

    @staticmethod
    def ventana_agg_cliente(ventana):

        ventana_cliente = MiTopLevel(ventana)
        ventana_cliente.geometry('500x500')
        ventana_cliente.title("Agregar Cliente")

        label_ruc= MiLabel(ventana_cliente, text="RUC: ", font=("MonoSpace", 8))
        label_ruc.place(x=20, y=40)

        entry_ruc= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_ruc.place(x=200, y=40)

        label_ci= MiLabel(ventana_cliente, text="CI: ", font=("MonoSpace", 8))
        label_ci.place(x=20, y=80)

        entry_ci= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_ci.place(x=200, y=80)

        label_nombre= MiLabel(ventana_cliente, text="NOMBRE: ",
                              font=("MonoSpace", 8))
        label_nombre.place(x=20, y=120)

        entry_nombre= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=120)

        label_apellido= MiLabel(ventana_cliente, text="APELLIDO: ",
                                font=("MonoSpace", 8))
        label_apellido.place(x=20, y=160)

        entry_apellido= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_apellido.place(x=200, y=160)

        label_direccion= MiLabel(ventana_cliente, text="DIRECCION: ",
                                 font=("MonoSpace", 8))
        label_direccion.place(x=20, y=200)

        entry_direccion= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_direccion.place(x=200, y=200)

        label_numero_contacto= MiLabel(ventana_cliente, text="CONTACTO: ",
                                       font=("MonoSpace", 8))
        label_numero_contacto.place(x=20, y=240)

        entry_numero_contacto= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_numero_contacto.place(x=200, y=240)

        label_mail= MiLabel(ventana_cliente, text="MAIL: ", font=("MonoSpace", 8))
        label_mail.place(x=20, y=280)

        entry_mail= MiCajaTexto(ventana_cliente, font=("MonoSpace", 8))
        entry_mail.place(x=200, y=280)

        '''Botones para confirmar y abortar la creacion de clientes nuevos'''

        cliente = Cliente(entry_ruc.get(), entry_ci.get(), entry_nombre.get(),
                          entry_apellido.get(), entry_direccion.get(),
                          entry_numero_contacto.get(),entry_mail.get())

        button_crear_cliente = MiBoton(ventana_cliente, text="Crear cliente",
                    command=lambda:Aplicacion.crear_cliente(cliente))
        button_crear_cliente.place(x=20, y=340)

        button_salir_inicio = MiBoton(ventana_cliente, text="Salir",
                                      command=lambda:ventana_cliente.destroy())
        button_salir_inicio.place(x=200, y=340)

        ventana_cliente.protocol("WM_DELETE_WINDOW", "onexit")

    @staticmethod
    def ventana_modificaciones_cliente(ventana):

        ventana.withdraw()
        opcion = IntVar()
        ventana_modificar_cliente = MiTopLevel(ventana)
        ventana_modificar_cliente.geometry('500x500')
        ventana_modificar_cliente.title("Modificaciones del cliente")

        label_opcion= MiLabel(ventana_modificar_cliente, text="INGRESE SU OPCION",
                                       font=("MonoSpace", 8))
        label_opcion.place(x=20, y=160)

        entry_opcion= MiCajaTexto(ventana_modificar_cliente, font=("MonoSpace", 8))
        entry_opcion.place(x=200, y=160)

        #Para ingreso de CI
        label_cedula = MiLabel(ventana_modificar_cliente,
                               text="Ingrese numero de cedula: ")
        label_cedula.place(x=20, y=200)

        entry_cedula = MiCajaTexto(ventana_modificar_cliente, font=("MonoSpace", 15))
        entry_cedula.place(x=200, y=200)
        entry_cedula.focus()

        #RadioButtons.

        radio_modificar_numero = MiRadiobutton(ventana_modificar_cliente, variable=opcion,
                                               text="Numero Cliente", value='1')
        radio_modificar_numero.pack()

        radio_modificar_mail = MiRadiobutton(ventana_modificar_cliente, variable=opcion,
                                             text="Mail Cliente", value='2')
        radio_modificar_mail.pack()

        radio_modificar_direccion = MiRadiobutton(ventana_modificar_cliente, variable=opcion,
                                                  text="Direccion", value='3')
        radio_modificar_direccion.pack()

        label_nuevo_valor = MiLabel(ventana_modificar_cliente, text="Ingrese el valor nuevo")
        label_nuevo_valor.place(x=20, y=260)

        entry_nuevo_valor = MiCajaTexto(ventana_modificar_cliente, font=("MonoSpace", 15))
        entry_nuevo_valor.place(x=200, y=260)

        button_confirmar = MiBoton(ventana_modificar_cliente, text="Confirmar",
        command=lambda: Aplicacion.seleccionar_opcion(entry_opcion.get(),
                                                      entry_cedula.get(),
                                                      entry_nuevo_valor.get(),
                                                      ventana_modificar_cliente))
        button_confirmar.place(x=20, y=300)

        button_retroceder = MiBoton(ventana_modificar_cliente, text="Retroceder",
                            command=lambda: Aplicacion.ventana_persona(ventana_modificar_cliente))
        button_retroceder.place(x=200, y=300)

    @staticmethod
    def seleccionar_opcion(opcion, numero_cedula, nuevo_valor, ventana):

        if (Modelo.validar_existencia_cliente(cedula_cliente=numero_cedula)==True):

            if (opcion=='1'):

                Modelo.modificar_numero_cliente(numero_cedula, nuevo_valor)

            elif (opcion=='2'):

                Modelo.modificar_mail_cliente(numero_cedula, nuevo_valor)

            elif (opcion=='3'):

                Modelo.modificar_direccion_cliente(numero_cedula, nuevo_valor)

                PopupInfo('Modificacion correcta', 'La modificacion se ha realizado',
                      ventana)
            else:

                PopupError('Ha ocurrido un error', 'Verifique que los datos sean correctos',
                       ventana)
        else:
                PopupError('Ha ocurrido un error', 'Verifique existncia', ventana)


    @staticmethod
    def crear_cliente(cliente):

        Modelo.guardar_cliente(cliente=cliente)

    @staticmethod
    def ventana_buscar_cliente(ventana):

        ventana_buscar_cliente = MiTopLevel(ventana)
        ventana_buscar_cliente.title("Buscar Clientes")

        label_ruc_ci= MiLabel(ventana_buscar_cliente, text="RUC: ",
                              font=("MonoSpace", 8))
        label_ruc_ci.place(x=20, y=40)

        entry_ruc_ci= MiCajaTexto(ventana_buscar_cliente, font=("MonoSpace", 8))
        entry_ruc_ci.place(x=20, y=40)

        button_buscar_cliente = MiBoton(ventana_buscar_cliente, text="Buscar",
            command= Aplicacion.confirmar_busqueda(entry_ruc_ci.get(),
                                                   ventana_buscar_cliente))
        button_buscar_cliente.place(x=10, y=20)

    @staticmethod
    def ventana_resultado_cliente(ruc_ci_cliente, ventana):

        ventana_resultado_cliente = MiTopLevel(ventana)
        ventana_resultado_cliente.title("EL cliente es:")

        cliente_resultado = Modelo.buscar_cliente(ruc_ci_cliente)

    @staticmethod
    def ventana_persona(ventana):

        ventana.withdraw()

        ventana_persona = MiTopLevel(ventana)
        ventana_persona.geometry('250x300')
        ventana_persona.title("Operaciones Persona")

        #Agregar cliente
        button_cliente = MiBoton(ventana_persona, text="Cliente",
                command= lambda:Aplicacion.ventana_operaciones_cliente(ventana_persona))
        button_cliente.place(x=20, y=100)

        #Agregar Empleado
        button_empleado = MiBoton(ventana_persona, text="Empleado",
                        command= lambda:Aplicacion.ventana_operaciones_empleado(ventana_persona))
        button_empleado.place(x=20, y=150)

        button_salir= MiBoton(ventana_persona, text="Retroceder",
                    command=lambda:Aplicacion.ventana_seleccion_menu(ventana_persona))
        button_salir.place(x=20, y=200)

    @staticmethod
    def ventana_agg_proveedor(ventana):

        ventana_proveedor = MiTopLevel(ventana)
        ventana_proveedor.geometry('500x500')
        ventana_proveedor.title("Agregar Proveedor")

        label_ruc= MiLabel(ventana_proveedor, text="RUC: ", font=("MonoSpace", 8))
        label_ruc.place(x=20, y=40)

        entry_ruc= MiCajaTexto(ventana_proveedor, font=("MonoSpace", 8))
        entry_ruc.place(x=200, y=40)

        label_nombre= MiLabel(ventana_proveedor, text="NOMBRE: ",
                              font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_proveedor, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_direccion= MiLabel(ventana_proveedor, text="DIRECCION: ",
                                 font=("MonoSpace", 8))
        label_direccion.place(x=20, y=120)

        entry_direccion= MiCajaTexto(ventana_proveedor, font=("MonoSpace", 8))
        entry_direccion.place(x=200, y=120)

        label_numero_contacto= MiLabel(ventana_proveedor, text="CONTACTO: ",
                                       font=("MonoSpace", 8))
        label_numero_contacto.place(x=20, y=160)

        entry_numero_contacto= MiCajaTexto(ventana_proveedor, font=("MonoSpace", 8))
        entry_numero_contacto.place(x=200, y=160)

        label_mail= MiLabel(ventana_proveedor, text="MAIL: ", font=("MonoSpace", 8))
        label_mail.place(x=20, y=200)

        entry_mail= MiCajaTexto(ventana_proveedor, font=("MonoSpace", 8))
        entry_mail.place(x=200, y=200)

        '''Botones para confirmar y abortar la creacion de clientes nuevos'''

        proveedor = Proveedor(entry_ruc.get(), entry_nombre.get(),
                            entry_direccion.get(), entry_numero_contacto.get(),
                            entry_mail.get())

        button_crear_proveedor = MiBoton(ventana_proveedor, text="Crear Proveedor",
                    command=lambda:Aplicacion.crear_proveedor(proveedor))
        button_crear_proveedor.place(x=20, y=240)

        button_salir = MiBoton(ventana_proveedor, text="Salir",
                                      command=lambda:ventana_proveedor.destroy())
        button_salir.place(x=200, y=240)

        ventana_proveedor.protocol("WM_DELETE_WINDOW", "onexit")

    @staticmethod
    def crear_proveedor(proveedor):

        Modelo.guardar_proveedor(proveedor=proveedor)

    @staticmethod
    def ventana_operaciones_empleado(ventana):

        ventana.withdraw()
        ventana_operaciones_empleado = MiTopLevel(ventana)
        ventana_operaciones_empleado.geometry('200x200')
        ventana_operaciones_empleado.title('Cliente')

        label_cliente = MiLabel(ventana_operaciones_empleado,
                                text="Seleccione la operacion que desea realizar")
        label_cliente.place(x=10, y=10)

        button_agregar = MiBoton(ventana_operaciones_empleado, text="Agregar EMpleado",
        command=lambda: Aplicacion.ventana_agg_empleado(ventana_operaciones_empleado))
        button_agregar.place(x=20, y=50)

        button_modificar = MiBoton(ventana_operaciones_empleado, text="Modificar Cliente",
        command=lambda: Aplicacion.ventana_modificaciones_empleado(ventana_operaciones_empleado))
        button_modificar.place(x=20, y=100)

        button_salir = MiBoton(ventana_operaciones_empleado, text="Retroceder",
        command=lambda:Aplicacion.ventana_persona(ventana_operaciones_empleado))
        button_salir.place(x=20, y=150)

    @staticmethod
    def ventana_operaciones_cliente(ventana):

        ventana.withdraw()
        ventana_operaciones_cliente = MiTopLevel(ventana)
        ventana_operaciones_cliente.geometry('200x200')
        ventana_operaciones_cliente.title('Cliente')

        label_cliente = MiLabel(ventana_operaciones_cliente,
                                text="Seleccione la operacion que desea realizar")
        label_cliente.place(x=10, y =10)

        button_agregar = MiBoton(ventana_operaciones_cliente, text="Agregar CLiente",
                                 command=lambda: Aplicacion.ventana_agg_cliente(ventana_operaciones_cliente))
        button_agregar.place(x=20, y=50)

        button_modificar = MiBoton(ventana_operaciones_cliente, text="Modificar Cliente",
                        command=lambda: Aplicacion.ventana_modificaciones_cliente(ventana_operaciones_cliente))
        button_modificar.place(x=20, y=100)

        button_salir = MiBoton(ventana_operaciones_cliente, text="Retroceder",
                               command=lambda:Aplicacion.ventana_persona(ventana_operaciones_cliente))
        button_salir.place(x=20, y=150)

    @staticmethod
    def ventana_agg_empleado(ventana):
        ventana_empleado = MiTopLevel(ventana)
        ventana_empleado.geometry('600x600')
        ventana_empleado.title("Agregar Empleado")

        label_ci= MiLabel(ventana_empleado, text="CI: ", font=("MonoSpace", 8))
        label_ci.place(x=20, y=90)

        entry_ci= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_ci.place(x=200, y=90)

        label_nombre= MiLabel(ventana_empleado, text="NOMBRE: ",
                              font=("MonoSpace", 8))
        label_nombre.place(x=20, y=140)

        entry_nombre= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=140)

        label_apellido= MiLabel(ventana_empleado, text="APELLIDO: ",
                                font=("MonoSpace", 8))
        label_apellido.place(x=20, y=190)

        entry_apellido= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_apellido.place(x=200, y=190)

        label_direccion= MiLabel(ventana_empleado, text="DIRECCION: ",
                                 font=("MonoSpace", 8))
        label_direccion.place(x=20, y=240)

        entry_direccion= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_direccion.place(x=200, y=240)

        label_fecha_nacimiento= MiLabel(ventana_empleado, text="FECHA NACIMIENTO: ",
                                       font=("MonoSpace", 8))
        label_fecha_nacimiento.place(x=20, y=290)

        entry_fecha_nacimiento= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_fecha_nacimiento.place(x=200, y=290)

        label_usuario= MiLabel(ventana_empleado, text="USUARIO: ",
                                       font=("MonoSpace", 8))
        label_usuario.place(x=20, y=340)

        entry_usuario= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_usuario.place(x=200, y=340)

        label_contrasenha= MiLabel(ventana_empleado, text="CONTRASEÑA: ",
                                       font=("MonoSpace", 8))
        label_contrasenha.place(x=20, y=390)

        entry_contrasenha= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_contrasenha.place(x=200, y=390)

        label_numero_contacto= MiLabel(ventana_empleado, text="CONTACTO: ",
                                       font=("MonoSpace", 8))
        label_numero_contacto.place(x=20, y=440)

        entry_numero_contacto= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_numero_contacto.place(x=200, y=440)

        label_mail= MiLabel(ventana_empleado, text="MAIL: ", font=("MonoSpace", 8))
        label_mail.place(x=20, y=490)

        entry_mail= MiCajaTexto(ventana_empleado, font=("MonoSpace", 8))
        entry_mail.place(x=200, y=490)

        '''Botones para confirmar y abortar la creacion de clientes nuevos'''

        empleado = Empleado(entry_ci.get(), entry_nombre.get(),
                          entry_apellido.get(), entry_direccion.get(),
                          entry_fecha_nacimiento.get(), entry_usuario.get(),
                          entry_contrasenha.get(), entry_numero_contacto.get(),entry_mail.get())

        button_crear_empleado = MiBoton(ventana_empleado, text="Crear Empleado",
                    command=lambda:Aplicacion.crear_empleado(empleado))
        button_crear_empleado.place(x=20, y=540)

        button_salir_inicio = MiBoton(ventana_empleado, text="Retroceder",
        command=lambda:Aplicacion.ventana_seleccion_menu(ventana_empleado))
        button_salir_inicio.place(x=200, y=540)

        ventana_empleado.protocol("WM_DELETE_WINDOW", "onexit")

    @staticmethod
    def ventana_producto(ventana):

        ventana.withdraw()
        ventana_producto = MiTopLevel(ventana)
        ventana_producto.geometry('250x300')
        ventana_producto.title("Operaciones Productos")

        #Agregar cliente
        button_alimento = MiBoton(ventana_producto, text="Alimento",
                command= lambda:Aplicacion.ventana_operaciones_producto(ventana_producto))
        button_alimento.place(x=20, y=100)

        #Agregar Empleado
        button_bebida = MiBoton(ventana_producto, text="Bebida",
                        command= lambda:Aplicacion.ventana_operaciones_producto(ventana_producto))
        button_bebida.place(x=20, y=150)

        button_salir= MiBoton(ventana_producto, text="Retroceder",
                    command=lambda:Aplicacion.ventana_seleccion_menu(ventana_producto))
        button_salir.place(x=20, y=200)

    @staticmethod
    def ventana_operaciones_producto(ventana):

        ventana.withdraw()
        ventana_operaciones_producto = MiTopLevel(ventana)
        ventana_operaciones_producto.geometry('200x200')
        ventana_operaciones_producto.title('Cliente')

        label_cliente = MiLabel(ventana_operaciones_producto,
                                text="Seleccione la operacion que desea realizar")
        label_cliente.place(x=10, y =10)

        button_agregar = MiBoton(ventana_operaciones_producto, text="Agregar Alimentos",
                                 command=lambda: Aplicacion.agregar_alimentos(ventana_operaciones_producto))
        button_agregar.place(x=20, y=50)

        button_modificar = MiBoton(ventana_operaciones_producto, text="Modificaciones",
                        command=lambda: Aplicacion.ventana_modificaciones_cliente(ventana_operaciones_producto))
        button_modificar.place(x=20, y=100)

        button_salir = MiBoton(ventana_operaciones_producto, text="Retroceder",
                               command=lambda:Aplicacion.ventana_producto(ventana_operaciones_producto))
        button_salir.place(x=20, y=150)

    @staticmethod
    def agregar_alimentos(ventana):

        ventana.withdraw()
        opcion = IntVar()
        ventana_agregar = MiTopLevel(ventana)
        ventana_agregar.title("Agregar alimentos")

        label_opcion= MiLabel(ventana_agregar, text="INGRESE SU OPCION",
                                       font=("MonoSpace", 8))
        label_opcion.place(x=20, y=160)

        entry_opcion= MiCajaTexto(ventana_agregar, font=("MonoSpace", 8))
        entry_opcion.place(x=200, y=160)

        #RadioButtons.
        radio_hamburguesa = MiRadiobutton(ventana_agregar, variable=opcion,
                                           text="Hamburguesa", value='1')
        radio_hamburguesa.pack()

        radio_lomito = MiRadiobutton(ventana_agregar, variable=opcion,
                                    text="Lomito", value='2')
        radio_lomito.pack()

        radio_papas_fritas = MiRadiobutton(ventana_agregar, variable=opcion,
                                         text="Papas Fritas", value='3')
        radio_papas_fritas.pack()

        radio_pizza = MiRadiobutton(ventana_agregar, variable=opcion,
                                    text="Pizza", value='4')
        radio_pizza.pack()

        button_confirmar = MiBoton(ventana_agregar, text="Confirmar",
        command=lambda: Aplicacion.seleccionar_opcion(entry_opcion.get(),
                                                      ventana_agregar))
        button_confirmar.place(x=20, y=250)

        button_retroceder = MiBoton(ventana_agregar, text="Retroceder",
        command=lambda: Aplicacion.ventana_seleccion_menu(ventana_agregar))
        button_retroceder.place(x=200, y=250)

    @staticmethod
    def seleccionar_opcion(opcion, ventana):
        if opcion=='1':
            Aplicacion.ventana_agg_hamburguesa(ventana)
        elif opcion=='2':
            Aplicacion.ventana_agg_lomito(ventana)
        elif opcion=='3':
            Aplicacion.ventana_agg_papas_fritas(ventana)
        elif opcion=='4':
            Aplicacion.ventana_agg_pizza(ventana)

    @staticmethod
    def ventana_agg_hamburguesa(ventana):
        ventana.withdraw()
        ventana_hamburguesa = MiTopLevel(ventana)
        ventana_hamburguesa.geometry('500x500')
        ventana_hamburguesa.title('Agregar HAmburguesa')

        label_codigo= MiLabel(ventana_hamburguesa, text="CODIGO: ", font=("MonoSpace", 8))
        label_codigo.place(x=20, y=40)

        entry_codigo= MiCajaTexto(ventana_hamburguesa, font=("MonoSpace", 8))
        entry_codigo.place(x=200, y=40)

        label_nombre= MiLabel(ventana_hamburguesa, text="NOMBRE: ", font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_hamburguesa, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_precio= MiLabel(ventana_hamburguesa, text="PRECIO: ",
                              font=("MonoSpace", 8))
        label_precio.place(x=20, y=120)

        entry_precio= MiCajaTexto(ventana_hamburguesa, font=("MonoSpace", 8))
        entry_precio.place(x=200, y=120)

        label_grupo= MiLabel(ventana_hamburguesa, text="GRUPO: ",
                                font=("MonoSpace", 8))
        label_grupo.place(x=20, y=160)

        entry_grupo= MiCajaTexto(ventana_hamburguesa, font=("MonoSpace", 8))
        entry_grupo.place(x=200, y=160)

        hamburguesa = Hamburguesa(entry_codigo.get(), entry_nombre.get(),
                                  entry_precio.get(), entry_grupo.get())

        button_confirmar = MiBoton(ventana_hamburguesa, text='Confirmar',
        command=lambda:Aplicacion.crear_hamburguesa(hamburguesa))
        button_confirmar.place(x=20, y=200)

        button_retroceder = MiBoton(ventana_hamburguesa, text='Retroceder',
        command=lambda: Aplicacion.agregar_alimentos(ventana_hamburguesa))
        button_retroceder.place(x=200, y=200)

    @staticmethod
    def crear_hamburguesa(hamburguesa):

        Modelo.guardar_hamburguesa(hamburguesa=hamburguesa)

    @staticmethod
    def ventana_agg_lomito(ventana):
        ventana.withdraw()
        ventana_lomito = MiTopLevel(ventana)
        ventana_lomito.title('Agregar lomito')

        label_codigo= MiLabel(ventana_lomito, text="CODIGO: ", font=("MonoSpace", 8))
        label_codigo.place(x=20, y=40)

        entry_codigo= MiCajaTexto(ventana_lomito, font=("MonoSpace", 8))
        entry_codigo.place(x=200, y=40)

        label_nombre= MiLabel(ventana_lomito, text="NOMBRE: ", font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_lomito, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_precio= MiLabel(ventana_lomito, text="PRECIO: ",
                              font=("MonoSpace", 8))
        label_precio.place(x=20, y=120)

        entry_precio= MiCajaTexto(ventana_lomito, font=("MonoSpace", 8))
        entry_precio.place(x=200, y=120)

        label_grupo= MiLabel(ventana_lomito, text="GRUPO: ",
                                font=("MonoSpace", 8))
        label_grupo.place(x=20, y=160)

        entry_grupo= MiCajaTexto(ventana_lomito, font=("MonoSpace", 8))
        entry_grupo.place(x=200, y=160)

        lomito = Lomito(entry_codigo.get(), entry_nombre.get(),
                                  entry_precio.get(), entry_grupo.get())

        button_confirmar = MiBoton(ventana_lomito, text='Confirmar',
        command=lambda: Aplicacion.crear_lomito(lomito))
        button_confirmar.place(x=20, y=200)

        button_retroceder = MiBoton(ventana_lomito, text='Retroceder',
        command=lambda: Aplicacion.agregar_alimentos(ventana_lomito))
        button_retroceder.place(x=200, y=200)

    @staticmethod
    def crear_lomito(lomito):

        Modelo.guardar_lomito(lomito=lomito)

    @staticmethod
    def ventana_agg_pizza(ventana):
        ventana.withdraw()
        ventana_pizza = MiTopLevel(ventana)
        ventana_pizza.title('Agregar lomito')

        label_codigo= MiLabel(ventana_pizza, text="CODIGO: ", font=("MonoSpace", 8))
        label_codigo.place(x=20, y=40)

        entry_codigo= MiCajaTexto(ventana_pizza, font=("MonoSpace", 8))
        entry_codigo.place(x=200, y=40)

        label_nombre= MiLabel(ventana_pizza, text="NOMBRE: ", font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_pizza, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_precio= MiLabel(ventana_pizza, text="PRECIO: ",
                              font=("MonoSpace", 8))
        label_precio.place(x=20, y=120)

        entry_precio= MiCajaTexto(ventana_pizza, font=("MonoSpace", 8))
        entry_precio.place(x=200, y=120)

        label_sabor= MiLabel(ventana_pizza, text="SABOR: ",
                                font=("MonoSpace", 8))
        label_sabor.place(x=20, y=160)

        entry_sabor= MiCajaTexto(ventana_pizza, font=("MonoSpace", 8))
        entry_sabor.place(x=200, y=160)

        pizza = Pizza(entry_codigo.get(), entry_nombre.get(),
                                  entry_precio.get(), entry_sabor.get())

        button_confirmar = MiBoton(ventana_pizza, text='Confirmar',
        command=lambda: Aplicacion.crear_pizza(pizza))
        button_confirmar.place(x=20, y=200)

        button_retroceder = MiBoton(ventana_pizza, text='Retroceder',
        command=lambda: Aplicacion.agregar_alimentos(ventana_pizza))
        button_retroceder.place(x=200, y=200)

    @staticmethod
    def crear_pizza(pizza):

        Modelo.guardar_pizza(pizza=pizza)

    @staticmethod
    def ventana_agg_papas_fritas(ventana):
        ventana.withdraw()
        ventana_papa_frita = MiTopLevel(ventana)
        ventana_papa_frita.title('Agregar papa frita')

        label_codigo= MiLabel(ventana_papa_frita, text="CODIGO: ", font=("MonoSpace", 8))
        label_codigo.place(x=20, y=40)

        entry_codigo= MiCajaTexto(ventana_papa_frita, font=("MonoSpace", 8))
        entry_codigo.place(x=200, y=40)

        label_nombre= MiLabel(ventana_papa_frita, text="NOMBRE: ", font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_papa_frita, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_precio= MiLabel(ventana_papa_frita, text="PRECIO: ",
                              font=("MonoSpace", 8))
        label_precio.place(x=20, y=120)

        entry_precio= MiCajaTexto(ventana_papa_frita, font=("MonoSpace", 8))
        entry_precio.place(x=200, y=120)

        label_tamanio= MiLabel(ventana_papa_frita, text="TAMAÑO: ",
                                font=("MonoSpace", 8))
        label_tamanio.place(x=20, y=160)

        entry_tamanio= MiCajaTexto(ventana_papa_frita, font=("MonoSpace", 8))
        entry_tamanio.place(x=200, y=160)

        papa_frita = PapaFrita(entry_codigo.get(), entry_nombre.get(),
                                  entry_precio.get(), entry_tamanio.get())

        button_confirmar = MiBoton(ventana_papa_frita, text='Confirmar',
        command=lambda: Aplicacion.crear_pizza(papa_frita))
        button_confirmar.place(x=20, y=200)

        button_retroceder = MiBoton(ventana_papa_frita, text='Retroceder',
        command=lambda: Aplicacion.agregar_alimentos(ventana_papa_frita))
        button_retroceder.place(x=200, y=200)

    @staticmethod
    def crear_papa_frita(papa_frita):

        Modelo.guardar_pizza(papa_frita=papa_frita)

    @staticmethod
    def ventana_agg_bebida_alcoholica(ventana):
        ventana.withdraw()
        ventana_bebida_alcoholica = MiTopLevel(ventana)
        ventana_bebida_alcoholica.title('Agregar papa frita')

        label_codigo= MiLabel(ventana_bebida_alcoholica, text="CODIGO: ", font=("MonoSpace", 8))
        label_codigo.place(x=20, y=40)

        entry_codigo= MiCajaTexto(ventana_bebida_alcoholica, font=("MonoSpace", 8))
        entry_codigo.place(x=200, y=40)

        label_nombre= MiLabel(ventana_bebida_alcoholica, text="NOMBRE: ", font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_bebida_alcoholica, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_precio= MiLabel(ventana_bebida_alcoholica, text="PRECIO: ",
                              font=("MonoSpace", 8))
        label_precio.place(x=20, y=120)

        entry_precio= MiCajaTexto(ventana_bebida_alcoholica, font=("MonoSpace", 8))
        entry_precio.place(x=200, y=120)

        bebida = BebidaConAlcohol(entry_codigo.get(), entry_nombre.get(),
                                  entry_precio.get())

        button_confirmar = MiBoton(ventana_bebida_alcoholica, text='Confirmar',
        command=lambda: Aplicacion.crear_bebida_con_alcohol(bebida))
        button_confirmar.place(x=20, y=200)

        button_retroceder = MiBoton(ventana_bebida_alcoholica, text='Retroceder',
        command=lambda: Aplicacion.ventana_producto(ventana_bebida_alcoholica))
        button_retroceder.place(x=200, y=200)

    @staticmethod
    def crear_bebida_con_alcohol(bebida):

        Modelo.guardar_bebida_con_alcohol(con_alcohol=bebida)

    @staticmethod
    def ventana_agg_bebida_sin_alcohol(ventana):
        ventana.withdraw()
        ventana_bebida_sin_alcohol = MiTopLevel(ventana)
        ventana_bebida_sin_alcohol.title('Agregar papa frita')

        label_codigo= MiLabel(ventana_bebida_sin_alcohol, text="CODIGO: ", font=("MonoSpace", 8))
        label_codigo.place(x=20, y=40)

        entry_codigo= MiCajaTexto(ventana_bebida_sin_alcohol, font=("MonoSpace", 8))
        entry_codigo.place(x=200, y=40)

        label_nombre= MiLabel(ventana_bebida_sin_alcohol, text="NOMBRE: ", font=("MonoSpace", 8))
        label_nombre.place(x=20, y=80)

        entry_nombre= MiCajaTexto(ventana_bebida_sin_alcohol, font=("MonoSpace", 8))
        entry_nombre.place(x=200, y=80)

        label_precio= MiLabel(ventana_bebida_sin_alcohol, text="PRECIO: ",
                              font=("MonoSpace", 8))
        label_precio.place(x=20, y=120)

        entry_precio= MiCajaTexto(ventana_bebida_sin_alcohol, font=("MonoSpace", 8))
        entry_precio.place(x=200, y=120)

        bebida = BebidaSinAlcohol(entry_codigo.get(), entry_nombre.get(),
                                  entry_precio.get())

        button_confirmar = MiBoton(ventana_bebida_sin_alcohol, text='Confirmar',
        command=lambda: Aplicacion.crear_bebida_sin_alcohol(bebida))
        button_confirmar.place(x=20, y=200)

        button_retroceder = MiBoton(ventana_bebida_sin_alcohol, text='Retroceder',
        command=lambda: Aplicacion.ventana_producto(ventana_bebida_sin_alcohol))
        button_retroceder.place(x=200, y=200)

    @staticmethod
    def crear_bebida_sin_alcohol(bebida):

        Modelo.guardar_bebida_sin_alcohol(sin_alcohol=bebida)

    @staticmethod
    def ventana_seleccionar_bebida(ventana):

        ventana.withdraw()
        opcion = IntVar()
        ventana_agregar_bebida = MiTopLevel(ventana)
        ventana_agregar_bebida.title("Bebidas")

        label_opcion= MiLabel(ventana_agregar_bebida, text="INGRESE SU OPCION",
                                       font=("MonoSpace", 8))
        label_opcion.place(x=20, y=160)

        entry_opcion= MiCajaTexto(ventana_agregar_bebida, font=("MonoSpace", 8))
        entry_opcion.place(x=200, y=160)

        radio_hamburguesa = MiRadiobutton(ventana_agregar_bebida, variable=opcion,
                                           text="Bebida alcoholica", value='1')
        radio_hamburguesa.pack()

        radio_lomito = MiRadiobutton(ventana_agregar_bebida, variable=opcion,
                                    text="Bebida SIn Alcohol", value='2')
        radio_lomito.pack()

        button_confirmar = MiBoton(ventana_agregar_bebida, text="Confirmar",
        command=lambda: Aplicacion.seleccionar_opcion(entry_opcion.get(),
                                                      ventana_agregar_bebida))
        button_confirmar.place(x=20, y=250)

        button_retroceder = MiBoton(ventana_agregar_bebida, text="Retroceder",
        command=lambda: Aplicacion.ventana_seleccion_menu(ventana_agregar_bebida))
        button_retroceder.place(x=200, y=250)

    @staticmethod
    def seleccionar_opcion_bebida(opcion, ventana):

        if opcion=='1':
            Aplicacion.ventana_agg_bebida_alcoholica(ventana)
        elif opcion=='2':
            Aplicacion.ventana_agg_bebida_sin_alcohol(ventana)

    @staticmethod
    def crear_empleado(empleado):

        Modelo.guardar_empleado(empleado=empleado)

    @staticmethod
    def main():

        root = MiVentana()
        api = Aplicacion(master=root)
        api.mainloop()

if __name__ == "__main__":
      Aplicacion.main()
