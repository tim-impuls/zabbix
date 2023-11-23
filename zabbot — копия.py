#!/bin/env python
import prettytable as pt
from prettytable import PLAIN_COLUMNS # убрать из таблицы разделитили
import os  # для пинга 
import paramiko # для SSh  запросов
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, callback_query, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton 
from datetime import datetime, timedelta
last_click_time = {}  # переменная для отработки нажатия  Все не чаще 5 минут
last_click_time1 = {}
last_click_time2 = {}
last_click_time3 = {}
last_click_time4 = {}
last_click_time5 = {}
last_click_time6 = {}
last_click_time7 = {}
last_click_time8 = {}
last_click_time9 = {}
last_click_time10= {}
last_click_time11= {}
last_click_time12= {}
last_click_time13= {}
last_click_time14= {}
import asyncio
import logging
import zabot  # импорт питон скрипта там заббикс запросы и формирование сообщений и отправка 


###################################################################
TOKEN = "6384143712:AAE1oBDmilKmNssW2IC1d0szm6JqsraWthc"  # токен бота                             
bot = Bot(token= zabot.TOKEN() )         
dp = Dispatcher(bot)
adm = [1052800295, 5690420121]  # список из id пользователей #5690420121 -  Тимур  #1052800295 Василий
################################################################# начальное меню на команду

import sys # импорт сис а потом принтуем пути где откуда можно импортировать
print(sys.path)

@dp.message_handler(commands=['camera'])
async def process_help_command(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)   # удаляем команду из чата
    markup =  types.InlineKeyboardMarkup(row_width=2)              # создаем клавиатуру
    butt_magadan_obl =  types.InlineKeyboardButton("Магаданская область",callback_data = 'magadan_obl')     # вариант меню
    butt_uzly_svyazi =  types.InlineKeyboardButton("Узлы связи",callback_data = 'uzly_svyazi')        
    butt_baza =  types.InlineKeyboardButton("База",callback_data = 'baza')
    butt_kvartiry =  types.InlineKeyboardButton("Квартиры",callback_data = 'kvartiry')
    butt_razvilka =  types.InlineKeyboardButton("Развилка",callback_data = 'razvilka')
    butt_permskiy_kray =  types.InlineKeyboardButton("Пермский край",callback_data = 'permskiy_kray')
    butt_ofis =  types.InlineKeyboardButton("Офис",callback_data = 'ofis')
    butt_magadan =  types.InlineKeyboardButton("Магадан",callback_data = 'magadan')
    butt_kudymkar =  types.InlineKeyboardButton("Кудымкар",callback_data = 'kudymkar')
    butt_krasnovishersk =  types.InlineKeyboardButton("Красновишерс",callback_data = 'krasnovishersk')
    butt_kirovskaya_oblast =  types.InlineKeyboardButton("Кировская область",callback_data = 'kirovskaya_oblast')
    butt_yakutiya =  types.InlineKeyboardButton("Якутия",callback_data = 'yakutiya')
    butt_klient =  types.InlineKeyboardButton("Клиент",callback_data = 'klient')
    butt_uzly_svyazi_PK =  types.InlineKeyboardButton("Узлы связи ПК",callback_data = 'uzly_svyazi_PK')
    butt_VSE =  types.InlineKeyboardButton("ВСЕ",callback_data = 'VSE')

    markup.add(butt_VSE)
    markup.add(butt_magadan_obl,butt_uzly_svyazi)
    markup.add(butt_baza,butt_kvartiry) 
    markup.add(butt_razvilka,butt_permskiy_kray)
    markup.add(butt_ofis,butt_magadan)
    markup.add(butt_kudymkar,butt_krasnovishersk)
    markup.add(butt_kirovskaya_oblast,butt_yakutiya)
    markup.add(butt_klient,butt_uzly_svyazi_PK)

    
    await bot.send_message(message.chat.id, 'Выберите группы для проверки', reply_markup=markup ) # сообщение после вывода клавиатуры

######################################################################################################################################### uzly_svyazi ofis
def log(group):                 # функция логирования. Можно заменить название файла. Создаётся там же где и скрипт лежит. Если не нужно тогда отредактиовать саму функцию, чтобы ничего не записывала. Быстрее чем весь код править и удалять
    with open("log_zabbot.txt", "a") as f:# открываем файл или создаем, елси его нет и ... 
        f.write(group + str(datetime.now()))   # добавляем название и время
        f.close()
    

