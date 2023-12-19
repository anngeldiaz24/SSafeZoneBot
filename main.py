import telebot
from telebot import types
import time
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Accedemos a las variables de entorno
TOKEN = os.getenv('token')
BOT_USERNAME = os.getenv('bot_username') # Nombre de usuario de nuestro bot

# Conexión con nuestro BOT
bot = telebot.TeleBot(TOKEN)

# Responde al comando /start y envia el menu de opciones al usuario
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user # Nombre de usuario en Telegram del cliente
    bot.reply_to(message, f'¡Hola {user.first_name}! Bienvenido a tu bot de seguridad {BOT_USERNAME}.')

    # Inicializa el contenido (cuerpo) del menú
    markup = types.InlineKeyboardMarkup(row_width=1)

    # Creamos los botones y las opciones disponibles del menú
    btn_activar_alarma = types.InlineKeyboardButton('Activar alarma', callback_data='activar_alarma')
    btn_llamar_policia = types.InlineKeyboardButton('Llamar a la policia', callback_data='llamar_policia')
    btn_monitorear_camara = types.InlineKeyboardButton('Monitorear camara', callback_data='monitorear_camara')
    btn_bloquear_puertas_ventanas = types.InlineKeyboardButton('Bloquear puertas y ventanas', callback_data='bloquear_puertas_ventanas')

    # Agregamos los botones del menú al markup
    markup.add(btn_activar_alarma, btn_llamar_policia, btn_monitorear_camara, btn_bloquear_puertas_ventanas)

    # Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Qué deseas realizar?\n<b>Selecciona una opción:</b>", parse_mode="html", reply_markup=markup)

# Responde al comando /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Puedes interactuar conmigo usando comandos. Por ahora, solo respondo a /start y /help')

# Responde a los mensajes de texto que no son comandos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Escribe un comando disponible.")
    else:
        bot.send_message(message.chat.id, "Este no es un comando valido. Por favor, escribe un comando valido que inicie con '<b>/</b>'.", parse_mode="html")

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# bot.reply_to(message, message.text)

# Responde a cada una de las opciones del menú que son enviadas con /start
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'activar_alarma':
        bot.answer_callback_query(call.id, "Se ha enviado la petición para que suene la alarma", show_alert=True)
        respuesta_alarma = bot.send_message(call.message.chat.id, "Intentando establecer conexión con el sistema...")
        time.sleep(3)
        bot.edit_message_text("Alarma en curso...", call.message.chat.id, respuesta_alarma.message_id)
    elif call.data == 'llamar_policia':
        bot.answer_callback_query(call.id, "Se ha enviado la petición para que se establezca la llamada con la policia", show_alert=True)
        respuesta_policia = bot.send_message(call.message.chat.id, "Intentando establecer conexión con el sistema...")
        time.sleep(3)
        bot.edit_message_text("Llamada en curso...", call.message.chat.id, respuesta_policia.message_id)
    elif call.data == 'monitorear_camara':
        bot.answer_callback_query(call.id, "Monitoreando camara...", show_alert=True)
    elif call.data == 'bloquear_puertas_ventanas':
        bot.answer_callback_query(call.id, "Puertas y ventanas bloqueadas", show_alert=True)

@bot.message_handler(commands=['foto'])
def send_image(message):
    img_url = 'https://c0.klipartz.com/pngpicture/40/304/gratis-png-discos-compactos-guadalajara-chivas-usa-houston-dynamo-san-jose-terremotos-liga-mx-futbol-thumbnail.png'
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption='El mejor equipo del futbol mexicano')

# Modulo principal del programa
if __name__ == "__main__":
    print('Iniciando el bot')
    bot.polling(none_stop=True)
    print('Bot finalizado')