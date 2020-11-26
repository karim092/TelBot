import telebot@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\nЯ бот Первой помощи, что случилось?")

my_list = ['Паническая атака', 'Инсульт']
@bot.message_handler(content_types=["text"])
def first(message):
    if message.text in my_list:
        text = message.text
        with open(f"{text}.txt", encoding='utf-8') as f:
            text = f.read()
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, 'Ничего не удалось найти сэр')


bot.polling(none_stop=True)


bot = telebot.TeleBot('1088507126:AAF6k3_GIhAcClpMOzyTjtKSrFxMIuGI3Ow')




