import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from main.main_design import MainDesign
from forms.login_tradicional.form_login import FormLogin
from forms.login_faceid.form_login_faceid import FormLoginFaceId
from forms.register.form_register import Register
from forms.master.form_master import MasterPanel
from tkinter import messagebox as msg

#La clase padre es MainDesign
class Main(MainDesign):
    
    #Inicializamos todo
    def __init__(self):
        super().__init__()
        
    def login_credenciales(self):
        def handle_login_result(result):
            if result:
                print("Iniciar sesión exitoso")
                self.ventana.destroy()
                print("Bienvenido")
                MasterPanel()
            else:
                print("Error al iniciar sesión")

        form_login = FormLogin(on_login=handle_login_result)
        form_login.run()

    def crear_cuenta(self):
        register = Register()
        register.run()
    
    def login_faceid(self):
        def handle_login_faceid_result(result):
            if result:
                print("Iniciar sesión exitoso")
                self.ventana.destroy()
                MasterPanel()
            else:
                print("Error al iniciar sesión")
        
        form_login_faceid = FormLoginFaceId(on_login_faceid=handle_login_faceid_result)
        form_login_faceid.run()