@dp.callback_query_handler(text="VSE")
async def send_random_value(call: types.CallbackQuery): 
    log('\nVSE ')  
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time.get(button_id) and current_time - last_click_time[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#      
    else:
        await call.answer("Пару минут... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time[button_id] = current_time   # записываем время нажатия
        
        text = zabot.magadan_obl()
        text += zabot.uzly_svyazi()
        '''
        text += zabot.baza()
        text += zabot.kvartiry()
        text += zabot.razvilka()
        text += zabot.permskiy_kray()
        text += zabot.ofis()
        text += zabot.magadan()
        text += zabot.kudymkar()
        text += zabot.krasnovishersk()
        text += zabot.kirovskaya_oblast()
        text += zabot.yakutiya() 
        text += zabot.uzly_svyazi_PK()
        text += zabot.klient()'''
        print(text)
        
        await bot.send_message(call.message.chat.id,text=text)
        zabot.logout()
###########################################
@dp.callback_query_handler(text="magadan_obl")
async def send_random_value(call: types.CallbackQuery):  
    log('\nmagadan_obl ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time1.get(button_id) and current_time - last_click_time1[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time1[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.magadan_obl())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="uzly_svyazi")
async def send_random_value(call: types.CallbackQuery):
    log('\nuzly_svyazi ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time2.get(button_id) and current_time - last_click_time2[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time2[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.uzly_svyazi())
        zabot.logout()
###########################################    
@dp.callback_query_handler(text="baza")
async def baza(call: types.CallbackQuery):        
    log('\nbaza ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time3.get(button_id) and current_time - last_click_time3[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time3[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.baza())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="kvartiry")
async def send_random_value(call: types.CallbackQuery):
    log('\nkvartiry ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time4.get(button_id) and current_time - last_click_time4[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time4[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.baza())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="razvilka")
async def send_random_value(call: types.CallbackQuery):
    log('\nrazvilka ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time5.get(button_id) and current_time - last_click_time5[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time5[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.baza())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="permskiy_kray")
async def send_random_value(call: types.CallbackQuery):
    log('\npermskiy_kray ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time14.get(button_id) and current_time - last_click_time14[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time14[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.permskiy_kray())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="ofis")
async def send_random_value(call: types.CallbackQuery):
    log('\nofis ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time6.get(button_id) and current_time1 - last_click_time6[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time6[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.ofis())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="magadan")
async def send_random_value(call: types.CallbackQuery):
    log('\nmagadan ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time7.get(button_id) and current_time - last_click_time7[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time7[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.magadan())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="kudymkar")
async def send_random_value(call: types.CallbackQuery):
    log('\nkudymkar ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time8.get(button_id) and current_time - last_click_time8[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time8[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.kudymkar())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="krasnovishersk")
async def send_random_value(call: types.CallbackQuery):
    log('\nkrasnovishersk ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time9.get(button_id) and current_time - last_click_time9[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time9[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.krasnovishersk())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="kirovskaya_oblast")
async def send_random_value(call: types.CallbackQuery):
    log('\nkirovskaya_oblast ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time10.get(button_id) and current_time - last_click_time10[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time10[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.kirovskaya_oblast())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="yakutiya")
async def send_random_value(call: types.CallbackQuery):
    log('\nyakutiya ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time11.get(button_id) and current_time - last_click_time11[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time11[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.yakutiya())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="klient")
async def send_random_value(call: types.CallbackQuery):
    log('\nklient ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time12.get(button_id) and current_time - last_click_time12[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time12[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.klient())
        zabot.logout()
########################################### 
@dp.callback_query_handler(text="uzly_svyazi_PK")
async def send_random_value(call: types.CallbackQuery):
    log('\nuzly_svyazi_PK ')
    button_id = call.data[6:]         #
    current_time = datetime.now()   # узнаем текущее время
    if last_click_time13.get(button_id) and current_time - last_click_time13[button_id] < timedelta(seconds=300):   # если 5 минут не прошло с последнего нажатия не будет проверять узлы
        await call.answer('Пожалуйста попробуйте позже.', show_alert=True)
#        await call.answer('Пожалуйста попробуйте позже.')
    else:
        await call.answer("Минуту... проверяю...", show_alert=True)    #всплывает сообщение
        last_click_time13[button_id] = current_time   # записываем время нажатия
        await bot.send_message(call.message.chat.id,text=zabot.uzly_svyazi_PK())
        zabot.logout()
########################################### 
#executor.start_polling(dp)
#чтобы крутился скрипт
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)