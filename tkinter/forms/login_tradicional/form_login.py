import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import messagebox as msg
from forms.login_tradicional.form_login_design import FormLoginDesign
from forms.login_faceid.form_login_faceid import FormLoginFaceId
from forms.register.form_register import Register
import database as db
import hashlib


class FormLogin(FormLoginDesign):
    
    #Inicializamos todo
    def __init__(self, on_login):
        super().__init__()
        self.on_login = on_login  # Callback para comunicar el resultado de autenticación

    
    def crear_cuenta(self):
        register = Register()
        register.run()
    
    def login_credentials(self, nombre, password):
        # Obtener el valor de las variables StringVar
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        res_db = db.getUserCredentials(nombre, hashed_password)
        if(res_db["affected"]):
            #print("Bienvenido")
            self.destroy()  
            #msg.showinfo(message="Has iniciado sesión", title="¡Éxito!")
            nombre_de_usuario = nombre  # Obtén el nombre de usuario
            self.on_login(True, nombre_de_usuario)  # Ejecuta el callback con True y el nombre de usuario
        else:
            print("¡Error! Usuario o credenciales incorrectas")
            msg.showinfo(message="¡Error! Usuario o credenciales incorrectas", title="¡Error!")
            self.on_login(False, None) 
    
        
 
