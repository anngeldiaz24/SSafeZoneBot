import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from forms.register.form_register import Register

class MainDesign:
    
    def crear_cuenta(self):
        pass

    def login_credenciales(self):
        pass
    
    def login_faceid(self):
        pass


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Samsung Safe Zone")
        self.ventana.geometry("800x500")
        self.ventana.config(bg="#FFFFFF")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        
        logo =utl.leer_imagen("./Tkinter/img/samsung1.jpg", (200, 200))
                        
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=50,
                              relief=tk.SOLID, padx=10, pady=10, bg='#000000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#000000')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='#000000')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="¡Bienvenido!", font=(
            'Bold', 30), fg="#000000", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top
        
        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        inicio = tk.Button(frame_form_fill, text="Crear Cuenta", font=(
            'Bold', 15), bg='#000000', bd=0, fg="#fff", command=self.crear_cuenta)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.crear_cuenta()))
        
        inicio = tk.Button(frame_form_fill, text="Iniciar Sesión con Credenciales", font=(
            'Bold', 15), bg='#000000', bd=0, fg="#fff", command=self.login_credenciales)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.login_credenciales()))
        
        inicio = tk.Button(frame_form_fill, text="Iniciar Sesión con FACE ID", font=(
            'Bold', 15), bg='#000000', bd=0, fg="#fff", command=self.login_faceid)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.login_faceid()))
        
        
        self.ventana.mainloop()


    