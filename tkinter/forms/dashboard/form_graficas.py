import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class GraficaDesign():
    
    def __init__(self, panel_principal):
        figura = Figure(figsize=(8, 6), dpi=100)
        ax1 = figura.add_subplot(211)
        ax2 = figura.add_subplot(212)
        
        figura.subplots_adjust(hspace=0.4)
        self.grafico_actividad_acceso(ax1)
        self.grafico_inactividad(ax2)
        
        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    #Mide la actividad de los accesos por hora al hogar y cuales son más frecuentes
    def grafico_actividad_acceso(self, ax):
        x = ["12-6am", "6am-12pm", "12-6pm", "6-9pm", "9pm-12am"]
        y = [2, 25, 11, 22, 41]
        valores_x = [1, 2, 3, 4, 5]

        colores = ['red', 'green', 'blue', 'orange', 'purple']  # Lista de colores

        ax.bar(valores_x, y, tick_label=x, color=colores, alpha=0.7)

        ax.set_title("Actividad de acceso")
        ax.set_xlabel("Horario")
        ax.set_ylabel("Número de accesos registrados")
        ax.legend()

        for i, v in enumerate(y):
            if v > ax.get_ylim()[1]:  
                ax.text(valores_x[i], v - 1, str(v), color='black', ha='center')
            else:
                ax.text(valores_x[i], v + 0.1, str(v), color='black', ha='center')

    # Mide la duración de los intervalos sin actividad en los días para implementar ahorro de energía automatizados
    def grafico_inactividad(self, ax):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        tiempo_inactividad = [5, 8, 7, 10, 15, 19, 2]
        valores_x = range(1, len(dias) + 1)  # Rango de valores para el eje x

        colores = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'pink']  # Lista de colores para las barras

        ax.bar(valores_x, tiempo_inactividad, tick_label=dias, color=colores, alpha=0.7)

        ax.set_title("Tiempo de inactividad por día")
        ax.set_xlabel("Días de la semana")
        ax.set_ylabel("Tiempo de inactividad (horas)")
        ax.legend()

        for i, v in enumerate(tiempo_inactividad):
            if v > ax.get_ylim()[1]:
                ax.text(valores_x[i], v - 1, str(v), color='black', ha='center')
            else:
                ax.text(valores_x[i], v + 0.1, str(v), color='black', ha='center')

