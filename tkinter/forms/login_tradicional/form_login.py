import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import messagebox as msg
from forms.login_tradicional.form_login_design import FormLoginDesign
from forms.login_faceid.form_login_faceid import FormLoginFaceId
from forms.register.form_register import Register
import database as db

class FormLogin(FormLoginDesign):
    
    #Inicializamos todo
    def __init__(self):
        super().__init__()
    
    def crear_cuenta(self):
        register = Register()
        register.run()
    
    def login_credentials(self, nombre, password):
        # Obtener el valor de las variables StringVar
        res_db = db.getUserCredentials(nombre, password)
        if(res_db["affected"]):
            print("Bienvenido")
            self.destroy()  
            msg.showinfo(message="Has iniciado sesión", title="¡Éxito!")
        else:
            print("¡Error! Usuario o credenciales incorrectas")
    
        
 
