from telebot import TeleBot

TOKEN = 'Your Bot token from BotFather'
bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True, interval=0)
