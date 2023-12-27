import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from forms.login_faceid.form_login_faceid_design import FormLoginFaceIdDesign
import cv2
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
import os
import database as db
from tkinter import messagebox as msg


class FormLoginFaceId(FormLoginFaceIdDesign):
    
    #Inicializamos todo
    def __init__(self, on_login_faceid):
        super().__init__()
        self.on_login_faceid = on_login_faceid #Callback
        
        self.path = "C:/Users/Angel Diaz/Desktop/SSafeZoneBot/" # angel path
        #self.path = "C:/Users/axlvi/OneDrive/Escritorio/Axl Coronado/Proyectos_GitHub/SSafeZoneBot/" # axl path
        self.color_success = "\033[1;32;40m"
        self.color_error = "\033[1;31;40m"
        self.color_normal = "\033[0;37;40m"
        
    def login_faceid_credentials(self, nombre):
        cap = cv2.VideoCapture(0)
        user_login = self.usuario.get()
        img = f"{user_login}_login.jpg"
        img_user = f"{user_login}.jpg"

        while True:
            ret, frame = cap.read()
            cv2.imshow("Login Facial", frame)
            if cv2.waitKey(1) == 48:
                break
        
        cv2.imwrite(img, frame)
        cap.release()
        cv2.destroyAllWindows()

        self.usuario.delete(0, tk.END)
        
        pixels = plt.imread(img)
        faces = MTCNN().detect_faces(pixels)

        self.face(img, faces)

        res_db = db.getUser(user_login, self.path + img_user)
        if(res_db["affected"]):
            my_files = os.listdir()
            if img_user in my_files:
                face_reg = cv2.imread(img_user, 0)
                face_log = cv2.imread(img, 0)

                comp = self.compatibility(face_reg, face_log)
                
                if comp >= 0.94:
                    print("{}Compatibilidad del {:.1%}{}".format(self.color_success, float(comp), self.color_normal))
                    print("Bienvenido")
                    self.destroy()  
                    msg.showinfo(message="Inicio de sesión exitoso", title="¡Éxito!")
                    self.on_login_faceid(True)
                else:
                    print("{}Compatibilidad del {:.1%}{}".format(self.color_error, float(comp), self.color_normal))
                    print("ERROR")
                    self.destroy()  
                    msg.showinfo(message="Incompatibilidad de datos", title="¡Error!")
                    self.on_login_faceid(False)
                os.remove(img_user)
        
            else:
                msg.showinfo(message="Usuario no encontrado", title="¡ERROR!")
        else:
            msg.showinfo(message="Usuario no encontrado", title="¡ERROR!")
        os.remove(img)
    
    
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
    

    def compatibility(self, img1, img2):
        orb = cv2.ORB_create()

        kpa, dac1 = orb.detectAndCompute(img1, None)
        kpa, dac2 = orb.detectAndCompute(img2, None)

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = comp.match(dac1, dac2)

        similar = [x for x in matches if x.distance < 70]
        if len(matches) == 0:
            return 0
        return len(similar)/len(matches)
