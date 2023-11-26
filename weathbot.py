import requests
import telebot
import random
from telebot import types
url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = 'your openweathermap api key'
api_telegram = 'your api key from telegram botfather'

bot = telebot.TeleBot(api_telegram)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Cześć, ' + str(message.from_user.first_name) + '👋👋,' + '\n\n' +
     'Jeżeli chcesz dane o pogodzie , wprowadz nazwę miasta!\n\n/help -Jeżeli potrzebujesz pomocy!🤙🤙')


@bot.message_handler(commands=['help'])
def welcome(message):
    sti = open('AnimatedSticke1r.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, '/start - Uruchomianie bota \n/help - Komendy bota\nJeżeli chcesz dane o pogodzie , poprostu wprowadz nazwę miasta(za każdym razem-pomownie): ')
 

@bot.message_handler(content_types=['text'])
def test(message):
    city_name = message.text
    try:
        params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'pl'}
        result = requests.get(url, params=params)
        weather = result.json()


        if weather["main"]['temp'] < 10:
            status = "Teraz jest bardzo chłodno lepiej ubierz ciepłą kurtkę i buty.❄️❄️\n\nLepiej nie pić alkoholu na ulice, można zmarznąć, poczucie ciepła jest oszustwem! 🥶😱🧐\n\nHerbatka- to najlepszy warunek😉!\n\n"
            sti = open('AnimatedSticker7.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif weather["main"]['temp'] < 20:
            status = "Teraz nie jest bardzo ciepło, ubieraj się ciepło!☁️☁️\n\n Jeżeli chcesz alkoholu, to lepiej pójdz z kolegami do baru!🤪!\n\n"
            sti = open('AnimatedSticker6.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        elif weather["main"]['temp'] > 27:
            status = "Teraz jest pięknie! ubieraj się jak chcesz!☀️☀️ Dobra pogoda , żeby pojechać do lasu na wycięczke! 😎☀️"
            sti = open('AnimatedSticke2r.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
        else:
            sti = open('AnimatedSticker5.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            status = "Teraz jest piękna temperatura!😍😍"

        bot.send_message(message.chat.id, "☀🌡 W mieście " + str(weather["name"]) + " temperatura " + str(float(weather["main"]['temp'])) + " celsjusza.\n\n" + 
                "☀️🌡 Maksymalna temperatura: " + str(float(weather['main']['temp_max'])) + " celsjusza.\n\n" + 
                "☀️🌡 Мinimalna temperatura: " + str(float(weather['main']['temp_min'])) + " celsjusza.\n\n" + 
                "💨 Prędkość wiatru: " + str(float(weather['wind']['speed'])) + " m/s.\n\n" + 
                "🤕 Ciśnienie: " + str(float(weather['main']['pressure'])) + " bar.\n\n" + 
                "💧 Wilgotność: " + str(int(weather['main']['humidity'])) + "%" + "\n\n" + 
                "🧐 Widocznośc: " + str(weather['visibility']) + " m.\n\n" + 
                "🤓 Opis: " + str(weather['weather'][0]["description"]) + "\n\n" + status)

    except:

        bot.send_message(message.chat.id, "Miasto  " + city_name + " nie znajdzione!")


bot.polling(none_stop=True)
