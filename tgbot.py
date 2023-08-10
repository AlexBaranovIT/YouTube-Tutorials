from telebot import TeleBot

TOKEN = 'Your Bot token from BotFather'
bot = TeleBot(TOKEN)

#Function that reacts on command start and sends welcome message
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hello!')

#Fuction that reacts on any text user typed, and send him echo response
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)

#Bot looking for updates none stop
bot.polling(none_stop=True)
