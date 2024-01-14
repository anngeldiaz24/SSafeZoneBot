import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL
#import cv2
from PIL import Image, ImageTk
import datetime
import os
import raspberry.funciones as rp
from raspberry.llamada_policia import llamarPolicia

class HogarDesign():
    
    def __init__(self, panel_principal):
        self.barra_superior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        self.barra_inferior = tk.Frame(panel_principal,bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)
        
        # Título con más espacio en la parte superior
        self.labelTitulo = tk.Label(self.barra_superior, text="PROTEGE TU HOGAR", font=("bold", 16), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.config(pady=30)  
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Frame contenedor para el video en la barra superior
        self.frame_video = tk.Frame(self.barra_superior, width=650, height=350)  # Ancho y alto según el tamaño del video
        self.frame_video.pack(side=tk.LEFT, padx=70)  # Alineado a la izquierda

        # Label para mostrar el video en el frame del video
        self.label_video = tk.Label(self.frame_video)
        self.label_video.pack()  # Por defecto, se centrará en el frame
    
        # Contenedor para los botones 1, 2 y 3
        contenedor_botones1_3 = tk.Frame(self.barra_inferior)
        contenedor_botones1_3.pack(side=tk.LEFT)

        # Contenedor para los botones 4, 5 y 6
        contenedor_botones4_6 = tk.Frame(self.barra_inferior)
        contenedor_botones4_6.pack(side=tk.LEFT)

        # Contenedor para los botones 2 y 5
        contenedor_botones2_5 = tk.Frame(self.barra_inferior)
        contenedor_botones2_5.pack(side=tk.LEFT)

        self.btn1 = tk.Button(contenedor_botones1_3, text="Activar alarma", command=self.funcion_btn1, font=("Arial", 15), bg="black", fg="white")
        self.btn1.pack(side=tk.TOP, padx=20, pady=5)
        self.btn1.config(width=20)

        self.btn2 = tk.Button(contenedor_botones2_5, text="Llamar a la policia", command=self.funcion_btn2, font=("Arial", 15), bg="black", fg="white")
        self.btn2.pack(side=tk.TOP, padx=10, pady=5)
        self.btn2.config(width=20)

        self.btn3 = tk.Button(contenedor_botones1_3, text="Desactivar alarma", command=self.funcion_btn3, font=("Arial", 15), bg="black", fg="white")
        self.btn3.pack(side=tk.TOP, padx=20, pady=5)
        self.btn3.config(width=20)

        self.btn4 = tk.Button(contenedor_botones4_6, text="Desbloquear entradas", command=self.funcion_btn4, font=("Arial", 15), bg="black", fg="white")
        self.btn4.pack(side=tk.TOP, padx=10, pady=5)
        self.btn4.config(width=20)

        self.btn5 = tk.Button(contenedor_botones2_5, text="Grabar contenido", command=self.funcion_btn5, font=("Arial", 15), bg="black", fg="white")
        self.btn5.pack(side=tk.TOP, padx=10, pady=5)
        self.btn5.config(width=20)

        self.btn6 = tk.Button(contenedor_botones4_6, text="Bloquear entradas", command=self.funcion_btn6, font=("Arial", 15), bg="black", fg="white")
        self.btn6.pack(side=tk.TOP, padx=10, pady=5)
        self.btn6.config(width=20)

        # Iniciar la transmisión de video
        self.mostrar_video()
        #Función de capturar la grabación
        self.grabando = False
        self.panel = panel_principal
        
        
    def mostrar_video(self):
        # Iniciar captura de video desde la cámara
        captura = cv2.VideoCapture(0)  # 0 para la cámara predeterminada

        def actualizar_video():
            ret, frame = captura.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (650, 350))  # Redimensionar el fotograma
                imagen = Image.fromarray(frame)
                imagen = ImageTk.PhotoImage(imagen)

                # Mostrar el video en el label dentro del frame de video
                self.label_video.img = imagen
                self.label_video.config(image=imagen)

            # Actualizar el video después de un breve tiempo
            self.label_video.after(10, actualizar_video)

        actualizar_video()
    
    def funcion_btn1(self):
        rp.activarAlarma()

    def funcion_btn2(self):
        llamarPolicia()
    
    def funcion_btn3(self):
        rp.desactivarAlarma()

    def funcion_btn4(self):
        rp.abrirServo()
    
    def funcion_btn5(self):
        if not self.grabando:
            self.grabando = True
            now = datetime.datetime.now()
            nombre_video = now.strftime("%Y-%m-%d_%H-%M-%S") + '.mp4'
            carpeta = 'records'  # Nombre de la carpeta
            ruta_carpeta = os.path.join(os.getcwd(), carpeta)  # Ruta completa de la carpeta
            if not os.path.exists(ruta_carpeta):  # Si la carpeta no existe, créala
                os.makedirs(ruta_carpeta)

            ruta_video = os.path.join(ruta_carpeta, nombre_video)  # Ruta completa del video

            self.out = cv2.VideoWriter(ruta_video, cv2.VideoWriter_fourcc(*'mp4v'), 10.0, (650, 350))

            def grabar_video():
                ret, frame = self.captura.read()
                if ret:
                    frame = cv2.resize(frame, (650, 350))  # Redimensionar el fotograma
                    self.out.write(frame)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    imagen = Image.fromarray(frame)
                    imagen = ImageTk.PhotoImage(imagen)
                    self.label_video.img = imagen
                    self.label_video.config(image=imagen)
                if self.grabando:
                    self.panel.after(100, grabar_video)  # Vuelve a llamar la función si está grabando
                else:
                    self.out.release()  # Liberar recursos
                    self.captura.release()  # Liberar recursos

            self.captura = cv2.VideoCapture(0)
            grabar_video()
        else:
            self.grabando = False  # Detener la grabación
            self.mostrar_video()
                
    def funcion_btn6(self):
        rp.cerrarServo()