import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from forms.register.form_register_design import RegisterDesign
#import cv2
from matplotlib import pyplot as plt
#from mtcnn.mtcnn import MTCNN
import os
import database as db
from tkinter import messagebox as msg
import hashlib
import re

class Register(RegisterDesign):
    #Inicializamos todo
    def __init__(self):
        super().__init__()
        self.path = "C:/Users/Angel Diaz/Desktop/SSafeZoneBot/" # angel path
        #self.path = "C:/Users/axlvi/OneDrive/Escritorio/Axl Coronado/Proyectos_GitHub/SSafeZoneBot/" # axl path
    
    def register_capture(self, nombre, password):
        # Validar el nombre de usuario y la contraseña
        if not self.validate_inputs(nombre, password):
            # Si la validación falla, muestra un mensaje de error y termina la función
            tk.messagebox.showerror("Error de validación", "Nombre de usuario o contraseña no válidos.")
            return

        cap = cv2.VideoCapture(0)
        user_reg_img = self.usuario.get()
        img = f"{user_reg_img}.jpg"

        while True:
            ret, frame = cap.read()
            cv2.imshow("Registro Facial", frame)
            if cv2.waitKey(1) == 48:
                break
        
        cv2.imwrite(img, frame)
        cap.release()
        cv2.destroyAllWindows()

        # Limpiar las variables
        self.usuario.delete(0, tk.END)
        self.password.delete(0, tk.END)
        
        pixels = plt.imread(img)
        faces = MTCNN().detect_faces(pixels)
        self.face(img, faces)

        # Hashear la contraseña antes de almacenarla
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.register_face_db(nombre, hashed_password, img)
    
    def face(self, img, faces):
        data = plt.imread(img)
        for i in range(len(faces)):
            x1, y1, ancho, alto = faces[i]["box"]
            x2, y2 = x1 + ancho, y1 + alto
            plt.subplot(1,len(faces), i + 1)
            plt.axis("off")
            face = cv2.resize(data[y1:y2, x1:x2],(150,200), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(img, face)
            plt.imshow(data[y1:y2, x1:x2])
    
    def validate_inputs(self, nombre, password):
        if len(nombre) < 6:
            tk.messagebox.showerror("Error de validación", "El nombre debe tener al menos 5 caracteres.")
            return False
            
        if not re.match("^[a-zA-Z0-9_]*$", nombre):
            tk.messagebox.showerror("Error de validación", "El nombre no puede contener caracteres especiales.")
            return False
            
        if len(password) < 8:
            tk.messagebox.showerror("Error de validación", "La contraseña debe tener al menos 7 caracteres.")
            return False
        
        return True

    def register_face_db(self, name_user, password_user, img):
        res_bd = db.registerUser(name_user, password_user, self.path + img)
        if(res_bd["affected"]):
            print("Bienvenido")
            self.destroy()  
            msg.showinfo(message="Registro exitoso", title="¡Éxito!")
        else:
            print("¡Error! Algo salio mal")
           
        os.remove(img)

