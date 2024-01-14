import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL
from PIL import Image, ImageTk

class DomoticaDesign():
    
    def __init__(self, panel_principal):
        
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        self.barra_inferior = tk.Frame(panel_principal,bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)
        
        # Título con más espacio en la parte superior
        self.labelTitulo = tk.Label(self.barra_superior, text="PÁGINA EN CONSTRUCCIÓN", font=("bold", 16), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.config(pady=30)  
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)
        
        frame_imagen = tk.Frame(self.barra_inferior, bg=COLOR_CUERPO_PRINCIPAL)
        frame_imagen.pack(side=tk.LEFT, fill='both', expand=True)

        imagen = Image.open("./tkinter/img/construccion.png")  
        imagen = imagen.resize((400, 400), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)

        label_imagen = tk.Label(frame_imagen, image=imagen, bg=COLOR_CUERPO_PRINCIPAL)
        label_imagen.image = imagen
        label_imagen.pack()