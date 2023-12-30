import os, time, locale
import threading # para crear hilos
from dotenv import load_dotenv # para cargar las variables del .env
from datetime import datetime # para acceder a la fecha y hora del sistema
import hashlib # para hashear la contraseña del usuario
import telebot # para manejar la API de Telegram
from telebot import types
from telebot.types import BotCommand # para crear los comandos del menú de telegram
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import ForceReply # para citar un mensaje
from telebot.types import ReplyKeyboardRemove # para eliminar botones
from tkinter.database import registerUserBot # para registrar al usuario desde el bot

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Accedemos a las variables de entorno
TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME') # Nombre de usuario de nuestro bot
AXL_CHAT_ID = os.getenv('AXL_CHAT_ID') # Id único de nuestro chat (axl)
ANGEL_CHAT_ID = os.getenv('ANGEL_CHAT_ID') # Id único de nuestro chat (angel)
DANIEL_CHAT_ID = os.getenv('DANIEL_CHAT_ID') # Id único de nuestro chat (daniel)

# Configurar el locale para obtener la fecha y hora en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Conexión con nuestro BOT
bot = telebot.TeleBot(TOKEN)
# Variable global en la que guardaremos los datos del usuario registrado
usuarios = {}

# Responde al comando /start y envia el menu de opciones al usuario
@bot.message_handler(commands=['start'])
def send_start_command(message):
    #print(message.chat.id)
    user = message.from_user # Nombre de usuario en Telegram del cliente
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, f'¡Hola {user.first_name}! 👋 Bienvenido a tu bot de seguridad {BOT_USERNAME}.')

    # Inicializa el contenido (cuerpo) del menú
    markup = types.InlineKeyboardMarkup(row_width=2)

    # Creamos los botones y las opciones disponibles del menú
    btn_activar_alarma = types.InlineKeyboardButton('🚨 Activar alarma 🚨', callback_data='activar_alarma')
    btn_llamar_policia = types.InlineKeyboardButton('🚓 Llamar a la policia 🚓', callback_data='llamar_policia')
    btn_monitorear_camara = types.InlineKeyboardButton('📹 Monitorear camara 📹', callback_data='monitorear_camara')
    btn_bloquear_puertas_ventanas = types.InlineKeyboardButton('🔒 Bloquear puertas y ventanas 🔒', callback_data='bloquear_puertas_ventanas')
    btn_cerrar = types.InlineKeyboardButton('❌', callback_data='cerrar')

    # Agregamos los botones del menú al markup
    markup.add(btn_activar_alarma, btn_llamar_policia, btn_monitorear_camara, btn_bloquear_puertas_ventanas, btn_cerrar)

    # Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Qué deseas realizar?\n<b>Selecciona una opción:</b>", parse_mode="html", reply_markup=markup)

# Responde al comando /register
@bot.message_handler(commands=['register'])
def send_register_command(message):
    """ Pregunta el username del usuario a registrar """
    markup = ForceReply() # Posiciona como respuesta al mensaje enviado
    bot.send_chat_action(message.chat.id, "typing")
    mensaje_nombre_usuario = bot.send_message(message.chat.id, "1️⃣ Escribe un nombre de usuario", reply_markup=markup)
    # Pasamos al siguiente paso (preguntar la contraseña) una vez que el usuario escriba su nombre de usuario
    bot.register_next_step_handler(mensaje_nombre_usuario, preguntar_contrasena)

def preguntar_contrasena(message):
    """ Pregunta la contraseña del usuario a registrar """
    # Creamos un diccionario dentro del diccionario 'usuarios' propio del usuario que utiliza el comando
    usuarios[message.chat.id] = {}
    # Guardamos el 'username' como una key y la respuesta del usuario como el valor
    usuarios[message.chat.id]["username"] = message.text
    global nombre_usuario
    nombre_usuario = message.text
    markup = ForceReply() # Posiciona como respuesta al mensaje enviado
    bot.send_chat_action(message.chat.id, "typing")
    mensaje_contrasena = bot.send_message(message.chat.id, f'2️⃣ Escribe una contraseña para {nombre_usuario}', reply_markup=markup)
    # Pasamos al siguiente paso (validar registro) una vez que el usuario escriba su contraseña
    bot.register_next_step_handler(mensaje_contrasena, validar_registro)

def validar_registro(message):
    # Si la contraseña no es mayor a 3 caracteres
    if not len(message.text) > 3:
        # Informamos del error y volvemos a preguntar
        markup = ForceReply() # Forzamos a que vuelva a respondar el mensaje enviado
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_error = bot.send_message(message.chat.id, f'🔴 ERROR: Debes escribir al menos 4 caracteres.\nEscribe una contraseña para {nombre_usuario}', reply_markup=markup)
        # Volvemos a validar la contraseña llamando a la función
        bot.register_next_step_handler(mensaje_error, validar_registro)
    else: # Si se introdujo la contraseña correctamente
        # Guardamos el 'password' como una key y la respuesta del usuario como el valor
        usuarios[message.chat.id]["password"] = message.text
        # Definimos 2 botones
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True, 
            input_field_placeholder="Pulsa un botón",
            resize_keyboard=True,
            row_width=2
            )
        markup.add("Confirmar registro", "Cancelar registro")
        # Preguntamos por confirmar
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_botones = bot.send_message(message.chat.id, '3️⃣ ¿Quieres registrar a este usuario con las credenciales proporcionadas?', reply_markup=markup)
        # Registramos las respuestas en la función indicada
        bot.register_next_step_handler(mensaje_botones, guardar_datos_usuario)

