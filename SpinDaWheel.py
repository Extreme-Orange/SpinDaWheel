import telebot
import time
import random
from telebot import TeleBot, types, custom_filters
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter

bot = telebot.TeleBot("6143843981:AAHhRkwV32luBrvhhh2x6FBK2wScU-0fZJ8")

# Define things
places = dict()

# Start
@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "This bot is meant to help raeanne decide where to eat. Add the names of the places you wanna choose between :)")

# Reset
@bot.message_handler(commands=['reset'])
def reset(message):
    try:
        places[message.from_user.first_name].clear()
        bot.send_message(message.chat.id, "Done")
    except:
        bot.send_message(message.chat.id, "No existing input")

# Spin
@bot.message_handler(commands=['spin'])
def spin_thing(message):
    choice1 = random.choice(places[message.from_user.first_name])
    start_message = bot.send_message(message.chat.id, f"Spinning...\n{choice1}")
    i = 0
    while i <= 30:
        try:
            choice = random.choice(places[message.from_user.first_name])
            bot.edit_message_text(f"Spinning...\n{choice}", chat_id=message.chat.id, message_id = start_message.message_id)
            time.sleep(0.01)
            i += 1
        except:
            i += 1
            continue
    choice = random.choice(places[message.from_user.first_name])
    bot.edit_message_text(f"You should go to {choice}", chat_id=message.chat.id, message_id = start_message.message_id)

# Entering locations
@bot.message_handler(func=lambda m: True)
def location(message):
    bot.send_message(message.chat.id, f"Ok {message.text} added")
    if message.from_user.first_name not in places:
        places[message.from_user.first_name] = [f"{message.text}"]
    else:
        places[message.from_user.first_name].append(f"{message.text}")

bot.infinity_polling()