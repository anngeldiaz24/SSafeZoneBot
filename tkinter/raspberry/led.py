from gpiozero import Button, LED

# Configurar los pines (ajusta los n�meros de pin seg�n tu configuraci�n)
boton = Button(25)
led = LED(16)

# Funci�n para activar el LED cuando se presiona el bot�n
def encender_led():
    led.on()

# Funci�n para apagar el LED cuando se suelta el bot�n
def apagar_led():
    led.off()

# Configurar las acciones del bot�n
boton.when_pressed = encender_led
boton.when_released = apagar_led

# Mantener el programa en ejecuci�n
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Programa terminado.")
