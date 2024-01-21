import os

from dotenv import load_dotenv

load_dotenv()

import telebot
import datetime
import time
import threading


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

lastChatId = 0
reminders_set = False

@bot.message_handler(commands=['start'])
def on_start(message):
    lastChatId = message.chat.id
    bot.send_message(message.chat.id, "Hi! What would you like to do?"+"\n"+"\n"+"/setreminders - Start receiving morning, afternoon, and evening reminders to perform simple actions to reduce the likely food of a monkey bothering you." +"\n"+"\n"+"/tips - Receive general tips for avoiding human wildlife conflict"+"\n"+"\n"+"/stopreminders - Stop reminders from being sent.")

@bot.message_handler(commands=['tips'])
def tips_handler(message):
    text = "Here are my general tips!/n/nWhen monkeys are not around: /n1. Close your windows when monkeys are around, or when nobody is at home/n2. Keep food out of sight/n3. Collect food deliveries promptly/n/nIf you see a moneky:/n1. Do not smile or bare your teeth (this is a sign of aggression!)/n2. Do not make eye contact with the monkey/n3. Do not approach the monkey/n4. Do not corner the monkey, and gently tap the ground with a stick to lead it towards the exit."
    bot.reply_to(message,text, parse_mode="Markdown")

@bot.message_handler(commands=['setreminders'])
def reminders_handler(message,reminders_set):
    text = "Reminders started!"
    reminders_set = True
    bot.reply_to(message,text, parse_mode="Markdown")

@bot.message_handler(commands=['stopreminders'])
def reminders_handler(message):
    text = "Reminders stopped!"
    reminders_set = False
    bot.reply_to(message,text, parse_mode="Markdown")


    
def message_timer(lastChatId):
    while 1:
        if str (datetime.datetime.now().strftime("% H")) == "7":
            bot.send_message(lastChatId, "Good morning! Remember to close your windows before you leave!")
            time.sleep(60*65)
        elif str (datetime.datetime.now().strftime("% H")) == "13":
            bot.send_message(lastChatId, "Good afternoon! Remember to collect any food deliveries promptly today!")
            time.sleep(60*65)
        elif str (datetime.datetime.now().strftime("% H")) == "20":
            bot.send_message(lastChatId, "Good evening! Remember to dipose of any food waste properly before you sleep!")
            time.sleep(60*65)

if reminders_set == True:
    message_timer(lastChatId)

x = threading.Thread(target=message_timer)
x.start()

bot.infinity_polling()


