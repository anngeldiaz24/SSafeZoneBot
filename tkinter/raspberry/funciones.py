from gpiozero import Servo, LED, Buzzer
from gpiozero import MotionSensor, Button
from time import sleep

 # Configuracion del servo
""" servo_pin1 = 18
servo_pin2 =17
servo_pin3 = 20
servo_pin4 =21
servo_pin5 =22
servo1 = Servo(servo_pin1)
servo2 = Servo(servo_pin2)
servo3 = Servo(servo_pin3)
servo4 = Servo(servo_pin4)
servo5 = Servo(servo_pin5) """

def abrirServo():

    # Abrir el servo (posicion a 0 grados)
    print("abrirServo funcionando")
    # servo1.min()
    # servo2.min()
    # servo3.min()
    # servo4.min()
    # servo5.min()
    # sleep(1)

def cerrarServo():
    # Cerrar el servo (posicion a 180 grados)
    print("cerrarServo funcionando")
    # servo1.max()
    # servo2.max()
    # servo3.max()
    # servo4.max()
    # servo5.max()
    # sleep(1)

# Definir pines
""" led_rojo = LED(16)
led_azul = LED(13)
buzzer = Buzzer(19) """

# Activar la alarma
def activarAlarma():
    print("activarAlarma funcionando")
    """ tiempo_total = 10  
    tiempo_parpeo = 0.5  

    # Bucle para parpadear
    while tiempo_total > 0:
        led_rojo.on()
        sleep(tiempo_parpeo)
        led_rojo.off()
        
        led_azul.on()
        sleep(tiempo_parpeo)
        led_azul.off()
        
        buzzer.toggle()  # Buzzer prendido y apagado
        tiempo_total -= tiempo_parpeo * 2  # Tiempo de parpadeos

    # Apagar la alarma despues de usarla
    led_rojo.off()
    led_azul.off()
    buzzer.off() """

def desactivarAlarma():
    print("desactivarAlarma funcionando")

def llamarPolicia():
    print("llamarPolicia funcionando")

def monitorearCamara():
    print("monitorearCamara funcionando")