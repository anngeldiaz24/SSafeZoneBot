from gpiozero import Button, LED

# Configurar los pines (ajusta los numeros de pin segun tu configuracion)
boton = Button(25)
led = LED(16)

# Funcion para activar el LED cuando se presiona el boton
def encender_led():
    led.on()

# Funcion para apagar el LED cuando se suelta el boton
def apagar_led():
    led.off()

# Configurar las acciones del boton
boton.when_pressed = encender_led
boton.when_released = apagar_led

# Mantener el programa en ejecucion
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Programa terminado.")
