from gpiozero import Servo, LED, Buzzer
from gpiozero import MotionSensor, Button
from time import sleep
import time

movimiento_detectado = False  # Inicialmente, no hay movimiento

# Función que detecta movimiento en el sensor de la raspberry
def detectar_movimiento():
    global movimiento_detectado # Variable global para indicar si existe movimiento en la raspberry

    # Si se detecta movimiento
    if movimiento_detectado:
        # Retorna true y se asigna a false la variable
        movimiento_detectado = False
        return True
    else: # Si no, retorna false
        return False

 # Configuracion del servo
servo_pin1 = 18
servo_pin2 =17
servo_pin3 = 20
servo_pin4 =21
servo_pin5 =22
servo_pin6 =23
servo1 = Servo(servo_pin1)
servo2 = Servo(servo_pin2)
servo3 = Servo(servo_pin3)
servo4 = Servo(servo_pin4)
servo5 = Servo(servo_pin5)
servo6 = Servo(servo_pin6)

# Definir pines para el sensor de la alarma
led_rojo = LED(16)
led_azul = LED(13)
buzzer = Buzzer(19)

# Configurar el LED en el pin 25
led = LED(25)

def abrirServo():
    # Abrir el servo (posicion a 0 grados)
    print("abrirServo funcionando")
    
    servo1.min()
    servo2.min()
    servo3.min()
    servo4.max()
    servo5.max()
    servo6.max()
    sleep(1)

def cerrarServo():
    # Cerrar el servo (posicion a 180 grados)
    print("cerrarServo funcionando")
    servo1.max()
    servo2.max()
    servo3.max()
    servo4.min()
    servo5.min()
    servo6.min()
    sleep(1)

# Activar la alarma
def activarAlarma():
    print("activarAlarma funcionando")
    tiempo_total = 10  
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

def desactivarAlarma():
    print("desactivarAlarma funcionando")
    led_rojo.off()
    led_azul.off()
    buzzer.off()

def monitorearCamara():
    print("monitorearCamara funcionando")

def activarSensorMovimiento():
    global movimiento_detectado
    print("activarSensorMovimiento funcionando")
    pir = MotionSensor(4)
    print("Esperar el PIR")
    pir.wait_for_no_motion()
    while True:
        print("Listo")
        pir.wait_for_motion()
        print("Movimiento detectado")
        movimiento_detectado = True
        time.sleep(5)
        break

def desactivarSensorMovimiento():
    global movimiento_detectado
    print("desactivarSensorMovimiento funcionando")
    pir = MotionSensor(4)
    print("Desactivar el PIR")
    pir.when_motion = lambda: None  # Ignorar eventos de movimiento
    pir.when_no_motion = lambda: None  # Ignorar eventos de no movimiento
    movimiento_detectado = False

def luzAlarma():
    print("LuzAlarma funcionando")
    tiempo_total = 10  
    tiempo_parpeo = 0.5  

    # Bucle para parpadear
    while tiempo_total > 0:
        led.on()
        sleep(tiempo_parpeo)
        led.off()
        break
def encenderLucesDomesticas():
    print("encenderLucesDomesticas funcionando")
    # Encender el LED
    led.on() 
def apagarLucesDomesticas():
    print("apagarLucesDomesticas funcionando")
    led.off() 

# Para probar la activacion constante del PIR
#activarSensorMovimiento()

# Para probar la desactivacion del PIR
#desactivarSensorMovimiento()