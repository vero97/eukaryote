from tkinter import *
from tkinter.messagebox import *


class MiVentana(Tk):

    def __init__(self, parent=None, **config):

        Tk.__init__(self, parent, **config)
        self.config(bg="light pink")

'''class MiFrame(Frame):

    def __init__(self, parent=None, **config):

        Frame.__init__(self, parent, config)
        self.config(bg="light blue")
        self.pack()'''

class MiBoton(Button):

    '''Clase MiBoton: se definen las configuraciones basicas de los botones'''
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.config(fg="black", bg="light pink", cursor="center_ptr",
                    font=("Calibri light", 12), width=15, anchor="center")
        self.pack()

class MiCajaTexto(Entry):

    '''Clase MiCajaTexto: se definen las propiedades basicas de las cajas de texto'''
    def __init__(self, parent=None, **config):

        Entry.__init__(self, parent, **config)
        self.config(bd=8, width=20, font=('Calibri', 12))

class MiTexto(Text):

    '''Clase MiTexto: se definen las propiedades del Text'''
    def __init__(self, parent=None, **config):
        """Inicializador del Text"""
        Text.__init__(self, parent, **config)
        self.config(font=('Calibri', 12))

class MiCheckButton(Checkbutton):

    '''Clase MiCheckButton: se definen las propiedades que tendra el check button'''
    def __init__(self, parent=None, **config):
        '''Inicializador del checkbutton'''
        Checkbutton.__init__(self, parent, **config)
        self.config(font=('Calibri', 10), height=5, width=20)

class MiMenuBoton(Menu):

    '''Clase MiMenuBoton: se definen las propiedades que tendra el Menu'''
    def __init__(self, **config):
        '''Inicializador del Menu'''

        Menu.__init__(self, **config)
        self.config(tearoff=False, font=('Calibri', 10))

class MiRadiobutton(Radiobutton):

    '''Clase MiRadiobutton: contiene las configuraciones basicas de los botones'''
    def __init__(self, parent=None, **config):
        '''Inicializador del RadioButton'''
        Radiobutton.__init__(self, parent, **config)
        self.pack()
        self.config(fg='black', cursor='center_ptr', font=('Calibri', 12))

class MiLabel(Label):

    '''Clase MiLabel: contiene las configuraciones basicas de las del Label'''
    def __init__(self, parent=None, **config):
        '''Inicializador del Label'''

        Label.__init__(self, parent, **config)
        self.config(fg="Black", font=('Calibri', 12))

class MiTopLevel(Toplevel):

    '''Clase MiTopLevel: contiene las configuraciones del TopLevel'''
    def __init__(self, parent=None, **config):

        Toplevel.__init__(self, parent, **config)
        self.resizable(0, 0)
        self.geometry("400x400+500+100")
        self.focus_set()
        self.grab_set()
        self.config(bg='cadetblue4')

class PopupInfo():

    '''Clase que crea una ventana de informacion'''
    def __init__(self, titulo, subtitulo, parent=None):
        self.popup_info = showinfo(titulo, subtitulo, parent=parent)

class PopupError():

    '''Clase que crea una ventana de error'''
    def __init__(self, titulo, subtitulo, parent=None):        
        self.popup_error = showerror(titulo, subtitulo, parent=parent)
