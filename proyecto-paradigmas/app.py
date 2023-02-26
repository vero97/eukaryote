from modelo import Modelo
from controlador import Controlador
from vista import Vista

class Main():

    def __init__(self):

        self.c = Controlador()
        self.v = Vista()
        self.m = Modelo()

    '''Menu que debera inicializarse.'''

    def menu_principal(self):

        self.c.clear_so_screen()
    
        mi_opcion = self.v.vista_mensajes()

        if(mi_opcion == 1):

            self.c.agregar_personas_proveedores()

        elif(mi_opcion == 2):

    	    self.c.listar_personas_proveedores()

        elif(mi_opcion == 3):

    	    self.c.buscar_personas_proveedores()

        elif(mi_opcion == 4):

    	    self.c.agregar_nuevos_productos()

        elif(mi_opcion == 5):

    	    self.c.listar_productos()

        elif(mi_opcion == 6):

    	    self.c.buscar_productos()

        elif(mi_opcion == 7):

    	    self.c.agregar_pedidos()

        elif(mi_opcion == 8):

    	    self.c.facturas_emitidas()

        elif(mi_opcion == 9):

    	    self.c.listar_facturas()

        elif(mi_opcion == 10):

            x = self.v.mensaje_salida()

            if(x == 1):

                self.c.exit()

            elif(x == 2):

                Main().menu_principal()

    if __name__ == "main":

        Main().menu_principal()