import tkinter as tk
from tkinter import font
from tkinter.font import BOLD
from config import COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL, COLOR_BARRA_SUPERIOR
import util.generic as utl
from forms.dashboard.form_hogar import HogarDesign
from forms.dashboard.form_graficas import GraficaDesign
from forms.dashboard.form_acceso import AccesoDesign

class Panel(tk.Tk):
    
                                      
    def __init__(self, username): 
        #Inicializamos el objeto heredado
        super().__init__()  
        self.username = username
        #print(self.username)
        #Primero cargamos la imagen   
        self.logo = utl.leer_imagen("./tkinter/img/familia.jpg", (600, 400))
        self.perfil = utl.leer_imagen("./tkinter/img/user2.png", (105, 105))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral() 
        self.controles_cuerpo()
        
    def config_window(self):
        #Configuracion inicial de la ventana                      
        self.title('Samsung Safe Zone Management - Dashboard')
        #self.iconbitmap("./tkinter/img/SecurityCamera.ico")
        w, h = 1024, 600                            
        self.geometry("%dx%d+0+0" % (w, h))
        self.resizable(width=0, height=0) 
        utl.centrar_ventana(self, w, h)          

    def paneles(self):
        #Crear paneles
        self.barra_superior = tk.Frame(
            self,
            bg=COLOR_BARRA_SUPERIOR,
            height=50
        )
        self.barra_superior.pack(side=tk.TOP, fill='both')
        
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150) 
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        #Configuracion
        font_awesome = font.Font(family='FontAwesome', size=12)
        
        #Etiqueta que se guarda en la barra superior
        self.labelTitulo = tk.Label(self.barra_superior, text="SAMSUNG")
        self.labelTitulo.config(
            fg="#fff",
            font=("Bold", 15), 
            bg = COLOR_BARRA_SUPERIOR, 
            pady=10, 
            width=16)
        self.labelTitulo.pack(side=tk.LEFT)
    
        self.buttonMenuLateral = tk.Button(self.barra_superior, 
                                           text='≡',
                                           command=self.toggle_panel,
                                           font=font_awesome,
                                           bd=0,
                                           bg=COLOR_BARRA_SUPERIOR,
                                           fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
        #Etiqueta de informacion
        self.labelTitulo = tk.Label(self.barra_superior, text="samsung@samsung.com")
        self.labelTitulo.config(
            fg="#fff",
            font=("Bold", 10), 
            bg = COLOR_BARRA_SUPERIOR, 
            pady=10, 
            width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
        
    def controles_menu_lateral(self):
        #Configuración menu lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family="FontAwesome", size=15)
        
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        
        username_label = tk.Label(self.menu_lateral, text=f"Usuario: {self.username}", fg="white", bg=COLOR_MENU_LATERAL)
        username_label.pack(side=tk.TOP, pady=(0, 10))  # Ajustar el espaciado según sea necesario
        
        #Botones
        self.buttonInicio = tk.Button(self.menu_lateral)
        self.buttonHogar = tk.Button(self.menu_lateral)
        self.buttonDashboard = tk.Button(self.menu_lateral)
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)
        
        buttons_info = [
            ("Inicio", self.buttonInicio,self.inicio),
            ("Dashboard", self.buttonDashboard,self.graficas),
            ("Hogar", self.buttonHogar,self.hogar),
            ("Acceso", self.buttonPicture,self.acceso),
        ]
        
        #iterar las opciones
        for text, button, comando in buttons_info:
            self.configurar_button_menu(button, text, font_awesome, ancho_menu, alto_menu, comando)
    
    def controles_cuerpo(self):
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                        bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        titulo = tk.Label(self.cuerpo_principal, text="¡BIENVENIDO A SSAFE ZONE!", font=("bold", 16), bg=COLOR_CUERPO_PRINCIPAL)
        titulo.place(relx=0.5, rely=0.1, anchor='center')

        
    def configurar_button_menu(self, button, text, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"{text}", anchor="w", font=font_awesome, bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu, command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
    
    def bind_hover_events(self, button):
        #Asociar eventer Enter y leave con la función dinamica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    def on_enter(self, event, button):
        #Hover con estilo
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")

    def on_leave(self, event, button):
        #Hover sin estilo
        button.config(bg=COLOR_MENU_LATERAL, fg="white")
        
    def toggle_panel(self):
        #Alternar visibilidad del menu lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill="y")
    
    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
    
    """ SUBMENU """
    def inicio(self):
        self.limpiar_panel(self.cuerpo_principal)
        self.controles_cuerpo()
        
    def hogar(self):
        self.limpiar_panel(self.cuerpo_principal)
        HogarDesign(self.cuerpo_principal)
         
    def graficas(self):
        self.limpiar_panel(self.cuerpo_principal)
        GraficaDesign(self.cuerpo_principal)
    
    def acceso(self):
        self.limpiar_panel(self.cuerpo_principal)
        AccesoDesign(self.cuerpo_principal, self.username)

    def run(self):
        self.mainloop()
    