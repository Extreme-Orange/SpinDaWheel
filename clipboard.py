@bot.message_handler(func=lambda m: True)
def location(message):
    bot.send_message(message.chat.id, f"Ok, Option 1 is {message.text}")
    places[message.from_user.first_name] = f"{message.text}"