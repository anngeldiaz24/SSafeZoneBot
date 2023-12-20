import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from main.main_design import MainDesign
from forms.login_tradicional.form_login import FormLogin
from forms.login_faceid.form_login_faceid import FormLoginFaceId
from forms.register.form_register import Register

#La clase padre es MainDesign
class Main(MainDesign):
    
    #Inicializamos todo
    def __init__(self):
        super().__init__()
    
    def login_credenciales(self):
        form_login = FormLogin()
        form_login.run()
    
    def crear_cuenta(self):
        register = Register()
        register.run()
    
    def login_faceid(self):
        form_login_faceid = FormLoginFaceId()
        form_login_faceid.run()