from gpiozero import MotionSensor
import time

def activar_pir():
    pir = MotionSensor(4)
    print("Esperar el PIR")
    pir.wait_for_no_motion()
    while True:
        print("Listo")
        pir.wait_for_motion()
        print("Movimiento detectado")
        time.sleep(1)

def desactivar_pir():
    pir = MotionSensor(4)
    print("Desactivar el PIR")
    pir.when_motion = lambda: None  # Ignorar eventos de movimiento
    pir.when_no_motion = lambda: None  # Ignorar eventos de no movimiento
