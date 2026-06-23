import telebot
from datetime import datetime

TOKEN = "8924487190:AAFqbLZlNDWBWLvNlPKe-7QzKhq1Cq4i1lE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to my bot! Use /help to see commands.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Available commands:\n/start\n/help\n/echo\n/time")

@bot.message_handler(commands=['echo'])
def echo(message):
    bot.reply_to(message, "Send /echo followed by your message.")

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['time'])
def time(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, "Current time: " + current_time)

print("Bot is running...")
bot.infinity_polling()