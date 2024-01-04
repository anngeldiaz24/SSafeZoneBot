import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class RegisterDesign:
    
    def register_capture(self, nombre, password):
        pass
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sign Up")
        self.ventana.iconbitmap("./Tkinter/img/SecurityCamera.ico")
        self.ventana.geometry("800x500")
        self.ventana.config(bg="#FFFFFF")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)             
        
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()
        
        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='#000000')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Crear Nuevo Usuario", font=(
            'Bold', 30), fg="#000000", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top
        
        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario: ", font=(
            'Bold', 14), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Bold', 14), textvariable=self.usuario)
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña: ", font=(
            'Bold', 14), fg="#000000", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Bold', 14), textvariable=self.password)
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")
        
        inicio = tk.Button(
            frame_form_fill,
            text="Registrarse",
            font=('Bold', 15),
            bg='#000000',
            bd=0,
            fg="#fff",
            command=lambda: self.register_capture(self.usuario.get(), self.password.get())
        )
        inicio.pack(fill=tk.X, padx=20, pady=20)   
        
    def run(self):
        self.ventana.mainloop()
    
    def destroy(self):
        self.ventana.destroy()