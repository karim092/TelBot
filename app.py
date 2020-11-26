import telebot

bot = telebot.TeleBot('1088507126:AAF6k3_GIhAcClpMOzyTjtKSrFxMIuGI3Ow')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()))



