import os
import telebot

bot = telebot.TeleBot('1734761310:AAHCXZqheeUklJU2DbbxWXO43ax2N-cv-zc') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def saludo(mensaje):
    bot.reply_to(mensaje, "Hola, Estoy disponible")
    print("Mandaron saludo")


@bot.message_handler(commands=['dolar', 'age'])
def edad(mensaje):
    bot.reply_to(mensaje, "El cambio del dolar es de 23.94")
    print("Mandaron dolar")

@bot.message_handler(commands=['euro', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "El cambio del euro es de 28.07")
    print("Mandaron euro")

@bot.message_handler(commands=['oro', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "El precio del oro es de 43097.31")
    print("Mandaron oro")

@bot.message_handler(commands=['cafe', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "El precio del cafe es de 3503.28 ")
    print("Mandaron cafe")

bot.polling()