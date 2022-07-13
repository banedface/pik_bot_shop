# -*- coding: utf-8 -*-
from distutils.cmd import Command
import telebot
from telebot import types
import logging

 
bot = telebot.TeleBot('5072084974:AAEP1y750xK1HGVxzVlxxeXVk0CdcWbCHpw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("зарегистривоваться")
    btn2 = types.KeyboardButton(" каталог магазина")
    btn3 = types.KeyboardButton(" тех-поддержка")
    btn4 = types.KeyboardButton(" корзина")
    btn5 = types.KeyboardButton(" почта")
    
    
    markup.add(btn1, btn2, btn3 , btn4 , btn5)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Ты попал в магазин Pikshop".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "зарегистрироваться "):
        bot.send_message(message.chat.id, text="Привет.Тебе нужно проити регистрацию")
    elif(message.text == "каталог магазина"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("кофты")
        btn2 = types.KeyboardButton("футболки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="товары", reply_markup=markup)
        
            
      
        
       
    
    elif(message.text == "кофты"):
        bot.send_message(message.chat.id, "0 в наличий")
    
    elif message.text == "футболки":
        bot.send_message(message.chat.id, text="0 в наличий")
        
        
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("зарегистрироваться")
        button2 = types.KeyboardButton("каталог магазина")
        button3 = types.KeyboardButton("тех-поддержка")
        button4 = types.KeyboardButton("корзина")
        button5 = types.KeyboardButton("почта")
        markup.add(button1, button2 , button3, button4, button5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Привет.Тебе нужно проити регистрацию по ссылке https://b102041.hostde32.fornex.host/registration.html ссылка для авторизаций https://b102041.hostde32.fornex.host/authorization.html ")

bot.polling(none_stop=True)
    


