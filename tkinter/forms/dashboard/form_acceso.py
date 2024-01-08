import tkinter as tk
from PIL import ImageTk, Image
from config import COLOR_CUERPO_PRINCIPAL
import database as db
from tkinter import messagebox
from forms.register.form_register import Register

class AccesoDesign():
    def __init__(self, panel_principal, username):
        
        self.username = username 
         
        self.barra_superior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        self.labelTitulo = tk.Label(self.barra_superior, text="MIEMBROS DEL HOGAR", font=("bold", 16), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.config(pady=30) 
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)
        
        # Botón añadido a la barra superior
        self.boton_nuevo_usuario = tk.Button(
            self.barra_superior,
            text="Nuevo Usuario",
            bg="#00FF00", 
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.crear_cuenta
        )
        self.boton_nuevo_usuario.pack(side=tk.RIGHT, padx=10)
        self.boton_nuevo_usuario.bind("<Return>", (lambda event: self.crear_cuenta()))
        

        self.barra_inferior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)
        
        self.panel = panel_principal
        self.panel.config(bg=COLOR_CUERPO_PRINCIPAL)

        self.miembros = db.getUsers()
        self.imagen() 
        self.mostrar_miembros()
    
    def crear_cuenta(self):
        register = Register()
        register.run()
        
    def mostrar_miembros(self):
        icono_user = Image.open("./Tkinter/img/user3.png")
        icono_user = icono_user.resize((20, 20), Image.LANCZOS)
        icono_user = ImageTk.PhotoImage(icono_user)

        for miembro in self.miembros:
            id_usuario, nombre_usuario = miembro

            frame_miembro = tk.Frame(self.barra_inferior, bg=COLOR_CUERPO_PRINCIPAL)
            frame_miembro.pack(padx=10, pady=5, anchor='w', fill='x')

            icono_label = tk.Label(frame_miembro, image=icono_user, bg=COLOR_CUERPO_PRINCIPAL)
            icono_label.image = icono_user
            icono_label.pack(side=tk.LEFT, padx=5)

            label_miembro = tk.Label(frame_miembro, text=nombre_usuario, font=("Arial", 12), bg=COLOR_CUERPO_PRINCIPAL)
            label_miembro.pack(side=tk.LEFT)

            btn_eliminar = tk.Button(
                frame_miembro, 
                text="Eliminar", 
                command=lambda id=id_usuario, name=nombre_usuario: self.eliminar_usuario(id, name), 
                bg="#FF5733", 
                fg="white", 
                font=("Arial", 10, "bold")
            )
            btn_eliminar.pack(side=tk.RIGHT) 

            if self.username == nombre_usuario:
                btn_eliminar.config(state=tk.DISABLED, bg="grey", fg="white")
                
    def eliminar_usuario(self, id_usuario, nombre_usuario):
        db.deleteUser(id_usuario)
        messagebox.showinfo("Eliminado", f"El usuario {nombre_usuario} ha sido eliminado exitosamente.")
        self.actualizar_lista_usuarios()
    
    def actualizar_lista_usuarios(self):
        # Eliminar todos los widgets hijos de self.barra_inferior
        for widget in self.barra_inferior.winfo_children():
            widget.destroy()

        # Actualizar la lista de usuarios
        self.miembros = db.getUsers()
        self.mostrar_miembros()
            
    def imagen(self):
        # Crear un nuevo Frame
        otro_frame = tk.Frame(self.panel, bg=COLOR_CUERPO_PRINCIPAL)
        otro_frame.pack(side=tk.LEFT, fill='both', expand=True)

        # Agregar una imagen al nuevo Frame
        imagen = Image.open("./Tkinter/img/familia3.jpg")  
        imagen = imagen.resize((450, 225), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)

        label_imagen = tk.Label(otro_frame, image=imagen, bg=COLOR_CUERPO_PRINCIPAL)
        label_imagen.image = imagen
        label_imagen.pack()