def guardar_datos_usuario(message):
    """ Guardamos los datos introducidos por el usuario """
    # Si la respuesta de los botones no son validas
    if message.text != "Confirmar registro" and message.text != "Cancelar registro":
        # Informamos del error y volvemos a preguntar
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_error = bot.send_message(message.chat.id, '🔴 ERROR: Respuesta no válida.\nPulsa un botón')
        # # Volvemos a validar la respuesta llamando a la función
        bot.register_next_step_handler(mensaje_error, guardar_datos_usuario)  
    elif message.text == "Confirmar registro": # Si la respuesta es "Confirmar registro"
        # Se muestra los datos proporcionados del registro
        bot.send_chat_action(message.chat.id, "typing")
        #usuarios[message.chat.id]["verify"] = message.text
        texto = '✅ Registro exitoso ✅\n'
        texto+= 'Datos introducidos:\n'
        texto+= f'<code>NOMBRE DE USUARIO:</code> {usuarios[message.chat.id]["username"]}\n'
        texto+= f'<code>CONTRASEÑA.......:</code> {usuarios[message.chat.id]["password"]}\n'
        #texto+= f'<code>VERIFICACION.....:</code> {usuarios[message.chat.id]["verify"]}\n'
        markup = ReplyKeyboardRemove() # Elimina la botonera de telegram (ReplyKeyboardMarkup)
        bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
        print(usuarios) # Imprime en consola el diccionario del usuario a registrar
        # Obtenemos el valor del 'username'
        username = usuarios[message.chat.id]["username"]
        # Obtenemos el valor del 'password'
        password = usuarios[message.chat.id]["password"]
        # Hasheamos la password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(username) # Imprime en consola el username del usuario a registrar
        print(password) # Imprime en consola el password del usuario a registrar
        print(hashed_password) # Imprime en consola la password hasheada del usuario a registrar
        # Registramos al usuario con la función que viene desde database.py
        registerUserBot(username, hashed_password)
        del usuarios[message.chat.id] # Borramos de memoria el objeto (diccionario) creado
    elif message.text == "Cancelar registro": # Si la respuesta es "Cancelar registro"
        bot.send_chat_action(message.chat.id, "typing")
        markup = ReplyKeyboardRemove() # Elimina la botonera de telegram (ReplyKeyboardMarkup)
        bot.send_message(message.chat.id, "✅ Registro cancelado exitosamente ✅", parse_mode="html", reply_markup=markup)

# Responde al comando /foto
@bot.message_handler(commands=['photo'])
def send_image_command(message):
    bot.send_chat_action(message.chat.id, "upload_photo")
    img_url = 'https://static.vecteezy.com/system/resources/previews/020/927/449/original/samsung-brand-logo-phone-symbol-name-white-design-south-korean-mobile-illustration-with-black-background-free-vector.jpg'
    img_path = open("./public/images/samsung.jpg", "rb")
    bot.send_photo(chat_id=message.chat.id, photo=img_path, caption=get_datetime())

# Responde al comando /document
@bot.message_handler(commands=['document'])
def send_document_command(message):
    bot.send_chat_action(message.chat.id, "upload_document")
    file = open("./public/docs/Sistema de Seguridad con Raspberry - SAMSUNG.pdf", "rb")
    bot.send_document(chat_id=message.chat.id, document=file, caption="Guía de casos de uso del sistema de seguridad de SSafeZoneBot")

# Responde al comando /help
@bot.message_handler(commands=['help'])
def send_help_command(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, 'Puedes interactuar conmigo usando comandos. Por ahora, solo respondo a /start y /help')

# Responde a los mensajes de texto que no son comandos
@bot.message_handler(content_types=["text"])
def send_mensajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_comando_disponible = bot.send_message(message.chat.id, "Escribe un comando disponible.")
        time.sleep(5)
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_elimina = bot.send_message(message.chat.id, "Eliminando mensajes invalidos: 3", parse_mode="html")
        time.sleep(1)
        bot.edit_message_text("Eliminando mensajes invalidos: 2", message.chat.id, mensaje_elimina.message_id)
        time.sleep(1)
        bot.edit_message_text("Eliminando mensajes invalidos: 1", message.chat.id, mensaje_elimina.message_id)
        time.sleep(1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, mensaje_comando_disponible.message_id)
        bot.delete_message(message.chat.id, mensaje_elimina.message_id)
    else:
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_comando_invalido = bot.send_message(message.chat.id, "Este no es un comando valido. Por favor, escribe un comando valido que inicie con '<b>/</b>'.", parse_mode="html")
        time.sleep(5)
        bot.send_chat_action(message.chat.id, "typing")
        mensaje_elimina = bot.send_message(message.chat.id, "Eliminando mensajes invalidos: 3", parse_mode="html")
        time.sleep(1)
        bot.edit_message_text("Eliminando mensajes invalidos: 2", message.chat.id, mensaje_elimina.message_id)
        time.sleep(1)
        bot.edit_message_text("Eliminando mensajes invalidos: 1", message.chat.id, mensaje_elimina.message_id)
        time.sleep(1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, mensaje_comando_invalido.message_id)
        bot.delete_message(message.chat.id, mensaje_elimina.message_id)

