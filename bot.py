# -*- coding: utf-8 -*-
import telebot
from telebot import types


bot = telebot.TeleBot('1796228286:AAGUpZ002o8qlxmU_l6Q3OC7AOX0eJBcNXk')

def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Текст кнопки')
    key2 = types.KeyboardButton('Текст второй кнопки')
    markup.add(key1)
    markup.add(key2)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=main())

@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == 'Текст кнопки':
        bot.send_message(message.chat.id, 'Текст 1', reply_markup=main())
    elif message.text == 'Текст второй кнопки':
        bot.send_message(message.chat.id, 'Текст 2', reply_markup=main())
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', reply_markup=main())

bot.polling()