# Maneja todos los demás tipos de contenido (mensajes).
@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 
                                                               'location', 'contact', 'sticker'])
def send_default_command(message):
    bot.send_chat_action(message.chat.id, "typing")
    mensaje_default = bot.send_message(message.chat.id, "Por ahora, solo recibo mensajes de texto.\nPor favor, usa los comandos que están disponibles en el menú interactivo.")
    time.sleep(5)
    bot.send_chat_action(message.chat.id, "typing")
    mensaje_elimina = bot.send_message(message.chat.id, "Eliminando mensajes invalidos: 3", parse_mode="html")
    time.sleep(1)
    bot.edit_message_text("Eliminando mensajes invalidos: 2", message.chat.id, mensaje_elimina.message_id)
    time.sleep(1)
    bot.edit_message_text("Eliminando mensajes invalidos: 1", message.chat.id, mensaje_elimina.message_id)
    time.sleep(1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, mensaje_default.message_id)
    bot.delete_message(message.chat.id, mensaje_elimina.message_id)

# Responde a cada una de las opciones del menú que son enviadas con /start
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'activar_alarma':
        bot.answer_callback_query(call.id, "Se ha enviado la petición para que suene la alarma", show_alert=True)
        bot.send_chat_action(call.message.chat.id, "typing")
        respuesta_alarma = bot.send_message(call.message.chat.id, "Intentando establecer conexión con el sistema...")
        time.sleep(3)
        bot.edit_message_text("Alarma en curso...", call.message.chat.id, respuesta_alarma.message_id)
    elif call.data == 'llamar_policia':
        bot.send_chat_action(call.message.chat.id, "typing")
        bot.answer_callback_query(call.id, "Se ha enviado la petición para que se establezca la llamada con la policia", show_alert=True)
        respuesta_policia = bot.send_message(call.message.chat.id, "Intentando establecer conexión con el sistema...")
        time.sleep(3)
        bot.edit_message_text("Llamada en curso...", call.message.chat.id, respuesta_policia.message_id)
    elif call.data == 'monitorear_camara':
        bot.send_chat_action(call.message.chat.id, "typing")
        bot.answer_callback_query(call.id, "Monitoreando camara...", show_alert=True)
    elif call.data == 'bloquear_puertas_ventanas':
        bot.send_chat_action(call.message.chat.id, "typing")
        bot.answer_callback_query(call.id, "Puertas y ventanas bloqueadas", show_alert=True)
    elif call.data == 'cerrar':
        bot.delete_message(call.from_user.id, call.message.id)
        return

""" FUNCIONES ADICIONALES """
# Obtiene la fecha y hora actual del sistema
def get_datetime():
    fecha_hora_actual = datetime.now()

    # Formatear la fecha y hora en un formato legible
    formato_fecha_hora = fecha_hora_actual.strftime('%A, %d de %B de %Y a las %H:%M horas')

    return formato_fecha_hora

def recibir_mensajes():
    # Bucle infinito que comprueba si hay nuevos mensajes en el bot
    bot.infinity_polling()

""" MODULO MAIN (PRINCIPAL) DEL PROGRAMA """
if __name__ == "__main__":
    # Configuramos los comandos disponibles del bot
    bot.set_my_commands([
        BotCommand("/start", "ve las opciones disponibles que tengo para ti"),
        BotCommand("/register", "registra a un nuevo usuario"),
        BotCommand("/photo", "toma una foto actual de la cámara instalada"),
        BotCommand("/document", "envia la guía de casos de uso del funcionamiento del sistema"),
        BotCommand("/help", "obten más información de los comandos disponibles")
    ])
    print('Iniciando el bot')
    #bot.polling(none_stop=True)
    bot_thread = threading.Thread(name="bot_thread", target=recibir_mensajes)
    bot_thread.start()
    print('Bot iniciado')

    # Se notifica al usuario que el bot se encuentra en funcionamiento
    bot.send_message(AXL_CHAT_ID, f'🟢 ¡En estos momentos me encuentro disponible para ti!\nAtentamente: <b>{BOT_USERNAME}</b>', parse_mode="html")
    bot.send_message(ANGEL_CHAT_ID, f'🟢 ¡En estos momentos me encuentro disponible para ti!\nAtentamente: <b>{BOT_USERNAME}</b>', parse_mode="html")
    bot.send_message(DANIEL_CHAT_ID, f'🟢 ¡En estos momentos me encuentro disponible para ti!\nAtentamente: <b>{BOT_USERNAME}</b>', parse_mode="html")